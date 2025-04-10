# Random Users Flask API

A Flask-based REST API that generates 75 random users using the **RandomUser.me** API service. The API responds with a list of users in JSON format.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)

## Features

- Fetches 75 randomly generated user profiles
- Returns clean JSON data
- CORS enabled for cross-origin requests
- Simple and lightweight implementation

## Prerequisites

Before getting started, make sure you have the following installed:

- **Python 3.6+**: Ensure you have a recent version of Python installed
- **Pip**: Python's package manager
- **Git**: (Optional) For cloning the repository

## Installation

### 1. Install Python

If you don't have Python installed:

- **Windows**:
  1. Visit the [official Python website](https://www.python.org/downloads/)
  2. Download the latest Python version for Windows
  3. During installation, check the option **"Add Python to PATH"**

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/flask_api.git
cd flask_api
```

### 3. Create a Virtual Environment

Isolate project dependencies with a virtual environment:

**Windows**:

```bash
py -3 -m venv .venv
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the API

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. The API will be available at: `http://localhost:5000/api/users`

### API Endpoints

- `GET /api/users`: Returns a list of 75 random user profiles
