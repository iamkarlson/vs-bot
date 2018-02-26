from api.constants import *

class BaseProcessor:
    def __init__(self):

    def get_slack_message(self, wi):
        attachments = ""
        attachments['fields'] = []
        if ASSIGNED_TO_FIELD in wi.fields:
            attachments['fields'].append({"title": "Assigned to", "short": True, "value": wi.fields[ASSIGNED_TO_FIELD]})
        else:
            attachments['fields'].append({"title": "Assigned to", "short": True, "value": "None"})
        if ITERATION_PATH_FIELD in wi.fields:
            attachments['fields'].append(
                {"title": "Iteration", "short": True, "value": wi.fields[ITERATION_PATH_FIELD]})
        else:
            attachments['fields'].append({"title": "Iteration", "short": True, "value": "None"})
        return attachments
