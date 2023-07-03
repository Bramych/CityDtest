import requests
import json

class API:

    def product_detail(self):
        base = {"region_code": "moscowregion",
                "xmlId": "CC8ABCD6-6989-832F-9E05-3DE0A030A06B"}
        url = "https://zc-qa-test.win/api/v4/productDetail/"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Cookie': 'BITRIX_SM_ABTEST_s1=1%7CA; PHPSESSID=7BqXpaWjSkngQsYHX8MVmA8VYWNF1t77; zc_v4_region=%7B%22id%22%3A%22Moscowregion%22%2C%22num%22%3A%2277%22%2C%22name%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%20%5Cu0438%20%5Cu043e%5Cu0431%5Cu043b%5Cu0430%5Cu0441%5Cu0442%5Cu044c%22%2C%22lat%22%3A%2255.75222%22%2C%22lon%22%3A%2237.61556%22%2C%22long%22%3A%2237.61556%22%2C%22cityNames%22%3A%7B%22i%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22r%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu044b%22%2C%22p%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0435%22%7D%2C%22names%22%3A%7B%22i%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%20%5Cu0438%20%5Cu043e%5Cu0431%5Cu043b%5Cu0430%5Cu0441%5Cu0442%5Cu044c%22%2C%22r%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu044b%20%5Cu0438%20%5Cu043e%5Cu0431%5Cu043b%5Cu0430%5Cu0441%5Cu0442%5Cu0438%22%2C%22p%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0435%20%5Cu0438%20%5Cu043e%5Cu0431%5Cu043b%5Cu0430%5Cu0441%5Cu0442%5Cu0438%22%7D%7D'
        }
        response = requests.request("POST", url, headers=headers, data=base)
        print(response.text)
        assert response.status_code == 200 and type(response.json()["status"]) is int