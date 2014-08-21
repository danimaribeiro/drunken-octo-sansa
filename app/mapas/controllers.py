#coding=utf-8

from flask import Blueprint, render_template, flash, request, redirect, url_for
from geojson import FeatureCollection, Feature, dumps

mapa = Blueprint('mapas', __name__,  url_prefix='/mapas')

from app import mongo

@mapa.route('/')
def mapas():
    return render_template('mapas/mapas.html')

@mapa.route('/mapa.json',  methods = ['GET', 'POST'])
def json_mapas():
    municipios = mongo.db.municipios.find({'properties.NOMEUF': 'SANTA CATARINA'}).limit(50)
    colecao = []
    for mun in municipios:
        f = Feature( properties=mun['properties'], geometry=mun['geometry'])
        f.properties['name'] = mun['properties']['NOME_1']
        colecao.append(f)
    colecao = FeatureCollection(colecao)
    return dumps(colecao)

    #{ $match : { "nfeProc.NFe.infNFe.dest.enderDest.cMun" : "4217501" } }
    #{"$group":{
    #        "_id": "$nfeProc.NFe.infNFe.dest.enderDest.cMun",
    #        "total":{"$sum": "$nfeProc.NFe.infNFe.total.ICMSTot.vNF" }
    #    }
    #}