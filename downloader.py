# -*- coding: utf-8 -*-

import requests
import json
import zipfile
import os

def export(url: str, extension: str, method):
    response = method(url % extension)
    if (response.status_code >= 400):
        print("Failed document import with status code %s" % response.status_code)
        return
    with open("./data/" + extension + ".json", "w") as file:
        response_json = json.loads(response.content.decode("utf-8"))
        file.write(json.dumps(response_json, indent=2))

def main():
    url_template = "https://www.armep.gwi.uni-muenchen.de/api/%s"
    extended_url_template = url_template % "index.php/%s"
    token_url_template = extended_url_template % "token_list?index=%s"
    
    export(url_template, "documents", requests.post)
    export(token_url_template, "translations", requests.get)
    export(token_url_template, "transliterations", requests.get)
    export(token_url_template, "lemmata", requests.get)
    export(token_url_template, "signs", requests.get)
    
    data_url = "https://www.armep.gwi.uni-muenchen.de/db_update/armep_data.zip"
    data_response = requests.get(data_url)
    zip_file_path = "./data/armep_data.zip"
    open(zip_file_path, "wb").write(data_response.content)
    with zipfile.ZipFile(zip_file_path) as zip_file:
        zip_file.extractall("./data")
    os.remove(zip_file_path)
        
    
if __name__ == "__main__":
    main()

