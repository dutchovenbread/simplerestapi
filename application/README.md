# Simple REST API Application

A minimal Python-based REST API application that runs on EC2.

## Features

- Built using Python's built-in `http.server` module
- No external dependencies required
- Provides health check endpoint
- JSON responses
- Request logging

## Endpoints

- `GET /` - API status and available endpoints
- `GET /health` - Health check endpoint

## Running Locally

```bash
python3 app.py
```

The server will start on `http://0.0.0.0:8080`

## Testing

Test the API locally:

```bash
# Get API status
curl http://localhost:8080/

# Health check
curl http://localhost:8080/health
```

## Deployment

The application is automatically deployed to EC2 by the GitHub Actions workflow when code is pushed to the main branch.
