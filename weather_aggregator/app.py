import os
import json
import requests
from flask import Flask
from flask import request

from weather_aggregator.weather_statistics import *

api_key = os.environ['API_KEY']
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "You in weather aggregator app!"


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    city = "".join(c for c in city if c.isalpha())
    days = request.args.get('days')
    days = "".join(c for c in days if c.isdecimal())
    today = get_today_date()
    first_day = get_n_date(today, int(days))
    last_day = get_n_date(today, 1)
    request_params = {"unitGroup": "metric", "key": api_key}
    response = requests.get(get_api_url() + city + '/' + str(first_day) + '/' + str(last_day), params=request_params)
    res_json = response.json()
    parameters = res_json['days']
    data = process_response_data(parameters)
    weather_statistics = statistics(data)
    final_result = get_final_result(city, first_day, today, weather_statistics)
    return json.dumps(final_result, indent=2, separators=(',', ': '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
