
import requests as rq

res = rq.get("https://jsonplaceholder.typicode.com/users")

json = res.json()

print("Nombre dentro del JSON: {}".format(json['forms'][0]['name']))

json['forms'][0]['name'] = "LUIS"
print(json['forms'][0]['name'])

print("Nombre dentro del JSON: {}".format(json['forms'][0]['edad']))

json['forms'][0]['edad'] = "26"
print(json['forms'][0]['edad'])