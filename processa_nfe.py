'''
Created on Aug 13, 2014

@author: danimar
'''
from xml.etree.ElementTree import iterparse
import cStringIO
from pymongo import MongoClient
import xmltodict

def processar_xml(xml, ip):
    nota = xmltodict.parse(xml) 
    client = MongoClient('localhost', 27017)
    db = client.metrics    
    notas_fiscais = db.notas_fiscais
    notas_fiscais.insert(nota)

