# LafroX — Manifiesto de alineación del Subdocumento 4

## Versión lógica posterior — 5 de octubre de 2026

Se aplicó el plan de coherencia con el SD3 actual de Descargas y los quince actores validados. Las fuentes iniciales y huellas siguientes se conservan como procedencia histórica; los canónicos lógicos y sus partes tienen cambios autorizados posteriores a `732a9d6`. Física, centros de datos, 4-W y T-11 conservan su contenido. Consultar [Coherencia y dependencias](COHERENCIA_SD3_SD4_2026-10-05.md) y [verificación vigente](VERIFICACION_COHERENCIA_2026-10-05.md) antes de atribuir alineación técnica o regenerar.

Fecha: 3 de octubre de 2026.

Fuente: `rama-latex`, commit `732a9d6688569bf981594c2e21c47a167b8f8ba7`. Destino: `alvaro-md`, base `e377a58085c6f5c979a5bf176ecb710ce9239bbb`.

Se convierten los fragmentos ensamblados del cuerpo, anexos y T-11. La numeración de tablas y figuras del cuerpo es corrida; las páginas se sustituyen por enlaces. Los cuatro diagramas TikZ conservan un enlace al fuente y una transcripción de rótulos. No se crean fuentes LaTeX ni binarios en el destino.

## Comprobaciones

```json
{
  "source_commit": "732a9d6688569bf981594c2e21c47a167b8f8ba7",
  "base_commit": "e377a58085c6f5c979a5bf176ecb710ce9239bbb",
  "fragments": 61,
  "tables": 77,
  "data_rows": 822,
  "cells_including_headers": 3828,
  "figures": 26,
  "tikz_figures": 4,
  "plain_paragraphs_checked": 258,
  "identifiers_checked": 187,
  "documents": {
    "LAFROX-Subdocumento4.md": {
      "tables": 40,
      "rows": 303
    },
    "LAFROX-Subdocumento4-Anexos.md": {
      "tables": 36,
      "rows": 429
    },
    "LAFROX-Formulario-T-11.md": {
      "tables": 1,
      "rows": 90
    }
  }
}
```

Las filas y celdas de todas las tablas se contrastaron con la representación convertida de cada celda fuente. Los párrafos sin comandos se cotejaron por normalización; los identificadores técnicos se verificaron en conjunto. La conversión no acredita revisión humana, pruebas operacionales ni cumplimiento de las Bases.

## Fuentes y huellas SHA-256

