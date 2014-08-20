'''
Created on 19/08/2014

@author: danimaribeiro
'''
import geojson
from pymongo import MongoClient

if __name__ == '__main__':
    arquivo = '../geo/municipios.geojson'

    client = MongoClient('localhost', 27017)
    db = client.metrics
    municipios = db.municipios

    with open(arquivo, 'r') as f:
        dump = f.read()
        geo = geojson.loads(dump)
        for feature in geo.features:
            municipios.insert(feature)