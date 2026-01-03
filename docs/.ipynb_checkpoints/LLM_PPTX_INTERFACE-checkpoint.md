# LLM Engineer - PPTX Engineer Interface Documentation

## Data Flow
```
LLM Engineer                    PPTX Engineer
     |                               |
     |   SlidedeckSchema (JSON)      |
     | ----------------------------->|
     |                               |
     |         .pptx file            |
     | <-----------------------------|
```

## JSON Schema

### Complete Example
```json
{
  "metadata": {
    "title": "Presentation Title",
    "author": "Author Name",
    "theme": "corporate_blue",
    "language": "en",
    "aspect_ratio": "16:9"
  },
  "slides": [
    {
      "slide_type": "title",
      "title": "Welcome Title",
      "subtitle": "Subtitle"
    },
    {
      "slide_type": "content",
      "title": "Content Page Title",
      "body_points": [
        {"text": "Point 1", "level": 0, "priority": "high"},
        {"text": "Sub point", "level": 1, "priority": "normal"},
        {"text": "Point 2", "level": 0, "priority": "normal"}
      ],
      "speaker_notes": "Speaker notes here..."
    },
    {
      "slide_type": "closing",
      "title": "Thank You",
      "subtitle": "Q&A"
    }
  ]
}
```

## Field Reference

### metadata (required)

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| title | string | Yes | - | Presentation title |
| author | string | No | null | Author |
| theme | enum | No | corporate_blue | Color theme |
| language | string | No | en | Language code |
| aspect_ratio | enum | No | 16:9 | Aspect ratio |

### slide_type (required)

| Value | Description | Use Case |
|-------|-------------|----------|
| title | Title slide | Opening |
| content | Content slide | Main content |
| section | Section divider | Chapter breaks |
| two_column | Two column layout | Comparisons |
| closing | Closing slide | Thank you/Q&A |

### body_points

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| text | string | Yes | Point text |
| level | int | No | Indent level (0-2) |
| priority | enum | No | Priority level |

## Length Guidelines

| Element | Maximum | Recommended |
|---------|---------|-------------|
| title | 200 chars | **50 chars** |
| subtitle | 300 chars | **80 chars** |
| body_point.text | 500 chars | **80-100 chars** |
| speaker_notes | 2000 chars | **500 chars** |
| slides count | 50 | **10-15** |
| body_points/slide | 10 | **4-6** |

**Important**: Exceeding recommended lengths triggers overflow handling (font reduction or truncation)

## Validation
```python
from app.schemas import validate_slide_json

try:
    validated = validate_slide_json(your_json)
    print("Validation passed!")
except ValidationError as e:
    print(f"Validation failed: {e}")
```

## Common Errors

1. **Missing title slide**
   - Error: `Must have at least one title slide`
   - Fix: Ensure at least one slide has `slide_type: "title"`

2. **Too many body_points**
   - Error: `Too many body points (max 10)`
   - Fix: Maximum 10 per slide, recommend 4-6
```

4. 按 `Command + S` 保存

---

### 步骤 7：编辑 `requirements.txt`

1. 回到项目根目录（`slidegen` 文件夹）
2. 点击 `requirements.txt` 文件
3. 粘贴以下内容：
```
# PPTX Engine Dependencies
python-pptx>=0.6.21
pydantic>=2.0.0

# Testing
pytest>=7.0.0
pytest-cov>=4.0.0