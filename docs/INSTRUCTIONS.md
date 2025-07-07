# INSTRUCTIONS.md

## Prerequisites

- Python
- pip
- Git
- Local Docker Installation


## 1. Clone the Repository

```
git clone https://github.com/Erannizry/devops-challenge.git
cd devops-challenge
```

## 2. Set Up Python Environment (Optional)

It is recommended to use a virtual environment:

```
python -m venv venv

venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

## 3. Install Dependencies

Install the required packages:

```
pip install -r requirements/base.txt
```

For testing dependencies:
```
pip install -r requirements/test-requirements.txt
```

## 4. Set Up Environment Variables

Before running the application, create a `.env` file in the project app directory. This file should contain the necessary environment variables, for example:

```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
DYNAMODB_TABLE=your_table_name
CODE_NAME=your_code_name
```

Adjust the values as needed for your environment.

## 5. Running the Application

You can run the application using Flask (Run in root directory)

```
flask --app app run --host 0.0.0.0
```

## Available Routes

| Route     | Method | Description |
|-----------|:------:|-------------|
| `/health` | GET    | Health check endpoint. Returns project status and metadata. |
| `/secret` | GET    | Retrieves a secret code from DynamoDB. Requires proper environment configuration. |


## 6. Running Tests

To run the test suite:

```
pytest
```

## 7. Using Docker

To build and run the application using Docker:

```
docker build -t <image-name> .
docker run -p 5000:5000 <image-name>
```
Replace <image-name> with your desired image tag.

Or with Docker Compose:

```
docker compose up --build
```

## 8. Verification

To verify the setup, you can run the provided script:

```
sh verification.sh
```
