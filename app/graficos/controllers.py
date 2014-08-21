#coding=utf-8
'''
Created on 20/08/2014

@author: danimaribeiro
'''
from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify
from geojson import FeatureCollection, Feature, dumps
import vincent

graphs = Blueprint('graficos', __name__,  url_prefix='/graficos')

from app import mongo

@graphs.route('/')
def mapas():
    return render_template('graficos/grafico.html')

@graphs.route('/vendas', methods=['GET', 'POST'])
def vendas():
    list_data = [10, 20, 30, 20, 15, 30, 45]
    bar = vincent.Bar(list_data)
    return bar.to_json()

@graphs.route('/mensal', methods=['GET', 'POST'])
def mensal():
    import pandas as pd

    farm_1 = {'apples': 10, 'berries': 32, 'squash': 21, 'melons': 13, 'corn': 18}
    farm_2 = {'apples': 15, 'berries': 43, 'squash': 17, 'melons': 10, 'corn': 22}
    farm_3 = {'apples': 6, 'berries': 24, 'squash': 22, 'melons': 16, 'corn': 30}
    farm_4 = {'apples': 12, 'berries': 30, 'squash': 15, 'melons': 9, 'corn': 15}

    farm_data = [farm_1, farm_2, farm_3, farm_4]
    farm_index = ['Farm 1', 'Farm 2', 'Farm 3', 'Farm 4']
    df_farm = pd.DataFrame(farm_data, index=farm_index)

    group = vincent.GroupedBar(df_farm)
    group.axis_titles(x='Total Produce', y='Farms')
    group.legend(title='Produce Types')
    group.colors(brew='Set1')
    return group.to_json()
