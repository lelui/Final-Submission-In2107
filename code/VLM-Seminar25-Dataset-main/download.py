from huggingface_hub import snapshot_download
from pathlib import Path

mistral_models_path = Path.home().joinpath('mistral_models', 'Pixtral')
mistral_models_path.mkdir(parents=True, exist_ok=True)

snapshot_download(repo_id="mistralai/Pixtral-12B-2409", allow_patterns=["params.json", "tekken.json"], local_dir=mistral_models_path)