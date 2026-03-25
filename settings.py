from pydantic import BaseModel
from cat import plugin


class MySettings(BaseModel):
    number_of_results: int = 10
    language: str = "en"


@plugin
def settings_schema():
    return MySettings.model_json_schema()