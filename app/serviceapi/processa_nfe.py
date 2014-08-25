#coding=utf-8
'''
Created on Aug 13, 2014

@author: danimar
'''
from pymongo import MongoClient
import xmltodict
from celery import Celery
from datetime import datetime

INTEIRO = lambda x:int(x)
NUMERO = lambda x:float(x)
DATA_HORA = lambda x: datetime.strptime(x, 'AAAA-MM-DDThh:mm:ssTZD')
DATA = lambda x: datetime.strptime(x, '%Y-%m-%d')

CONVERSOES = {"cUF": INTEIRO, "vNF":NUMERO, "dEmi": DATA,
              "vBC":NUMERO, "vICMS":NUMERO, "vBCST":NUMERO, "vST":NUMERO, "vProd":NUMERO, "vFrete":NUMERO,
              "vSeg":NUMERO, "vDesc":NUMERO, "vII":NUMERO, "vIPI":NUMERO, "vPIS":NUMERO, "vCOFINS":NUMERO, "vOutro":NUMERO }


def postprocessor(path, key, value):
    try:
        if key=='Signature':
            return None
        return key, CONVERSOES[key](value) if CONVERSOES.__contains__(key) else value
    except (KeyError, ValueError, TypeError):
        return key, value

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
app = Celery('processa_nfe', broker=BROKER_URL)

@app.task
def processar_xml(xml, ip):
    print(xml)
    nota = xmltodict.parse(xml, postprocessor=postprocessor)
    client = MongoClient('localhost', 27017)
    db = client.metrics
    notas_fiscais = db.notas_fiscais
    notas_fiscais.insert(nota)
    return 1

