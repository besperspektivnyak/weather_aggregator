# Weather aggregator
## About
This service can gives you information about the weather in any city for several last days. Information includes 
- average
- median
- minimum
- maximum 

of such parameters as
- temperature (°C)
- humidity (%)
- pressure (mb)
## Installation
Install all packages from requirements.txt.

``pip install -r requirements.txt``

Get your own API key on [Visual Crossing](https://www.visualcrossing.com/). Then paste it in config.py instead of phrase 'Your api key'.

## Using
The service receives GET requests 

``/weather?city=<city>&days=<n>``

The main app is weather_aggregation/app.py.

To run app in terminal:

``> cd weather_aggregator``

``> flask run``

## Docker
To run app from docker file you can build docker image by command 

``docker built -t weather '[full path to Dockerfile]'``

or 

you can pull image from Docker Hub

``docker pull besperspektivnyak/weather``

To build container 

``docker run -p 8080:8080 --name weather 'besperspektivnyak/weather or weather'``

the last argument is the name of your image, choose it based on the way you build image.

The service launch on [http://localhost:8080/](http://localhost:8080/). 