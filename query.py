import json

import requests

DISFACTORY_API_URL = "https://staging.disfactory.tw/api/sectcode?sectcode={sectcode}&landcode={land_number}"


def query_disfactory(sectcode: str, land_number: str) -> str:
    url = DISFACTORY_API_URL.format(sectcode=sectcode, land_number=land_number)
    result = requests.get(url)
    if result.status_code != 200:
        return ""

    json_data = result.json()
    return json_data["id"]


def query_factory_id(json_data_path: str):
    with open(json_data_path, "r") as f:
        data = json.load(f)

    violation_list = data["violations"]

    for violation in violation_list:
        sectcode = violation["sectcode"]
        land_numbers = violation["land_numbers"]
        for land_number in land_numbers:
            factory_id = query_disfactory(sectcode, land_number)
            if factory_id != "":
                violation["factory_id"] = factory_id
                break

    with open(json_data_path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
