import base64
import requests
import pprint
from config import config_manager


class BaseApi:
    def __init__(self, api_type):
        print('base api ctor')
        self.api_type = api_type

    def build_client(self):
        print('creating vso client')
        # password_mgr = urllib.top_level_url
        self.config = config_manager.ConfigManager("bot.ini")
        top_level_url = self.config.URL
        token = ":" + self.config.TOKEN
        print(token)
        self.pat = base64.b64encode(bytes(token, 'ascii')).decode("utf-8", "ignore")
        print(self.pat)
        self.headers = {"Authorization": f"Basic {self.pat}"}

    def api_url(self):
        default_url = "%s/%s/_apis" % (self.config.URL, self.config.COLLECTION)
        print(default_url)
        return {
            'wis': f"{default_url}/wit/workitems",
            'projects': f"{default_url}/projects",
        }[self.api_type]

    def get(self):
        response = requests.get(self.api_url(), headers=self.headers)
        print(response.text)
        return response.json()




if __name__ == "__main__":
    api = BaseApi("projects")
    api.build_client()
    # print(config.URL) print(config.COLLECTION)
    print(api.api_url())
    pp = pprint.PrettyPrinter(indent=4)
    projects = api.get()
    project = next(x for x in projects['value'])
    pp.pprint()
