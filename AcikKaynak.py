from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Kullanici(Resource):
    def get(self):
       data = pd.read_csv('Kullanici.csv')
       data = data.to_dict('records')
       return { 'data' : data}, 200

    def post(self):
        name = request.args['name']
        position = request.args['position']
        team = request.args['team']

        data = pd.read_csv('Kullanici.csv')

        new_data = pd.DataFrame({
            'name': [name],
            'position': [position],
            'team': [team]
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('Kullanici.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200

    class Name(Resource):
        def get(self):
            data = pd.read_csv('Kullanici.csv', usecols=[0])
            data = data.to_dict('records')
            return {'data': data}, 200

    api.add_resource(Name, '/Kullaniciname')
    api.add_resource(Kullanici, '/Kullanici')

    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=6767)
