import urllib
import config.config_manager

class BaseApi:
    def __init__(self):
        print('base api ctor')
    def build_client(self,type):
        print('creating vso client')
        #password_mgr = urllib.HTTPPasswordMgrWithDefaultRealm()
        password_mgr = urllib.top_level_url
        top_level_url = "http://example.com/"

        password_mgr.add_password(None, top_level_url, 'user', 'password')

        handler = urllib.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.build_opener(urllib.HTTPHandler, handler)
        request = urllib.Request(url)


def api_url(x):
    default_url = "%s/%s/_apis"%config.URL,config.COLLECTION
    print(default_url)
    return {
        'wis': "{default_url}/wi/",
        'projects': "{default_url}/projects" % locals(),
    }[x]

if __name__=="__main__":
    print(config.URL)
    print(config.COLLECTION)
    print(api_url("projects"))
