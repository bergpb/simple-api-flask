# -*- coding: utf-8 -*-

import os
import json
from flask import Flask, jsonify, request
from urllib.request import urlopen, Request

app = Flask(__name__)

@app.route('/api', methods=['GET'])

def getInfo():
    
    nomes = ['berg', 'kelven', 'nardier']

    return jsonify(data = nomes)
        
  
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
