from api.constants import *
from api.requesters.wiapi import WiApi


class Worker:
    def __init__(self):
        self.vsts_api = WiApi()

    def get_wi(self, wi_id):
        attachments = {}
        wi = self.vsts_api.get_by_id(wi_id)

        if ITEM_TYPE_FIELD not in wi.fields:
            attachments = [{"pretext": "this kind of work items is not supported yet"}]
            return [attachments]
        wi_type = wi.fields[ITEM_TYPE_FIELD]
        if wi_type== ITEM_TYPE_BUG:
            attachments = {"pretext": f"Bug #{wi_id} information:",
                           "text": f"Title: {wi.fields[TITLE_FIELD]}\n"
                                   f"Description: {wi.fields['Microsoft.VSTS.TCM.ReproSteps']}",
                           "color": "#cc293d"}
        elif wi_type == ITEM_TYPE_PBI:
            attachments = {"pretext": f"Product Backlog Item #{wi_id} information:",
                           "text": f"Title: {wi.fields[TITLE_FIELD]}\n"
                                   f"Description: {wi.fields[PBI_DESCRIPTION_FIELD]}",
                           "color": "#009ccc"}
        else:
            attachments = {"pretext": f"{wi_type} #{wi_id} information:",
                           "text": f"Title: {wi.fields[TITLE_FIELD]}\n"
                                   f"Description: {wi.fields[PBI_DESCRIPTION_FIELD]}"}
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
        return [attachments]
