import json
import os
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

app = FastAPI()
in_memory_json_data: dict = {}


def load_all_json_data():
    # Load all data from JSON files in the json directory
    json_data_dir = os.path.join(SCRIPT_DIR, "json")
    for filename in os.listdir(json_data_dir):
        if filename.endswith(".json"):
            json_file_path = os.path.join(json_data_dir, filename)
            json_data = json.load(open(json_file_path)).get("violations", {})
            for item in json_data:
                in_memory_json_data[item["id"]] = item


load_all_json_data()


class Violation(BaseModel):
    id: str
    year: str
    month: str
    number: str
    city: str
    sectname: str
    sectcode: str
    land_numbers: List[str]
    usage_zone: str
    use: str
    status: List[str]
    factory_id: Optional[str] = None


@app.get("/violations/{factory_id}", response_model=List[Violation])
def get_violation_by_factory_id(factory_id: str):
    results = []
    for _, data in in_memory_json_data.items():
        if data["factory_id"] == factory_id:
            results.append(data)

    return results


@app.get("/search", response_model=List[Violation])
def search_violations(sectcode: str, land_number: str):
    results = []
    for _, data in in_memory_json_data.items():
        if data["sectcode"] == sectcode and land_number in data["land_numbers"]:
            results.append(data)

    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
