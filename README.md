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
