import json
import requests
import time
from config.ConfReader import conf


class FECScraper:
    FEC_KEY = conf.FEC_API_KEY
    DELAY_INTERVAL = 1.5
    MAX_MISSES = 5
    PAGE_INTERVAL = 20

    @staticmethod
    def get_all_candidates():
        header = {'X-API-Key': conf.FEC_API_KEY}
        res = requests.get('https://api.open.fec.gov/v1/candidates/?api_key=6eWjIoZfjPJ0HgM5M8HKst7GcwRmt7587hPx5Odl',
                           headers=header)
        data = res.json()
        print(data)

    @staticmethod
    def get_candidate(candidate_id):
        header = {'X-API-Key': conf.FEC_API_KEY}
        res = requests.get('https://api.open.fec.gov/v1/candidate/' + str(candidate_id)
                           + '/?api_key=6eWjIoZfjPJ0HgM5M8HKst7GcwRmt7587hPx5Odl',
                           headers=header)
        data = res.json()
        print(data)


FECScraper.get_candidate("P40002172")
