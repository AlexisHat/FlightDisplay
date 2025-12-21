from opensky_api import OpenSkyApi

class OpenSkyClient:
    def __init__(self, username=None, password=None):
        self.api = OpenSkyApi(username, password)

    def get_states_for_bbox(self, bbox):
        return self.api.get_states(bbox=bbox)