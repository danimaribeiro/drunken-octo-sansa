'''
Created on 18/08/2014

@author: danimaribeiro
'''
from os import listdir
from os.path import isfile, join
import xmltodict
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

if __name__ == '__main__':
    diretorio = './xmls_teste/'
    onlyfiles = [ join(diretorio,f) for f in listdir(diretorio) if isfile(join(diretorio,f)) ]

    with open(onlyfiles[0], 'rb') as f:
        conteudo = f.read()
        nota = xmltodict.parse(conteudo, postprocessor=postprocessor)
        print (nota)
