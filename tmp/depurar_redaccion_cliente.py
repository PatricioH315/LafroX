from pathlib import Path
import json,re
r=Path(__file__).resolve().parents[1]
paths=[r/'08_plan_riesgos/contenido.tex',r/'LAFROX-Subdocumento8-Anexos.tex',r/'LAFROX-Formulario-T-16.tex',*sorted((r/'08_plan_riesgos').glob('anexo-*.tex'))]
base={p.relative_to(r).as_posix():p.read_text(encoding='utf-8') for p in paths}
(r/'tmp/depuracion-cliente-base.json').write_text(json.dumps(base,ensure_ascii=False),encoding='utf-8')
changes={
'No se introducen precios ni valorización monetaria en S8.':'La comparación utiliza exclusivamente esfuerzo en HH.',
'; no se incorporan precios en este plan.':'.',
' No se presenta simulación Monte Carlo ni percentil de confianza.':'',
' No se presentan resultados de simulación, percentiles ni probabilidades de cumplimiento.':'',
'; el análisis no se presenta como simulación ni como resultado observado.':'. La evaluación posterior se verifica mediante las pruebas y evidencias exigidas.',
'sin atribuirle una persona no identificada por este':'conforme a la designación formal del CLIENTE',
'Las pruebas y medidas descritas son requisitos de habilitación; no se presentan como ejecutadas ni aprobadas.':'La habilitación requiere ejecutar las pruebas y aprobar la evidencia de cumplimiento.',
'Los responsables deben verificar la evidencia antes de autorizar el alcance afectado; describir un control no demuestra su ejecución ni acredita eficacia residual.':'Los responsables deben verificar la ejecución y eficacia de los controles antes de autorizar el alcance afectado.',
'No se afirma que una versión haya quedado sin soporte ni se inventa fecha de término.':'La vigencia del soporte y su fecha de término se verifican con la información publicada por el proveedor.',
'Se trabaja con cinco niveles propios, no con una escala atribuida a una norma:':'Se utilizan cinco niveles definidos para este proyecto:',
'Las puntuaciones posteriores son proyecciones condicionadas a evidencia, no una FMEA de controles ya ensayados.':'Las puntuaciones posteriores son proyecciones sujetas a la verificación de la evidencia de cada control.',
'No se calcula percentil ni suficiencia estadística: FMEA no es una simulación.':'La estimación corresponde al valor esperado; no determina percentiles ni suficiencia estadística de la reserva.',
' No es una probabilidad derivada de FMEA.':'',
'No hay evidencia suficiente de coincidencia entre esas capacidades técnicas y los perfiles, causas y períodos de los riesgos del CLIENTE; por ello el crédito inicial contra la nueva contingencia es cero.':'El crédito inicial contra la contingencia específica es cero y sólo podrá reconocerse tras verificar la coincidencia de capacidades, perfiles, causas y períodos.',
'Las respuestas son propuestas de tratamiento derivadas del evento, los disparadores y los responsables consignados en T-16; no certifican controles ya implementados ni eficacia residual.':'Las respuestas se activan según el evento y sus disparadores; los responsables deben ejecutar los controles y comprobar su eficacia con la evidencia indicada.',
'Se conserva el impacto inicial; no se borra una consecuencia sanitaria o contractual mediante mejor detección.':'El impacto residual mantiene la gravedad de las consecuencias sanitarias y contractuales, incluso con una mejor detección.',
'Son proyecciones de planificación condicionadas a la acción y su prueba; no se presentan controles previstos como eficaces ya comprobados.':'La valoración posterior está condicionada a ejecutar la acción y verificar su eficacia.',
'Sin esa conciliación no se afirma que la reserva estimada quepa en la capacidad propuesta ni que exista atraso o capacidad adicional cuantificada.':'La aprobación de la reserva requiere verificar su cobertura con la capacidad disponible y cuantificar cualquier refuerzo o efecto sobre el calendario.',
'; no se presume ensayo ejecutado.':'. La habilitación requiere aprobar estos ensayos.',
'Ninguna proyección acredita eficacia comprobada ni capacidad o financiamiento aprobados.':'La eficacia requiere verificación y la capacidad y el financiamiento están sujetos a aprobación.',
}
count=0
for p in paths:
 old=base[p.relative_to(r).as_posix()]
 # Toda la declaración de IA se conserva literalmente.
 cut=old.find('\\section*{Declaración de uso de IA}')
 if cut<0:cut=old.find('\\section*{Declaración de uso de Inteligencia')
 if cut<0 and 'contenido.tex'==p.name:
  cut=old.find('La declaración de uso de IA')
 prefix,suffix=(old[:cut],old[cut:]) if cut>=0 else (old,'')
 for a,b in changes.items():
  count+=prefix.count(a);prefix=prefix.replace(a,b)
 new=prefix+suffix
 # Todas las filas técnicas permanecen numéricamente idénticas; se permite retirar referencias editoriales como S8.
 for a,b in zip([x for x in old.splitlines() if ' & ' in x],[x for x in new.splitlines() if ' & ' in x]):
  assert re.findall(r'\d+(?:[.,]\d+)?',a)==re.findall(r'\d+(?:[.,]\d+)?',b),p
 assert [l for l in old.splitlines() if 'contenido academico' in l]==[l for l in new.splitlines() if 'contenido academico' in l],p
 if cut>=0:assert new.endswith(suffix)
 if new!=old:p.write_text(new,encoding='utf-8')
print(count,'ajustes editoriales; cifras y declaración de IA intactas.')
