import requests
import json

class Account:

    def test_get_info(self):
        url = "https://zc-qa-test.win/api/checkLogin/"
        payload = json.dumps({
            "login": "+79803876814"
        })
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Cookie': 'BITRIX_SM_ABTEST_s1=1%7CA; PHPSESSID=92juKJoXUWVD6UFSUZM1lRuwdKykaQKq; __ddg1_=JmlcibCJcCra9GpP0aFq; zc_v4_region=%7B%22id%22%3A%22Moscowregion%22%2C%22num%22%3A%2277%22%2C%22name%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%20%5Cu0438%20%5Cu043e%5Cu0431%5Cu043b%5Cu0430%5Cu0441%5Cu0442%5Cu044c%22%2C%22lat%22%3A%2255.75222%22%2C%22lon%22%3A%2237.61556%22%2C%22long%22%3A%2237.61556%22%2C%22cityNames%22%3A%7B%22i%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22r%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu044b%22%2C%22p%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0435%22%7D%2C%22names%22%3A%7B%22i%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%20%5Cu0438%20%5Cu043e%5Cu0431%5Cu043b%5Cu0430%5Cu0441%5Cu0442%5Cu044c%22%2C%22r%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu044b%20%5Cu0438%20%5Cu043e%5Cu0431%5Cu043b%5Cu0430%5Cu0441%5Cu0442%5Cu0438%22%2C%22p%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0435%20%5Cu0438%20%5Cu043e%5Cu0431%5Cu043b%5Cu0430%5Cu0441%5Cu0442%5Cu0438%22%7D%7D'
        }
        response = requests.get(url, headers=headers, data=payload)
        print(response.status_code)
        assert response.status_code == 200



