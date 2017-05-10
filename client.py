import requests

class ImpostometroClient:

    def get_state_counter(self, state, start_date, end_date):
        url = "https://impostometro.com.br/Contador/Estado?estado={0}s&dataInicial={1}&dataFinal={2}".format(state, start_date, end_date)
        headers = {'Accept-Encoding': 'gzip, deflate, sdch, br',
                   'X-Requested-With': 'XMLHttpRequest'}
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            counter = result.content
        else:
            couter = '{}'
        return counter

    def get_city_counter(self, state, city, start_date, end_date):
        url = "https://impostometro.com.br/Contador/Municipios?estado={0}s&municipio={1}&dataInicial={2}&dataFinal={3}".format(state, city, start_date, end_date)
        headers = {'Accept-Encoding': 'gzip, deflate, sdch, br',
                   'X-Requested-With': 'XMLHttpRequest'}
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            counter = result.content
        else:
            couter = '{}'
        return counter


import unittest
class ImpostometroClientTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = ImpostometroClient()

    def test_get_state_counter(self):
        state = "sc"
        start_date = "01/01/2017"
        end_date = "09/05/2017"
        result = self.client.get_state_counter(state, start_date, end_date)
        print result

    def test_get_state_counter(self):
        state = "sc"
        city = "florianopolis"
        start_date = "01/01/2017"
        end_date = "09/05/2017"
        result = self.client.get_city_counter(state, city, start_date, end_date)
        print result