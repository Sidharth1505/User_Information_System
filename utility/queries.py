import json
class GetJson:
    def get_json(self):
        with open('utility/settings.json', "r") as db:
            queries = json.load(db)
            return queries