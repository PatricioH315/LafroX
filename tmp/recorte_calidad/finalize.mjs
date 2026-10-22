import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const skill='C:/Users/henri/.codex/plugins/cache/openai-primary-runtime/presentations/26.1020.11127/skills/presentations';
const {finalizePresentation}=await import(pathToFileURL(skill+'/container_tools/artifact_tool_utils.mjs').href);
const report=JSON.parse(await fs.readFile(root+'/tmp/recorte_calidad/report.json','utf8'));
const result=await finalizePresentation({workspaceDir:root,
candidatePath:root+'/tmp/recorte_calidad/candidate.pptx',
finalPath:root+'/Presentaciones/Actualizada/LafroX - Informe 2 - plan de calidad resumido.pptx',
pythonExecutable:'C:/Users/henri/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
integrityValidatorPath:skill+'/container_tools/inspect_presentation_package_integrity.py',
layoutValidatorPath:skill+'/container_tools/inspect_presentation_layout_geometry.py',
layoutArgs:['--expected-slide-size-emu','18288000,10287000'],explicitTotalSlideCount:50,
fontPolicy:{basis:'reference',families:report.fonts,referencePath:report.source,referenceSha256:report.source_sha256},
// This existing native deck is validated in PowerPoint; the bundled WASM
// importer previously crashes and must not be used to reserialize Morph.
verifyArtifactToolImport:false,receiptPath:root+'/tmp/recorte_calidad/validation.json'});
console.log(JSON.stringify(result,null,2));
