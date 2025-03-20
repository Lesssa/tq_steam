import json


class Config:
    @staticmethod
    def load_config():
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)


config = Config.load_config()
