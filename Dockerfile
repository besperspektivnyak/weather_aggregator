FROM python:3.8.0

MAINTAINER Elizaveta Grishina

WORKDIR /app

RUN apt-get update -y && apt-get install -y python3-pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH /app
ENV PATH=$PATH:/app
CMD ["python3", "weather_aggregator/app.py"]