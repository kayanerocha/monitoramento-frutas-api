from flask_restful import Resource
from flask import jsonify
import json
import os

class SwaggerConfig(Resource):
    def get(self):
        project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
        with open(f'{project_dir}/static/swagger/config.json', 'r') as config_file:
            config_data = json.load(config_file)
        return jsonify(config_data)