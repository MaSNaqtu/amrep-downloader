# -*- coding: utf-8 -*-


import requests
import json

def main():
    response = requests.post("https://www.armep.gwi.uni-muenchen.de/api/documents")
    if (response.status_code >= 400):
        print("Failed document import with status code %s" % response.status_code)
        return
    with open("./data/documents.json", "w") as file:
        response_json = json.loads(response.content.decode("utf-8"))
        file.write(json.dumps(response_json, indent=2))
        
    response = requests.post("https://www.armep.gwi.uni-muenchen.de/api/tokens")
    if (response.status_code >= 400):
        print("Failed token import with status code %s" % response.status_code)
        return
    with open("./data/tokens.json", "w") as file:
        file.write(response.content.decode("utf-8"))
        
    
if __name__ == "__main__":
    main()