| Fuente | SHA-256 |
| --- | --- |
| [04/anexos/fisica/16_anexo_4b_memoria_calculo.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex) | `e294d5a885e928a45cedafc90ea5809ebbc10fb38440fadfe583bb063a340db4` |
| [04/anexos/logica/contenido.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/contenido.tex) | `a1680d2c0e4bb6d1068cce1e05169adbb171e2a7d619fdf2bdb71b93c42d8667` |
| [04/anexos/logica/partes/00_catalogo_anexos.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/00_catalogo_anexos.tex) | `46b2fba7c8b58694ae9e49f5820879509a3b63fc0ce4850c47aa54459112f279` |
| [04/anexos/logica/partes/01_apertura_anexos.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/01_apertura_anexos.tex) | `341fc6994492d407d37e011b19a43b467e9f03d8c94e33c44ce1368e7896f19d` |
| [04/anexos/logica/partes/02_anexo_4_1_a_catalogo_de_eventos_canonicos.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/02_anexo_4_1_a_catalogo_de_eventos_canonicos.tex) | `a6b5736bd59bcaac73371bf1416de99c181b3d08d395aebe33bf7ff467434e0a` |
| [04/anexos/logica/partes/03_anexo_4_1_b_gobierno_de_la_integracion.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/03_anexo_4_1_b_gobierno_de_la_integracion.tex) | `f0a40ab79782c1dc9088e5729dcc4f5690170624f9650a1f60f23840aa8afe4f` |
| [04/anexos/logica/partes/04_anexo_4_1_c_escenarios_de_carga_masiva.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/04_anexo_4_1_c_escenarios_de_carga_masiva.tex) | `90e2f19ebe7d06baecef7a5c0bb742ddaedbb0249687093bf90336c900231ea9` |
| [04/anexos/logica/partes/05_anexo_4_1_d_matriz_de_los_doce_modulos.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/05_anexo_4_1_d_matriz_de_los_doce_modulos.tex) | `48e3fa7b5453ac3719d7322480ef57aebc24a4455a2ec95e6bbbaef986c9b364` |
| [04/anexos/logica/partes/06_anexo_4_1_e_trazabilidad_funcional.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/06_anexo_4_1_e_trazabilidad_funcional.tex) | `6aaa44b164ed447c6ffb3a340265c09bf4e2eb97cb1aa20d936b35376068e9fb` |
| [04/anexos/logica/partes/07_anexo_4_1_f_mapa_de_limites_de_contexto.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/07_anexo_4_1_f_mapa_de_limites_de_contexto.tex) | `c70010e220a19dfbe3ad7ba20ad9fc63939c75a56ccde53a4d0117492b991e96` |
| [04/anexos/logica/partes/08_anexo_4_1_g_catalogo_de_interfaces_internas.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/08_anexo_4_1_g_catalogo_de_interfaces_internas.tex) | `1bb284fcf8fa4098eeb80100883698029439c50180c3f2d88e52aa2bbde3c75a` |
| [04/anexos/logica/partes/09_anexo_4_1_h_catalogo_de_interfaces_externas.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/09_anexo_4_1_h_catalogo_de_interfaces_externas.tex) | `466a20401ba7e78c417792805758a3ded2268e54cdd462628515cffae51a2a8b` |
| [04/anexos/logica/partes/10_anexo_4_1_i_volumen_de_mensajes.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/10_anexo_4_1_i_volumen_de_mensajes.tex) | `052512b39eb2cefbba396747540a0e7b37bd871044de0956cfd17063ed6ba8e4` |
| [04/anexos/logica/partes/11_anexo_4_1_j_funciones_sin_conexion.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/11_anexo_4_1_j_funciones_sin_conexion.tex) | `a32ee37df7966df1d7de4fb963c322f24dd389ea57b5b5ede3cdfe3e75b5a1b9` |
| [04/anexos/logica/partes/12_anexo_4_1_k_reglas_de_reconciliacion.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/12_anexo_4_1_k_reglas_de_reconciliacion.tex) | `059ebaba7d09f26ea7edbed5bc1d2f083a2a027f3b803b03de94ca87e20e3fd6` |
| [04/anexos/logica/partes/13_anexo_4_1_l_decisiones_del_numeral_16_1.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/13_anexo_4_1_l_decisiones_del_numeral_16_1.tex) | `72c1e8e96a3ca3b40f60f0ee5fe17e934717ac835a716bd577a4b762ab01cd34` |
| [04/anexos/logica/partes/14_anexo_4_1_m_verificacion_de_continuidad_logica.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/14_anexo_4_1_m_verificacion_de_continuidad_logica.tex) | `97435cbcd26fbaf299e8bf34cdc8552a8efda843e71cd9de16086baf21956c2e` |
| [04/anexos/logica/partes/15_anexo_4_1_n_correspondencia_de_componentes_logicos.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/15_anexo_4_1_n_correspondencia_de_componentes_logicos.tex) | `e2dc7c6889f23296b06e1dcf1696518df6960f72b088fad9d393f82bf968bdc6` |
| [04/anexos/logica/partes/16_referencias.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/16_referencias.tex) | `8cbed5f8917d4ba1d38e10cb1a0124c0b820f6e06aed8d3fbb09f7eff8c9fad3` |
| [04/anexos/logica/partes/17_declaracion_de_uso_de_ia.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/17_declaracion_de_uso_de_ia.tex) | `b89bc4f150e2ee40e09248490b8632266bcdeab85ae7a351e9640db6d8dc6d84` |
| [04/anexos/logica/partes/18_anexo_4_1_o_decisiones_logicas.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/18_anexo_4_1_o_decisiones_logicas.tex) | `7553319c98846018b5140ab03acd1b8c1127b12cd15b8387ab938bd8b06f8874` |
| [04/anexos/logica/partes/19_anexo_4_1_p_tecnologias_soporte.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/19_anexo_4_1_p_tecnologias_soporte.tex) | `23bc178cd0f943631c61d742afc7aab8f387eeab7886e81e9f060a72249d67ca` |
| [04/anexos/logica/partes/20_anexo_4_1_q_modelado_amenazas.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/20_anexo_4_1_q_modelado_amenazas.tex) | `c9e200a15357c185be1dae0c66035ce8e487e98ee05907c5026cfe50990fae95` |
| [04/anexos/logica/partes/21_anexo_4_1_r_controles_seguridad.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/21_anexo_4_1_r_controles_seguridad.tex) | `d9f06fa2c0f827d4cf0e5f0b5ac09d987b3b50981092603a07058c10e31a51e6` |
| [04/anexos/logica/partes/22_anexo_4_1_s_puntos_de_vista.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/22_anexo_4_1_s_puntos_de_vista.tex) | `04761104a787bfe12deff82e0156e850ccedfcd613a6715b01e12d2b60bd3a1e` |
| [04/anexos/logica/partes/23_anexo_4_1_t_desempeno.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/23_anexo_4_1_t_desempeno.tex) | `1d187465ae7cf103f250c7543624292a45366b1e3157aa1b89b2763910bd0610` |
| [04/anexos/logica/partes/24_anexo_4_1_u_evidencia_documental.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/24_anexo_4_1_u_evidencia_documental.tex) | `7b8196aa0830e2e1d46b664925797374e8e5729d7370929a73b05d8fe72788ab` |
| [04/anexos/logica/partes/25_anexo_4_1_v_aceptacion_y_dependencias.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos/logica/partes/25_anexo_4_1_v_aceptacion_y_dependencias.tex) | `8d64ca283be7c1dcfcb703ee14574d611ac1593c7c83b2a2449bd3efb3a14e6a` |
| [04/anexos_logica.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/anexos_logica.tex) | `2e41e974e04a8bd9197657b735c4b42b18f1ae61b7161dd5934a54451e5df6da` |
| [04/formulario_T11.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/formulario_T11.tex) | `239ecbd2aad4055f10c5f8e791b643e1f7e78614eb76923284e081e15ea580f4` |
| [04/formularios/T11/15_anexo_t11.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/formularios/T11/15_anexo_t11.tex) | `89218574a40b58e67d2bdcc3dfa42d7e96cf28d0e823168eb4426d89cbcad43d` |
| [04/partes/4.1_logica/01_introduccion.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/01_introduccion.tex) | `c27d0a2ab26deef79935f288d57068054b031f85294451924bb606f362654245` |
| [04/partes/4.1_logica/02_especificaciones_tecnologias_de_software_a_utilizar.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/02_especificaciones_tecnologias_de_software_a_utilizar.tex) | `a8129e3387cae7963076b7ac2f9572a0a3339223de588cb94f2ca2b7f3247b9d` |
| [04/partes/4.1_logica/03_principios_de_integracion.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/03_principios_de_integracion.tex) | `9f62a5ab968840d71c8714c9bbb34839ae3968649983b22fa05c58c9c849ff02` |
| [04/partes/4.1_logica/04_capas_de_la_arquitectura.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/04_capas_de_la_arquitectura.tex) | `fd542813935afd1ffdc914ca1cdd0829c537ede46e8381f5b6cda6ecc8266e51` |
| [04/partes/4.1_logica/05_modulos_funcionales_y_limites_de_contexto.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/05_modulos_funcionales_y_limites_de_contexto.tex) | `5b6fe9028969053a346d553464b8c6dbaec5204eb43c876b1f3c5cb15c8a8334` |
| [04/partes/4.1_logica/06_modelo_de_datos_conceptual.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/06_modelo_de_datos_conceptual.tex) | `c7c64b79f8e30b176a41852cd0c1ecee59aeeff4405f305bf7c3ad1662dd77b9` |
| [04/partes/4.1_logica/07_catalogo_de_interfaces.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/07_catalogo_de_interfaces.tex) | `4c953a293652e85adaeaf41c986d87f17685b985074f98910edadf2328bb10b3` |
| [04/partes/4.1_logica/08_detalle_de_tecnologias_seleccionadas.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/08_detalle_de_tecnologias_seleccionadas.tex) | `85399ddfb61b81344981cf67cf2f802c04e2a4fc4d1e63ff56c7252da118485b` |
| [04/partes/4.1_logica/09_implantacion_progresiva_del_backend_laravel.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/09_implantacion_progresiva_del_backend_laravel.tex) | `22d0d41b0ebba5ec7cba17e7221b0d32152c4c0b2b3f1a8f85f0d5905bccd524` |
| [04/partes/4.1_logica/10_ambientes_del_ciclo_de_vida_y_promocion_de_componentes.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/10_ambientes_del_ciclo_de_vida_y_promocion_de_componentes.tex) | `ce14fd467e765a0e53c0cbc1363e4c2b31f1675847ded9d0a02ac9b7f1b06d00` |
| [04/partes/4.1_logica/11_patrones_de_diseno_y_continuidad.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/11_patrones_de_diseno_y_continuidad.tex) | `709721e1bcb2d91d3b89a79614fd95fa3066a84a2c5fab14e956be2a7a0f4d22` |
| [04/partes/4.1_logica/12_registro_de_decisiones_de_arquitectura.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/12_registro_de_decisiones_de_arquitectura.tex) | `41b16342e14b8686bee92eec98fadd33ace026c15a947543d73a34c5ac5ec41d` |
| [04/partes/4.1_logica/13_puntos_unicos_de_falla_y_riesgos_residuales.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/13_puntos_unicos_de_falla_y_riesgos_residuales.tex) | `b34e824c2195f2493c08bb27db970098afc357de62a96b70b84656bb2c92c523` |
| [04/partes/4.1_logica/14_comparacion_de_alternativas_arquitectonicas.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/14_comparacion_de_alternativas_arquitectonicas.tex) | `64003f2de637705cf0f44fd75433a778197c2228014895735f2d53e07dde714b` |
| [04/partes/4.1_logica/15_relacion_entre_las_vistas_de_arquitectura.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/15_relacion_entre_las_vistas_de_arquitectura.tex) | `022ebc9bf52d085e8d854da2c040fc216436fc2caafe2e25abbd752d84e314d8` |
| [04/partes/4.1_logica/16_funciones_disponibles_y_no_disponibles_sin_conexion.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/16_funciones_disponibles_y_no_disponibles_sin_conexion.tex) | `df9db9abdc006c1939ef602ba8334073f06391409d92ec224f281e76ab21f654` |
| [04/partes/4.1_logica/17_reglas_de_reconciliacion.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/17_reglas_de_reconciliacion.tex) | `85304f127a03e22830d05f0f3c2eea226fc0825cceb764aac24c15c7f16b088f` |
| [04/partes/4.1_logica/18_articulacion_entre_prueba_de_entrega_dte_y_acuse.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/18_articulacion_entre_prueba_de_entrega_dte_y_acuse.tex) | `5139605353a091649c3ac27badd19946ab2a0557b297a12efb7751ec77455b54` |
| [04/partes/4.1_logica/19_identidad_y_ciclo_de_vida_de_conductores_externos.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/19_identidad_y_ciclo_de_vida_de_conductores_externos.tex) | `880fe1bfe818e95b9305466fafb5e130a63a488148c2509ee69758600c96dfbf` |
| [04/partes/4.1_logica/20_primer_cuello_de_botella_bajo_la_carga_de_septiembre.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/20_primer_cuello_de_botella_bajo_la_carga_de_septiembre.tex) | `2c2b0c7e37ce52c769ed404969bac955f7fc6890a0dca4eab01215716c576461` |
| [04/partes/4.1_logica/21_decisiones_del_numeral_16_1_del_caso.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/21_decisiones_del_numeral_16_1_del_caso.tex) | `74d6c5337b6d1574ab21fab27f2ff2ad86f778736847008e6427e572f17c3d6b` |
| [04/partes/4.1_logica/22_condiciones_y_supuestos_de_diseno.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/22_condiciones_y_supuestos_de_diseno.tex) | `7f0f6ef8fc2444e2bc9817c36cfc51b5c9bafca9b9c1f43db73ec0bd95b58128` |
| [04/partes/4.1_logica/contenido.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.1_logica/contenido.tex) | `fdcf51ab7363b7b61dc872d362cd14d3cc2f0c3c79938b80adfa6bbc54f4d687` |
| [04/partes/4.2_fisica/02_0_arquitectura_fisica.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/02_0_arquitectura_fisica.tex) | `2344bf1ce35987aaa2aea93d12c716682cc75c0b7c79d16ba1dbc3d4db7eb6ad` |
| [04/partes/4.2_fisica/02_a_emplazamiento.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/02_a_emplazamiento.tex) | `c6e6ea5631fcd02bdd613068dc3f4459ebd40322b225a5e0ebccd921358eb624` |
| [04/partes/4.2_fisica/02_b_servicios_nube.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/02_b_servicios_nube.tex) | `c4e9380a9c31e733bee8b8ac83183f7b37f98ba9f39474b298881c3fd1706c14` |
| [04/partes/4.2_fisica/02_c_conexiones.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/02_c_conexiones.tex) | `47cb69db89a830dc094d395f94b6b114b97f7accdd4961414b291d2b8deeea16` |
| [04/partes/4.2_fisica/04_c_implementos.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/04_c_implementos.tex) | `de75b56e1822c3ed6010f49be5ef8af760c7ed1717aeea83b0ff2bff059eabb0` |
| [04/partes/4.2_fisica/11_j_despliegue.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/11_j_despliegue.tex) | `97461bf6436d9010a225320a2196882245e8b0a2508a55d2e2bc11ccfa7c427b` |
| [04/partes/4.2_fisica/12_k_dimensionamiento.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/12_k_dimensionamiento.tex) | `3d563e207bf328a5aec095926366c95b16e5372c3333a211a5a6f19ac3379b4a` |
| [04/partes/4.2_fisica/contenido.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/contenido.tex) | `92dfa8246114291742c5848f541cec139ddfaef9bc7d580d830dccaf68fd7b71` |
| [04/partes/4.3_centros_de_datos/05_d_sitio_principal.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.3_centros_de_datos/05_d_sitio_principal.tex) | `75a4162c78d138ad82a469d2d0ccb715ecc3091fe89ff5680e273eb14771c78e` |
| [04/partes/4.3_centros_de_datos/06_e_sitio_secundario.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.3_centros_de_datos/06_e_sitio_secundario.tex) | `71996563a72f1c8ce14240977128652c9e2b9ce08f627a33f1867fe07f86ede6` |
| [04/partes/cierre/declaracion_de_uso_de_ia.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/cierre/declaracion_de_uso_de_ia.tex) | `11c8b5d8d5f53d519a3b85e0123724e7f1aa7669a21ccf7afc3cb388899f3270` |
| [04/partes/cierre/referencias.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/cierre/referencias.tex) | `d04937e5bc035ec63b541c5114ac8aabfda3426e8584e8eb14f6a1d9afc68468` |
| [contenido.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/contenido.tex) | `bef6bac661e7b06868080a93082dc7acda36c1d1fca0bb90723e48122a71d6d9` |
| [main.tex](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/main.tex) | `6aef262378ebcfe94801e4ca8a6d94557334f106501b1df7462699cb7a23a9cb` |

