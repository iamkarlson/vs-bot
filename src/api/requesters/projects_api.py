import pprint

from api.baseapi import BaseApi

class ProjectsApi(BaseApi):
    def __init__(self):
        BaseApi.__init__(self,"projects")
        self.build_client()
        print('projects api ctor.')

    def GET(self):
        self.build_client()
        projects= self.get()
        return projects

    def GET(self, id):
        self.build_client()
        project = self.get(id)
        return project


if __name__=="__main__":
    api = ProjectsApi()
    print(api.api_url())
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(api.get())
