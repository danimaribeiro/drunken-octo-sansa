#coding=utf-8
'''
Created on Aug 13, 2014

@author: danimar
'''
from flask.ext.httpauth import HTTPBasicAuth
from flask import Flask, jsonify, make_response, request
from app.serviceapi.processa_nfe import processar_xml
#from rq import Queue
#from redis import Redis

BROKER_URL = 'amqp://guest:guest@localhost:5672//'

app = Flask(__name__, instance_path=r'C:\Projetos\drunken-octo-sansa\\')
#redis_conn = Redis()
#q = Queue(connection=redis_conn)
auth = HTTPBasicAuth()

@app.route('/envio_xml', methods = ['GET', 'POST'])
#@auth.login_required
def envio_xml():
    xml = request.data
    print(xml)
    job = processar_xml.delay(xml, request.remote_addr)
    return jsonify( { 'id': job.id, 'codigo':'10', 'resposta':  'Xml recebido com sucesso' } )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'erro': 'Url não encontrada' } ), 404)

@app.errorhandler(405)
def not_allowed(error):
    return make_response(jsonify( { 'erro': 'Método não permitido' } ), 405)

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 401)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')