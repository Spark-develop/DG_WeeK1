import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open('../response.json') as json_obj:
    response = json.load(json_obj)

name = input("Please add your name: ")
sport = input("Please add your favourite sports name: ")
if (sport == ""):
    sport = 'Table Tennis'
if (name):
    response[name] = sport
    with open('../response.json','w') as file:
        json.dump(response,file,indent=0)