## Figuras vigentes

| Figura fuente | SHA-256 |
| --- | --- |
| [04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Concepcion.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Concepcion.png) | `6a3a7e2a31673679f549bb1413bb29ccca4d34085e23b07d4feaf5f5eb00cb0a` |
| [04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Talca.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Talca.png) | `672b1a47f08e01d40abf9d6a413b6022a1fc73586a2cb95e36a564e1af65f477` |
| [04/figuras/centros_de_datos/Racks_CD_Talca.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/centros_de_datos/Racks_CD_Talca.png) | `2a64303130a32e29f156f964b264c13db690f9a5f7b19c59be43e444dc1b6f2a` |
| [04/figuras/centros_de_datos/Recinto_CD_Talca.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/centros_de_datos/Recinto_CD_Talca.png) | `1f34c901cf7fb7129cb093008ecb8578482c0e28c148bea55fd3dd8c89b284ae` |
| [04/figuras/fisica/Arquitectura_Fisica_Crossdocking.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/Arquitectura_Fisica_Crossdocking.png) | `2f167e10cf577aea32e3865abb81cef4c7d20da9773e0b4ca5ac5e4380fa2bec` |
| [04/figuras/fisica/Arquitectura_Fisica_General.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/Arquitectura_Fisica_General.png) | `4b6d4a128599f4025ed31c73ef68ce36755d3ae22c1f7d301ce772cd61a916d4` |
| [04/figuras/fisica/Arquitectura_Fisica_Nube.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/Arquitectura_Fisica_Nube.png) | `1802a5152f1e3c3e927ca67605024ea843a40d15f45f1f2b284aad403c5786a7` |
| [04/figuras/fisica/ambientes/amb_desarrollo.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/ambientes/amb_desarrollo.png) | `6169bb7f89c8db0b6e325ba078dfd2d6ec96842c63235f7ac1c930640baff5a8` |
| [04/figuras/fisica/ambientes/amb_preproduccion.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/ambientes/amb_preproduccion.png) | `bceca7ae0e5494baec48c441b80906c80bca53ed488303e3be585de740e8db46` |
| [04/figuras/fisica/ambientes/amb_produccion.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/ambientes/amb_produccion.png) | `f6a29f8e8db8816b766ad007497f9fd12fa3a3dd5ea634a82124ae31c0ff6a99` |
| [04/figuras/fisica/ambientes/amb_qa.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/ambientes/amb_qa.png) | `d842e1a35473c1e5f4a44c1778e9858d53246c2ae87408a277653ddfc98549c6` |
| [04/figuras/fisica/ambientes/amb_recuperacion.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/ambientes/amb_recuperacion.png) | `08d980f24ce22873b36630260de3d35212a7c4284c027043be7859a6fc1ee91a` |
| [04/figuras/logica/ARQL-15_Pedido_con_conexion.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-15_Pedido_con_conexion.png) | `1b547a6d6a4050280fef1b1a96bb3a9499db58f29007dc2e437e2604ff62f159` |
| [04/figuras/logica/ARQL-16_Pedido_sin_conexion.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-16_Pedido_sin_conexion.png) | `cc56f33f1236cb8bba08a60125ee899110c07fa4ca9af6bb779b37863d97907f` |
| [04/figuras/logica/ARQL-17_Acceso_local_24h.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-17_Acceso_local_24h.png) | `919c55e078238e773a2aff983a8496ba00968cd06eacc1243bf8f9dbcaee2db2` |
| [04/figuras/logica/ARQL-18_Dominio_trazabilidad.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-18_Dominio_trazabilidad.png) | `80df9386a41229d5b8c7fd734025bc64621893701c7b1ce69cb055de86d27f2e` |
| [04/figuras/logica/ARQL-19_Vista_general_legible.pdf](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-19_Vista_general_legible.pdf) | `2e05db7b381bde3ab2a66bfa1ec812f5ecf78050a60c8b8515a6dcf8e8dc3981` |
| [04/figuras/logica/cambios laravel/ARQL-01_Vision_general.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/cambios%20laravel/ARQL-01_Vision_general.png) | `2de9ec88c51e63305e5bdb2ab1e05340b50d0d22afe6441d0a8d04c54a83b7f5` |
| [04/figuras/logica/capas_recortes/ARQL-21_Recorte_Presentacion.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-21_Recorte_Presentacion.png) | `2693dcb5c0f7d7bcec6a6e19e672bcb759ee011722e63f2f90b4af1881c4dc47` |
| [04/figuras/logica/capas_recortes/ARQL-22_Recorte_Borde.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-22_Recorte_Borde.png) | `7c507d482d1b42a7862781fce9a811eeebe6645fb505fb85f2eda8bfc5161017` |
| [04/figuras/logica/capas_recortes/ARQL-23_Recorte_Puertas.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-23_Recorte_Puertas.png) | `2cd57182cfff0716028766043141731f1641636386ea7a4b2103c8b2d15c5278` |
| [04/figuras/logica/capas_recortes/ARQL-24_Recorte_Negocio.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-24_Recorte_Negocio.png) | `dc848744f6ac2b98168d6ba72322de232e818a033e71111ccd94e1a93ec5faa7` |
| [04/figuras/logica/capas_recortes/ARQL-25_Recorte_Integracion.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-25_Recorte_Integracion.png) | `ce0cfc5de322f8c616649029c75caba23402deb5c9c06b37f62adc32590f98f6` |
| [04/figuras/logica/capas_recortes/ARQL-26_Recorte_Datos.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-26_Recorte_Datos.png) | `a59ce2406223a76ee407ff76447999e54500f60c6882485395a4e7b82afdc7e0` |
| [04/figuras/logica/capas_recortes/ARQL-27_Recorte_Seguridad.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-27_Recorte_Seguridad.png) | `eb37a66d715856b9428d24f324450068406f19c0f07d6c009fb040676f0f7629` |
| [04/figuras/logica/capas_recortes/ARQL-28_Recorte_Observabilidad.png](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-28_Recorte_Observabilidad.png) | `1dd730e504119ce4b2033c4c5aad2ecf4b3414e4132d31bb8597bd093a332e09` |

