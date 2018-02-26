import requests
import pprint
from collections import namedtuple

from api.baseapi import BaseApi

import pprint

import requests

from api.baseapi import BaseApi


class WiApi(BaseApi):
    def __init__(self):
        BaseApi.__init__(self, "wis")
        self.build_client()
        print('wi_api ctor.')

    def get_by_id(self, item_id):
        api_url = self.api_url()
        url = f"{api_url}?ids={item_id}"
        print(f"wi url: {url}")
        response = requests.get(url, headers=self.headers)
        resp_json = response.json()
        if response.status_code == 200:
            wi_json = next(x for x in resp_json['value'])
            wi = namedtuple("WorkItem", wi_json.keys())(*wi_json.values())
            return wi
        raise ValueError(resp_json['message'])



if __name__ == "__main__":
    api = WiApi()
    api.build_client()
    # print(config.URL) print(config.COLLECTION)
    print(api.api_url())
    pp = pprint.PrettyPrinter(indent=4)
    wis = api.get_by_id(1)
    pp.pprint(f"wi url :{wis.url}")
