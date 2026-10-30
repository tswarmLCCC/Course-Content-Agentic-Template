"""
Utility to resolve the configurable directory path for raw Intel course materials.
Reads from (in priority order):
1. Environment variable INTEL_MATERIALS_PATH
2. courses/aiml-2050-ai-in-the-workforce/local_config.json
3. Fallback: courses/aiml-2050-ai-in-the-workforce/intake/intel_slide_decks/
"""
import os
import json
from pathlib import Path

COURSE_DIR = Path(__file__).resolve().parent.parent

def get_intel_materials_path() -> Path:
    env_path = os.environ.get("INTEL_MATERIALS_PATH")
    if env_path and os.path.exists(env_path):
        return Path(env_path)

    local_config_file = COURSE_DIR / "local_config.json"
    if local_config_file.exists():
        try:
            with open(local_config_file, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                configured_path = cfg.get("intel_materials_path")
                if configured_path and os.path.exists(configured_path):
                    return Path(configured_path)
                elif configured_path:
                    print(f"[Warning] Configured path does not exist: {configured_path}")
        except Exception as e:
            print(f"[Warning] Error reading local_config.json: {e}")

    # Fallback to local intake folder
    fallback = COURSE_DIR / "intake" / "intel_slide_decks"
    return fallback

if __name__ == "__main__":
    path = get_intel_materials_path()
    print(f"Resolved Intel materials path: {path}")
    print(f"Directory exists: {path.exists()}")
    if path.exists():
        files = list(path.glob("*"))
        print(f"Found {len(files)} items in directory.")
