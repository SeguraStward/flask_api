# Random Users Flask API

A Flask-based REST API that generates 75 random users using the **RandomUser.me** API service. The API responds with a list of users in JSON format.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.0-green.svg)

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
    - [Install Python](#1-install-python)
    - [Clone the Repository](#2-clone-the-repository)
    - [Create a Virtual Environment](#3-create-a-virtual-environment)
    - [Install Dependencies](#4-install-dependencies)
4. [Project Structure](#project-structure)
5. [API Documentation](#api-documentation)
    - [Endpoints](#endpoints)
    - [Error Handling](#error-handling)
6. [Running the API](#running-the-api)
7. [Testing](#testing)
    - [Running Tests](#running-tests)
    - [Test Structure](#test-structure)
8. [Configuration](#configuration)
9. [Deployment](#deployment)
10. [Contributing](#contributing)

## Features

- Fetches 75 randomly generated user profiles
- Returns clean JSON data
- CORS enabled for cross-origin requests
- Simple and lightweight implementation
- Comprehensive error handling
- Unit tests for API endpoints

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

## Project Structure

```txt
flask_api/
├── app/
│   ├── __init__.py          # Flask application factory
│   ├── routes.py            # API routes definitions
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py  # Service to fetch users from external API
│   └── utils/
│       ├── __init__.py
│       └── errors.py        # Custom error classes
├── tests/
│   ├── __init__.py
│   ├── test_routes.py       # Tests for API routes
│   └── test_user_service.py # Tests for user service
├── app.py                   # Application entry point
├── config.py                # Configuration settings
└── requirements.txt         # Project dependencies
```

## API Documentation

### Endpoints

1. **Home Endpoint**
   - **URL**: `/api/`
   - **Method**: `GET`
   - **Description**: Returns basic API information and available endpoints
   - **Response Format**:

     ```json
     {
       "message": "Flask API for Random Users",
       "endpoints": {
         "users": "/api/users"
       }
     }
     ```

2. **Users Endpoint**
   - **URL**: `/api/users`
   - **Method**: `GET`
   - **Description**: Returns 75 randomly generated user profiles
   - **Response**: JSON array of user objects
   - **Error Codes**:
     - `503`: External API service unavailable
     - `500`: Internal server error

### Error Handling

All API errors return JSON responses with the following format:

```json
{
  "error": "Error message description"
}
```

## Running the API

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. The API will be available at: `http://localhost:5000/api/users`

## Testing

The project includes comprehensive unit tests for both API routes and services:

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_routes.py
```

### Test Structure

- test_routes.py: Tests for API endpoints including success and error scenarios
- test_user_service.py: Tests for the UserService class that handles external API interactions

## Configuration

Configuration is handled through the config.py file, which includes:

- `DEBUG`: Controls debug mode (default: True)
- `RANDOM_USER_API_URL`: External API endpoint (default: "<https://randomuser.me/api/>")
- `USERS_TO_RETURN`: Number of users to fetch (default: 75)

## Deployment

For production deployment:

1. Set `DEBUG = False` in config.py
2. Deploy using WSGI server like Gunicorn:

   ```bash
   pip install gunicorn
   gunicorn -w 4 "app:create_app()"
   ```

3. Consider using a reverse proxy like Nginx for production environments
