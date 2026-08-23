"""Unit tests for language detection and translation utility."""

from src.utils.translator import contains_foreign_script, translate_to_english


def test_contains_foreign_script():
    # English/ASCII text
    assert contains_foreign_script("Awesome Android App") is False
    assert contains_foreign_script("Python 3.12 Developer Tool") is False

    # Foreign scripts
    assert contains_foreign_script("Отличный инструмент для разработчиков") is True
    assert contains_foreign_script("开源安卓项目") is True
    assert contains_foreign_script("یک ابزار عالی برای توسعه دهندگان") is True


def test_translate_english_noop():
    english_text = "A modern lightweight Android music player."
    assert translate_to_english(english_text) == english_text


def test_translate_empty_text():
    assert translate_to_english("") == ""
    assert translate_to_english("   ") == "   "
