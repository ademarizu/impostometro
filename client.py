import requests

class ImpostometroClient:

    def get_counter(self, state, start_date, end_date):
        url = "https://impostometro.com.br/Contador/Estado?estado={0}s&dataInicial={1}&dataFinal={2}".format(state, start_date, end_date)
        headers = {'Accept-Encoding': 'gzip, deflate, sdch, br',
                   # 'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4',
                   # 'Accept': '*/*',
                   # 'Referer': 'https://impostometro.com.br/',
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

    def test_get_counter(self):
        state = "sc"
        start_date = "01/01/2017"
        end_date = "09/05/2017"
        result = self.client.get_counter(state, start_date, end_date)
        print result