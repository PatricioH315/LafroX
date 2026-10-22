import path from 'node:path';
import fs from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
const root = process.cwd();
const skill = 'C:/Users/henri/.codex/plugins/cache/openai-primary-runtime/presentations/26.1020.11127/skills/presentations';
const {finalizePresentation} = await import(pathToFileURL(path.join(skill, 'container_tools/artifact_tool_utils.mjs')));
const source = path.join(root, 'Presentaciones/Actualizada/LafroX - Informe 2 - calidad e innovaciones revisadas.pptx');
const candidate = path.join(root, 'Presentaciones/Actualizada/LafroX - Informe 2 - numeracion Gantt y EDT ajustadas.pptx');
const result = await finalizePresentation({
  workspaceDir: root,
  candidatePath: candidate,
  finalPath: path.join(root, 'tmp/ppt_edits/finalized.pptx'),
  pythonExecutable: 'C:/Users/henri/AppData/Local/Programs/Python/Python312/python.exe',
  integrityValidatorPath: path.join(skill, 'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath: path.join(skill, 'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs: ['--expected-slide-size-emu', '18288000,10287000'],
  explicitTotalSlideCount: 51,
  requiredNativeTableOwnerSlides: [],
  requiredNativeChartOwnerSlides: [],
  sourceTemplatePath: source,
  verifyArtifactToolImport: true,
  receiptPath: path.join(root, 'tmp/ppt_edits/finalizer-receipt.json'),
});
await fs.writeFile(path.join(root, 'tmp/ppt_edits/finalizer-result.json'), JSON.stringify(result, null, 2));
console.log(JSON.stringify(result));
