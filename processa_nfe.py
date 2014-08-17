'''
Created on Aug 13, 2014

@author: danimar
'''
from pymongo import MongoClient
import xmltodict
from celery import Celery

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
app = Celery('processa_nfe', broker=BROKER_URL)

@app.task
def processar_xml(xml, ip):
    nota = xmltodict.parse(xml) 
    client = MongoClient('localhost', 27017)
    db = client.metrics    
    notas_fiscais = db.notas_fiscais
    notas_fiscais.insert(nota)
    return 1