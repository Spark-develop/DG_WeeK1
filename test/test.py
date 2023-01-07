import sys,os,json

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

with open('response.json') as json_obj:
  response = json.load(json_obj)
assert isinstance(response, dict)
assert response.get("Data Glacier") =="Table Tennis"