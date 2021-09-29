from datetime import date, timedelta
from typing import List

import numpy as np
from url import url


def get_today_date() -> date:
    return date.today()


def get_n_date(now_date: date, days: int) -> date:
    return now_date - timedelta(days)


def get_api_url() -> str:
    return url['api_url']


def process_response_data(response: dict) -> dict:
    new_data: dict = {'temperature': [], 'humidity': [], 'pressure': []}
    for day in response:
        new_data['temperature'].append(day['temp'])
        new_data['humidity'].append(day['humidity'])
        new_data['pressure'].append(day['pressure'])
    return new_data


def statistics(data: dict) -> List[dict]:
    weather_stats = list()
    specifications: list = [dict(), dict(), dict()]
    for key, value in data.items():
        for spec in specifications:
            spec['average'] = round(np.average(data[key]), 1)
            spec['median'] = np.median(data[key])
            spec['min'] = np.min(data[key])
            spec['max'] = np.max(data[key])
        weather_stats.append(spec)
    return weather_stats


def get_final_result(city: str, first_day: date, last_day: date, stats_data: list) -> dict:
    stats = dict()
    counter = 0
    stats_names = ['temperature_c', 'humidity', 'pressure_mb']
    stats['city'] = city
    stats['from'] = str(first_day)
    stats['to'] = str(last_day)
    for name in stats_names:
        stats[name] = stats_data[counter]
        counter += 1
    return stats
