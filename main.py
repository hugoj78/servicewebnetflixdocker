import json
import requests 

def post(json_file, base_url):
    with open(json_file, "r") as read_file:
        json_obj = json.load(read_file)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    try:
        for data in json_obj['data']:
            print(data)
            request = requests.post(base_url, headers=headers, json=data)
    except Exception as e:
        return {request.status_code}


# POST MOCKUP DATA
post("./json/media.json",  "http://0.0.0.0:8092/medias")
post("./json/poster.json", "http://0.0.0.0:8091/posters")
post("./json/user.json", "http://0.0.0.0:8090/users")




#post(endpoint, token, json_obj, headers)
#get(endpoint, token, headers)
