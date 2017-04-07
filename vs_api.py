import api.wiapi

if __name__=="__main__":
    api = api.wiapi()
    print(api.GET(12))