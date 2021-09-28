FROM python:latest
MAINTAINER Elizaveta Grishina
RUN apt-get update -y && apt-get install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH /app
ENV PATH=$PATH:/app
EXPOSE 8080
CMD ["python3", "weather_aggregator/app.py"]