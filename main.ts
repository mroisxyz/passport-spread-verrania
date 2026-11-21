// Entry point: copy the committed passport spread into /output/entry.png.
// The image is drawn deterministically by make_passport.py and shipped with the repo.
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const here = fileURLToPath(new URL(".", import.meta.url));
const out = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(out, { recursive: true });
copyFileSync(join(here, "entry.png"), join(out, "entry.png"));
console.error("passport spread written to", join(out, "entry.png"));
