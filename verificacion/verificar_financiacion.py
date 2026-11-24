"""Verifica la provisión propia del complemento sin publicar importes en la oferta técnica.

Usa la copia del modelo que identifica asignacion_complementaria.json y requiere
openpyxl. Solo lee el libro. No recalcula ni atribuye nuevos VAN/TIR al modelo.
"""
from pathlib import Path
from decimal import Decimal
import argparse
import hashlib
import json
import openpyxl

SD10=Path(__file__).resolve().parents[1]
DEFAULT_MODEL=SD10.parent/'tmp/lafrox-revision-sd4-20261114/SD7/outputs/sd7-ajuste-20261122/LafroX_ModeloFinanciero_3_SD7.xlsx'

def verify(model):
    assignment=json.loads((SD10/'trazabilidad/asignacion_complementaria.json').read_text(encoding='utf-8'))
    initial=hashlib.sha256(model.read_bytes()).hexdigest()
    assert initial==assignment['fuente_financiera_sha256'], 'Cambió la fuente financiera; recalcular asignación y financiación'
    values=openpyxl.load_workbook(model,read_only=True,data_only=True)
    formulas=openpyxl.load_workbook(model,read_only=True,data_only=False)
    sheet=values['COSTOS HH - SUELDOS']
    def decimal(value):
        assert isinstance(value,(float,int)), 'Dato económico ausente o no numérico'
        return Decimal(str(value))
    rates={}
    for profile,row in [('17',40),('30',41),('12S',16)]:
        assert formulas['COSTOS HH - SUELDOS'][f'H{row}'].value==f'=E{row}*F{row}'
        assert formulas['COSTOS HH - SUELDOS'][f'G{row}'].value==f'=MAX(F{row}*PARAMETROS!$C$55,P{row})'
        cost=decimal(sheet[f'F{row}'].value)
        provision=max(cost*decimal(values['PARAMETROS']['C55'].value),decimal(sheet[f'P{row}'].value))
        assert abs(provision-decimal(sheet[f'G{row}'].value))<Decimal('0.0000001')
        assert abs(decimal(sheet[f'R{row}'].value)-decimal(assignment['base_HH'][profile]))<Decimal('0.000001')
        rates[profile]=(cost,provision)
    fields={'17':'perfil_17_mesa_HH','30':'perfil_30_NOC_HH','12S':'perfil_12S_integracion_HH'}
    total_cost=Decimal(0)
    total_provision=Decimal(0)
    balances=[]
    assert [m['mes_contractual'] for m in assignment['meses']]==list(range(21,57))
    for month in assignment['meses']:
        cost=sum((Decimal(month[field])*rates[profile][0] for profile,field in fields.items()),Decimal(0))
        provision=sum((Decimal(month[field])*rates[profile][1] for profile,field in fields.items()),Decimal(0))
        assert provision>=cost
        total_cost+=cost
        total_provision+=provision
        col=month['mes_contractual']+2
        assert values['INDICADORES'].cell(28,col).value==month['mes_contractual']
        balances.append(decimal(values['INDICADORES'].cell(32,col).value)-total_provision)
    margin=decimal(values['RESUMEN']['L11'].value)
    assert total_provision<margin, 'La provisión supera el margen de referencia'
    assert min(balances)>0, 'La provisión genera un déficit acumulado durante Operación'
    assert hashlib.sha256(model.read_bytes()).hexdigest()==initial
    values.close()
    formulas.close()
    return {'proyecto':'LafroX','passed':True,'meses':36,'perfiles':3,
            'HH_complementarias':sum(m['total_complementario_HH'] for m in assignment['meses']),
            'fuente_financiera_sha256':initial,'costos_y_tarifas_reproducidos':True,
            'margen_y_saldos_operacion_positivos':True,'libro_fuente_modificado':False,
            'limite':'Provisión contra el modelo de referencia identificado; no actualiza su VAN/TIR ni acredita contratación, aprobación o financiación efectivamente desembolsada.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--modelo',type=Path,default=DEFAULT_MODEL)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=verify(args.modelo)
    if args.output:
        args.output.write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    print(json.dumps(result,ensure_ascii=False,indent=2))
