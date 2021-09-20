from flask import Flask
from flask import request
import requests
import json

from weather_aggregator.weather_statistics import get_api_url, get_api_key, get_today_date, get_n_date, \
    get_final_result, process_response_data, statistics
weather_aggregator = Flask(__name__)


@weather_aggregator.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    city = "".join(c for c in city if c.isalpha())
    days = request.args.get('days')
    days = "".join(c for c in days if c.isdecimal())
    today = get_today_date()
    first_day = get_n_date(today, int(days))
    last_day = get_n_date(today, 1)
    request_params = {"unitGroup": "metric", "key": get_api_key()}
    response = requests.get(get_api_url() + city + '/' + str(first_day) + '/' + str(last_day), params=request_params)
    res_json = response.json()
    parameters = res_json['days']
    data = process_response_data(parameters)
    weather_statistics = statistics(data)
    final_result = get_final_result(city, first_day, today, weather_statistics)
    return json.dumps(final_result, indent=2, separators=(',', ': '))


if __name__ == '__main__':
    weather_aggregator.run()
