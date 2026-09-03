/**
 * Plugin de opencode: refuerza la activación del skill orquestador
 * `licitacion-workflow` inyectando la instrucción en el prompt de sistema.
 *
 * Se referencia desde `opencode.jsonc` en `plugin`. Requiere opencode >= 1.0.137
 * y reiniciar opencode tras cualquier cambio de config.
 */
import type { Plugin } from "opencode";

const plugin: Plugin = async ({ config, project, client, prompt, messages, $ }) => {
  const workflowLoaded = messages.some(
    (m) => (m.content as string)?.includes("licitacion-workflow")
  );

  const oracle = await project.readFile(".opencode/skills/licitacion-workflow/SKILL.md");

  const reminder =
    `\n\n# SKILL ORQUESTADOR (inyectado por el plugin .opencode/plugins/activar-skills.ts)\n` +
    `El skill ${oracle && workflowLoaded ? "ya está cargado" : "debe cargarse"} ` +
    `para orquestar qué skill activar en cada fase de la propuesta. ` +
    `Ejecuta la herramienta \`skill\` con nombre \`licitacion-workflow\` al iniciar cualquier avance.\n`;

  if (workflowLoaded) {
    return;
  }

  await prompt(reminder);
};

export default plugin;
