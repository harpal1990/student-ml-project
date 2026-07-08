from pathlib import Path
import yaml

def load_config():
    # Project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # config/config.yaml
    config_path = BASE_DIR / "config" / "config.yaml"

    with open(config_path, "r") as file:
        return yaml.safe_load(file)