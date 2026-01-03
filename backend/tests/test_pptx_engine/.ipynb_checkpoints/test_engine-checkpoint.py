"""
PPTX Engine Unit Tests
"""

import pytest
import os
import tempfile
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.schemas.slide_schema import (
    SlidedeckSchema,
    validate_slide_json,
    create_example_slidedeck,
)
from app.services.pptx_engine import (
    PPTXEngine,
    generate_pptx,
    TextOverflowEngine,
    BoundingBox,
    COLOR_SCHEMES,
)


@pytest.fixture
def sample_slidedeck():
    return {
        "metadata": {
            "title": "Test Presentation",
            "theme": "corporate_blue",
            "language": "en"
        },
        "slides": [
            {
                "slide_type": "title",
                "title": "Test Title Slide",
                "subtitle": "Test Subtitle"
            },
            {
                "slide_type": "content",
                "title": "Test Content",
                "body_points": [
                    {"text": "First point", "level": 0},
                    {"text": "Second point", "level": 0}
                ]
            }
        ]
    }


@pytest.fixture
def temp_output_path():
    with tempfile.NamedTemporaryFile(suffix='.pptx', delete=False) as f:
        yield f.name
    if os.path.exists(f.name):
        os.remove(f.name)


class TestSlideSchema:
    def test_valid_slidedeck(self, sample_slidedeck):
        slidedeck = validate_slide_json(sample_slidedeck)
        assert slidedeck.metadata.title == "Test Presentation"
        assert len(slidedeck.slides) == 2
    
    def test_example_slidedeck(self):
        example = create_example_slidedeck()
        slidedeck = validate_slide_json(example)
        assert slidedeck.metadata.theme.value == "corporate_blue"


class TestOverflowEngine:
    def test_direct_fit(self):
        engine = TextOverflowEngine()
        box = BoundingBox(0, 0, 5.0, 2.0)
        result = engine.fit_text("Short text", box, 18.0)
        assert result['strategy'] == 'direct_fit'
    
    def test_empty_text(self):
        engine = TextOverflowEngine()
        box = BoundingBox(0, 0, 5.0, 2.0)
        result = engine.fit_text("", box, 18.0)
        assert result['strategy'] == 'empty'


class TestPPTXEngine:
    def test_generate_success(self, sample_slidedeck, temp_output_path):
        engine = PPTXEngine(theme="corporate_blue")
        result = engine.generate(sample_slidedeck, temp_output_path)
        assert result['success'] is True
        assert result['num_slides'] == 2
        assert os.path.exists(temp_output_path)
    
    def test_available_themes(self):
        themes = PPTXEngine.get_available_themes()
        assert 'corporate_blue' in themes
        assert len(themes) >= 5


class TestIntegration:
    def test_full_workflow(self, temp_output_path):
        slidedeck = create_example_slidedeck()
        validated = validate_slide_json(slidedeck)
        result = generate_pptx(validated.model_dump(), temp_output_path, theme="modern_green")
        assert result['success'] is True
        assert result['metrics']['lqs'] > 0.7


if __name__ == "__main__":
    pytest.main([__file__, "-v"])