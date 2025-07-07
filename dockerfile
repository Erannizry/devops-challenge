FROM python:3.13.5-slim

WORKDIR /docker-challenge

# Copy and install dependencies
COPY requirements/base.txt /docker-challenge/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY /app /docker-challenge/app

EXPOSE 5000

# Run the Flask app
CMD ["flask", "--app", "app", "run", "--host", "0.0.0.0"]
