import requests
import json


robot_key= "Jc8yPl4kOtrZTzFkBMIn"
robot_key= "1258"

scot2data= requests.get("http://rad-dashboard.azurewebsites.net/api/nodesconfig/get?robotId="+robot_key+"&node=roameo_nav&fulljson")
print(scot2data.text)

w = json.loads(scot2data.text)
print(w)
x= json.loads (w)
print(x)


