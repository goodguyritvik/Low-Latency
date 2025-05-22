# Edge Task Scheduler

An intelligent scheduling system that determines whether to process tasks locally or offload them to cloud resources using machine learning.

## Features

- Machine learning-based decision making
- Real-time task evaluation
- Docker container support
- Customizable decision thresholds

## Prerequisites

- Docker Desktop
- WSL 2 (Windows only)
- Python 3.9+

## Installation

1. Clone this repository
2. Set up the environment:

```bash
# Build Docker image
docker build -t edge-scheduler .

# Alternatively for local development
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

## Usage

### Docker
```bash
docker run -it --rm edge-scheduler
```

### Local Development
```bash
python scheduler.py
```

### Testing Components
```bash
# Test predictions
python predict.py

# Generate test data
python datacreation.py
```

## Project Structure

```
.
├── Dockerfile              # Primary container configuration
├── Dockerfile_v2           # Alternative container config
├── requirements.txt        # Python dependencies
├── scheduler.py            # Main scheduling logic
├── predict.py              # Prediction module
├── model_updated.py        # Trained ML model
├── datacreation.py         # Test data generator
└── random_test.py          # Test scripts
```

## Configuration

Modify these files for customization:
- `scheduler.py`: Adjust task processing logic
- `predict.py`: Change prediction thresholds
- `requirements.txt`: Update dependencies

## Troubleshooting

**Docker Issues:**
```bash
wsl --shutdown
# Restart Docker Desktop
```

**Python Issues:**
```bash
pip install --upgrade -r requirements.txt
```

## License

[MIT License](LICENSE)
