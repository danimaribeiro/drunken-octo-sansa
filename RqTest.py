'''
Created on Aug 13, 2014

@author: danimar
'''
from processa_nfe import processar_xml
from os import listdir
from os.path import isfile, join
import requests

if __name__ == '__main__':
    diretorio = './xmls_teste/'
    onlyfiles = [ join(diretorio,f) for f in listdir(diretorio) if isfile(join(diretorio,f)) ]
    total = 0
    for i in range(0,100):
        for item in onlyfiles:
            with open(item, 'rb') as f:
                conteudo = f.read()            
                r = requests.post('http://localhost:5000/envio_xml', data=conteudo)
                print r.status_code
                total += 1
                if total>=10000:
                    break
        if total>=10000:
            break
        
    