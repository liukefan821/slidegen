# PPTX Engine Module Documentation

## Overview

PPTX Engine is the core rendering module of the intelligent slide generation system. It converts structured JSON data into professional PowerPoint files.

## Core Features

### 1. Text Overflow Handling

Four-strategy cascade pipeline ensures text never exceeds slide boundaries:

| Strategy | Description | Fidelity |
|----------|-------------|----------|
| Direct Fit | Text fits directly | 100% |
| Font Reduction | Reduce font size (min 12pt) | 100% |
| Smart Truncation | Truncate at sentence boundary | 30-70% |
| Force Truncate | Force truncation | Minimum |

### 2. Theme Colors

5 predefined themes:
- `corporate_blue` - Professional blue (default)
- `modern_green` - Fresh green
- `elegant_purple` - Elegant purple
- `warm_orange` - Warm orange
- `tech_dark` - Tech dark

### 3. Quality Metrics

Automatic quality evaluation:
- **TOR**: Text Overflow Rate (target < 5%)
- **SUR**: Space Utilization Rate (optimal 0.5-0.7)
- **VBS**: Visual Balance Score
- **LQS**: Layout Quality Score (target > 0.85)

## Quick Start
```python
from app.services.pptx_engine import generate_pptx

result = generate_pptx(
    slidedeck_json=your_json_data,
    output_path="output.pptx",
    theme="corporate_blue"
)

if result['success']:
    print(f"Success! LQS: {result['metrics']['lqs']:.2f}")
else:
    print(f"Failed: {result['error_message']}")
```

## API Reference

### generate_pptx()
```python
def generate_pptx(
    slidedeck_json: Dict,
    output_path: str,
    theme: str = "corporate_blue"
) -> Dict
```

**Parameters:**
- `slidedeck_json`: JSON data conforming to SlidedeckSchema
- `output_path`: Output file path
- `theme`: Theme name

**Returns:**
```python
{
    'success': True,
    'output_path': 'output.pptx',
    'num_slides': 5,
    'elapsed_time': 0.234,
    'metrics': {
        'tor': 0.0,
        'sur': 0.62,
        'vbs': 0.82,
        'lqs': 0.87
    },
    'warnings': []
}
```

## Dependencies
```
python-pptx>=0.6.21
pydantic>=2.0.0
```

## Interface with LLM Engineer

See [LLM_PPTX_INTERFACE.md](./LLM_PPTX_INTERFACE.md)