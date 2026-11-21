// Ships a deterministic passport spread: the committed entry.png is copied verbatim.
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL(".", import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const destination = join(outDir, "entry.png");
copyFileSync(join(root, "entry.png"), destination);
console.error(`Deterministic passport spread written to ${destination}`);
