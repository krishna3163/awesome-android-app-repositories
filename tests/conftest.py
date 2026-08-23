"""Shared test fixtures and sample data."""

import pytest

from src.config import Developer, Feature, ImageSet, Project, TelegramSource


@pytest.fixture
def sample_main_channel_post() -> str:
    return (
        "Neuronpedia\n\n"
        "Neuronpedia is an open-source AI interpretability platform for exploring and "
        "understanding what happens inside neural networks and LLMs. It enables researchers "
        "to inspect model features, neuron activations, circuits, and internal representations, "
        "making complex model behavior more transparent and easier to understand. It also "
        "provides tools for investigating and steering model behavior.\n\n"
        "🔗 Links:\n\n"
        "- Website\n"
        "- Features\n"
        "- Source code\n\n"
        "Developer: Johnny Lin\n\n"
        "❤️ Support the Project\n\n"
        "If this project makes your life easier, here are a few quick ways to show some love:\n\n"
        "⭐ Star the repo/app\n"
        "☕ Buy a coffee for the developer\n"
        "🛠 Contribute code, issues, or pull-requests\n\n"
        "🏷 Tags:\n\n"
        "#Website\n"
        "#AI\n"
        "#Learning"
    )


@pytest.fixture
def sample_main_channel_entities(sample_main_channel_post: str) -> list[dict]:
    text = sample_main_channel_post
    entities = []

    # Find offsets for hyperlinks
    website_idx = text.find("Website")
    if website_idx != -1:
        entities.append({
            "offset": website_idx,
            "length": len("Website"),
            "url": "https://neuronpedia.org/",
        })

    features_idx = text.find("Features")
    if features_idx != -1:
        entities.append({
            "offset": features_idx,
            "length": len("Features"),
            "url": "https://t.me/popCLOUDS/13548",
        })

    source_idx = text.find("Source code")
    if source_idx != -1:
        entities.append({
            "offset": source_idx,
            "length": len("Source code"),
            "url": "https://github.com/hijohnnylin/neuronpedia",
        })

    dev_idx = text.find("Johnny Lin")
    if dev_idx != -1:
        entities.append({
            "offset": dev_idx,
            "length": len("Johnny Lin"),
            "url": "https://github.com/hijohnnylin",
        })

    return entities


@pytest.fixture
def sample_features_channel_post() -> str:
    return (
        "Features of Neuron Pedia:\n\n"
        "• 🧠 Feature/latent exploration — inspect individual model features and activations\n\n"
        "• 🔍 Semantic search — search millions of latents/features by meaning\n\n"
        "• 📊 Activation analysis — view top activations, logits, and activation density\n\n"
        "• 🎛️ Model steering — modify model behavior using latents or custom vectors\n\n"
        "• 🕸️ Circuit Tracer/graphs — visualize relationships between model components\n\n"
        "• 🤖 Auto-interpretability — automatically generate and score feature explanations\n\n"
        "• 🔬 SAE support — work with Sparse Autoencoders and their features\n\n"
        "• 👁️ Probes, concepts & transcoders — support advanced interpretability research\n\n"
        "• 🧪 Inference testing — run prompts and examine internal model behavior\n\n"
        "• 📈 Dashboards & UMAP — visualize features and embeddings\n\n"
        "• 🔌 API + Python/TypeScript libraries — access functionality programmatically\n\n"
        "• 💾 Import/export & datasets — work with interpretability datasets\n\n"
        "• 🏠 Self-hosting — run the open-source platform locally or in the cloud"
    )


@pytest.fixture
def sample_project() -> Project:
    return Project(
        id="neuronpedia",
        name="Neuronpedia",
        description=(
            "Neuronpedia is an open-source AI interpretability platform for exploring and "
            "understanding what happens inside neural networks and LLMs."
        ),
        website="https://neuronpedia.org",
        repository="https://github.com/hijohnnylin/neuronpedia",
        developer=Developer(
            name="Johnny Lin",
            url="https://github.com/hijohnnylin",
        ),
        features=[
            Feature(
                title="Feature/latent exploration",
                description="Inspect individual model features and activations",
            ),
            Feature(
                title="Semantic search",
                description="Search millions of latents/features by meaning",
            ),
        ],
        tags=["Website", "AI", "Learning"],
        images=ImageSet(
            cover="assets/apps/neuronpedia/cover.jpg",
            screenshots=["assets/apps/neuronpedia/screenshot-1.jpg"],
        ),
        telegram=TelegramSource(
            main_channel="@popMODS",
            main_message_id=12345,
            features_channel="@popCLOUDS",
            features_message_id=13548,
        ),
        status="active",
        created_at="2026-08-22T00:00:00Z",
        updated_at="2026-08-22T00:00:00Z",
    )
