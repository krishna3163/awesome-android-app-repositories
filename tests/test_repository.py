"""Unit tests for JSON database repository CRUD."""

from pathlib import Path

from src.config import FailedPost, PendingFeature, Project, ReviewMatch
from src.database import repository


def test_repository_crud(tmp_path: Path, monkeypatch, sample_project: Project):
    # Redirect DATA_DIR and DB paths to temporary folder
    test_data_dir = tmp_path / "data"
    monkeypatch.setattr(repository, "DATA_DIR", test_data_dir)
    monkeypatch.setattr(repository, "APPS_DB", test_data_dir / "apps.json")
    monkeypatch.setattr(repository, "PENDING_DB", test_data_dir / "pending-features.json")
    monkeypatch.setattr(repository, "REVIEW_DB", test_data_dir / "review-required.json")
    monkeypatch.setattr(repository, "FAILED_DB", test_data_dir / "failed-posts.json")
    monkeypatch.setattr(repository, "PROCESSED_DB", test_data_dir / "processed-messages.json")

    # 1. Apps DB
    assert repository.load_apps() == []
    repository.save_apps([sample_project])
    loaded_apps = repository.load_apps()
    assert len(loaded_apps) == 1
    assert loaded_apps[0].id == sample_project.id

    # 2. Pending features DB
    assert repository.load_pending_features() == []
    pending = PendingFeature(raw_title="Features of App", normalized_title="app")
    repository.save_pending_features([pending])
    loaded_pending = repository.load_pending_features()
    assert len(loaded_pending) == 1
    assert loaded_pending[0].raw_title == "Features of App"

    # 3. Review required DB
    assert repository.load_review_required() == []
    review = ReviewMatch(incoming_name="Test", matched_project_id="test-id", similarity_score=80.0)
    repository.save_review_required([review])
    loaded_reviews = repository.load_review_required()
    assert len(loaded_reviews) == 1
    assert loaded_reviews[0].matched_project_id == "test-id"

    # 4. Failed posts DB
    assert repository.load_failed_posts() == []
    failed = FailedPost(channel="@test", message_id=123, error="Test error")
    repository.save_failed_posts([failed])
    loaded_failed = repository.load_failed_posts()
    assert len(loaded_failed) == 1
    assert loaded_failed[0].message_id == 123

    # 5. Processed messages tracker
    assert repository.load_processed_messages() == {}
    repository.save_processed_messages({"popMODS": 100, "popCLOUDS": 200})
    loaded_processed = repository.load_processed_messages()
    assert loaded_processed == {"popMODS": 100, "popCLOUDS": 200}
