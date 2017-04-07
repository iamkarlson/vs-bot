import models
from api.baseapi import BaseApi

class WiApi(BaseApi):
    def __init__(self):
        BaseApi(self)
        print('wi_api ctor.')

    def GET(self,id):
        client = BaseApi.build_client('wi')
        wi= client.get(id)
        return wi