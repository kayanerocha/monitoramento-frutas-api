from decouple import config
import dotenv
import os
import json


class ENVIRONMENT:
    def __init__(self):
        project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
        dotenv_path = os.path.join(project_dir, '.env')
        dotenv.load_dotenv(dotenv_path)
        self.domain = config("DOMAIN")
        self.prefix = config("PREFIX")

    def get_instance(self):
        if not hasattr(self, "_instance"):
            self._instance = ENVIRONMENT()
        return self._instance

    def getDomain(self):
        return self.domain

    def getPrefix(self):
        return self.prefix


domain = ENVIRONMENT().get_instance().getDomain()
prefix = ENVIRONMENT().get_instance().getPrefix()


def build_swagger_config_json():
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
    config_file_path = f'{project_dir}/static/swagger/config.json'

    with open(config_file_path, 'r') as file:
        config_data = json.load(file)

    config_data['servers'] = [
        {"url": f"http://localhost:5000{prefix}"},
        {"url": f"https://monitoramentofrutas.pythonanywhere.com{prefix}"}
    ]

    new_config_file_path = f'{project_dir}/static/swagger/config.json'

    with open(new_config_file_path, 'w') as new_file:
        json.dump(config_data, new_file, indent=2)