'''
Created on 18/08/2014

@author: danimaribeiro
'''

if __name__ == '__main__':
    from app import app
    app.run(host='0.0.0.0', port=8080, debug=True)