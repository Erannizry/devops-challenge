FROM python:3.13.5-slim

WORKDIR /docker-challenge

COPY requirements.txt /docker-challenge
RUN pip install --no-cache-dir -r requirements.txt

COPY /app /docker-challenge/app

EXPOSE 5000

CMD ["flask", "--app", "app", "run", "--host", "0.0.0.0"]
