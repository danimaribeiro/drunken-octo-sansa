'''
Created on 18/08/2014

@author: danimaribeiro
'''
# Run a test server.
from app import app
app.run(host='0.0.0.0', port=8080, debug=True)