## Salidas técnicas y huellas SHA-256

| Archivo | SHA-256 |
| --- | --- |
| [LAFROX-Formulario-T-11.md](<LAFROX-Formulario-T-11.md>) | `ec13547611dc591c4ca8ec9f23da9eb8190405299fe6189b70bd01c709523046` |
| [LAFROX-Subdocumento4-Anexos.md](<LAFROX-Subdocumento4-Anexos.md>) | `61acb17adcc3e48b8606be0e2fac66368950db6c6eb09a0b365c41718d2a2a60` |
| [LAFROX-Subdocumento4.md](<LAFROX-Subdocumento4.md>) | `f683b804cfdb368f2d8aafb44891cc369130ddfa5fac3a4d044fafeaaf9b8590` |
| [MD_4.2_2.3/Subdocumento_4_completo.md](<MD_4.2_2.3/Subdocumento_4_completo.md>) | `c44bd1a2e0882c65f32df01ae73f20d2fdde1e41c4e47844f002ef5fc90ca2e3` |
| [MD_4.2_2.3/partes/02_0_arquitectura_fisica.md](<MD_4.2_2.3/partes/02_0_arquitectura_fisica.md>) | `7704948cb78fac4fe39003041b761cf7a90cb38e709455fe73fb5f06b937c48c` |
| [MD_4.2_2.3/partes/02_a_emplazamiento.md](<MD_4.2_2.3/partes/02_a_emplazamiento.md>) | `fed9b412888fc107b6d941b75943190218f8c6f6b5cdeb5037e16408654c4cf2` |
| [MD_4.2_2.3/partes/02_b_servicios_nube.md](<MD_4.2_2.3/partes/02_b_servicios_nube.md>) | `69138b3c1627157e8c4d2706584e630f544e18344ceb4e0963b6623b4e9eb5fb` |
| [MD_4.2_2.3/partes/02_c_conexiones.md](<MD_4.2_2.3/partes/02_c_conexiones.md>) | `521613a22292f799c6efd28080096fd94c0f71fa7b92092fa8d376ffe6c37f5c` |
| [MD_4.2_2.3/partes/04_c_implementos.md](<MD_4.2_2.3/partes/04_c_implementos.md>) | `3b8c14535f9cf4b58a560526f8f8419978ce5f54039fc34ae028f366ec40b981` |
| [MD_4.2_2.3/partes/05_d_sitio_principal.md](<MD_4.2_2.3/partes/05_d_sitio_principal.md>) | `4c00c536129ad7dadf3e6190655d0e3883c58dbb3611464be33337d75a28ad39` |
| [MD_4.2_2.3/partes/06_e_sitio_secundario.md](<MD_4.2_2.3/partes/06_e_sitio_secundario.md>) | `dcaa496a22e59694bda76cf2cb44ad50520a6b62aa376727dd15ebfe201f8996` |
| [MD_4.2_2.3/partes/11_j_despliegue.md](<MD_4.2_2.3/partes/11_j_despliegue.md>) | `edee691da5885790d52b7c79457c80d4427ad1dd682f18572ab66d3271e2eadd` |
| [MD_4.2_2.3/partes/12_k_dimensionamiento.md](<MD_4.2_2.3/partes/12_k_dimensionamiento.md>) | `62444b97cdaa9c8540996b66a7bec4b567c33191f5e3d799a4ede6437fa5e478` |
| [MD_4.2_2.3/partes/14_m_decisiones_adr.md](<MD_4.2_2.3/partes/14_m_decisiones_adr.md>) | `76a4e47d350da74ba418a3c1ae90c39dd5f2644102a9616eb2e039039e4b8680` |
| [MD_4.2_2.3/partes/15_anexo_t11.md](<MD_4.2_2.3/partes/15_anexo_t11.md>) | `a2fea0ae3cb11ffd5cab0d279c0385ebd18b9e47501f2a53fc34a13a3d755525` |
| [MD_4.2_2.3/partes/16_anexo_4b_memoria_calculo.md](<MD_4.2_2.3/partes/16_anexo_4b_memoria_calculo.md>) | `dd9def8a4683bffb3b8c5a71b0b1ca9b10f5a4dc00b01830453bc5a7b159a7de` |
| [MD_4.2_2.3/partes/17_referencias.md](<MD_4.2_2.3/partes/17_referencias.md>) | `9c65c190e0ded1abf647ac1345c3ad1853950aa17ab739e4839f87a082ee6b09` |
| [anexos_cierre/16_referencias.md](<anexos_cierre/16_referencias.md>) | `006ca86fb7d8958209f56f405a06f770c5f2f393f67437401a82bf90f5d07c1c` |
| [anexos_cierre/17_declaracion_de_uso_de_ia.md](<anexos_cierre/17_declaracion_de_uso_de_ia.md>) | `52ac0feca70d74c0ed2a5e71d375b2af0d21216cb56d38d665894677544fc2c7` |
| [logica 4.1/LAFROX-Subdocumento4.1-Anexos.md](<logica 4.1/LAFROX-Subdocumento4.1-Anexos.md>) | `ad3c824c3b03e9e3d4f34b0e587f267c5e38150417e39308f71b3877dcee69b4` |
| [logica 4.1/LAFROX-Subdocumento4.1.md](<logica 4.1/LAFROX-Subdocumento4.1.md>) | `3121e8c33035c1d4f49b9c0bbaebd42f6c874947b2f335af592d20da729cec58` |
| [partes_cierre/declaracion_de_uso_de_ia.md](<partes_cierre/declaracion_de_uso_de_ia.md>) | `1cc629c028f0d41f9eae2aeac40709d5c7db22823bbfe59058051b549971abfa` |
| [partes_cierre/referencias.md](<partes_cierre/referencias.md>) | `d3d3bdb290d618c91aa521d7615d8662fbaf724a0356f08fe905294d1ae1226f` |

## Validación final

Se comprobaron 579 enlaces locales y 808 anclas explícitas en 32 archivos Markdown del capítulo. [Resultados y límites](VERIFICACION_ALINEACION.md).

## Complemento posterior de diseño

La mejora autorizada de SD5 del 3 de octubre de 2026 añade [CD-05](COMPLEMENTO_COORDINACION_DATOS_SD5.md), separado de la conversión fiel. Precisa autoridad, transporte y aceptación de reservas; no cambia el commit de procedencia ni afirma que las cifras originales incorporen ese nuevo intercambio.
