#coding=utf-8
'''
Created on 20/08/2014

@author: danimaribeiro
'''
from flask import Blueprint, render_template
import vincent

graphs = Blueprint('graficos', __name__,  url_prefix='/graficos')

from app import mongo

@graphs.route('/')
def index():
    return render_template('graficos/index.html')

@graphs.route('/impostos')
def impostos():
    return render_template('graficos/impostos.html')

@graphs.route('/vendas')
def vendas():
    return render_template('graficos/vendas.html')

@graphs.route('/api_vendas', methods=['GET', 'POST'])
def api_vendas():
    list_data = [10, 20, 30, 20, 15, 30, 45]
    bar = vincent.Bar(list_data, width=580, height=260)
    return bar.to_json()

@graphs.route('/api_vendas_dia', methods=['GET', 'POST'])
def api_vendas_dia():
    import pandas as pd
    resultado = mongo.db.notas_fiscais.aggregate([
            {"$group":{
                "_id": "$nfeProc.NFe.infNFe.ide.dEmi",
                "total":{"$sum": "$nfeProc.NFe.infNFe.total.ICMSTot.vNF" }
            }},
            {"$sort": {"_id": -1}},
            {"$limit":20}
            ])

    resultado = resultado['result']
    resultado = pd.DataFrame.from_records(resultado, index="_id")
    line = vincent.Line(resultado, width=540, height=380)
    line.axis_titles(x='', y='Valor vendas')
    line.y_axis_properties(label_align="right", title_offset=-40, title_size=14)
    return line.to_json()

@graphs.route('/api_impostos', methods=['GET', 'POST'])
def api_impostos():
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
