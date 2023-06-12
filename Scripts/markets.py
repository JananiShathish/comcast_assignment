''' this module has got 2 API endpoints implementations
1: to get the summary details of all the market
2: to get the summary details of one particular market'''

import os
import requests

from flask import  request, jsonify, render_template
from werkzeug.exceptions import Unauthorized

PASSWD = {"janani": "shathish", "sashvith": "rakshan"}

def basic_auth(username, password):
    if PASSWD.get(username) == password:
        return {"sub": username}
    else: 
        raise Unauthorized('unauthorized User') # raise exception for custom error response
   

def fetch_updates():
    ''' To fetch all the markets summary details'''
    try:
            url = 'https://api.bittrex.com/v3/markets/summaries'
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return jsonify({'error': 'Failed to fetch cryptocurrency market updates'}), response.status_code
            market_updates = response.json()
            return jsonify({'result': market_updates})
    
    except request.exceptions.RequestException as error:
        return 'Error fetching updates: ' + str(error), 500


def summary_updates(marketname):
    '''This function is to get the particular market summary details by 
    sending the symbol name as query string in the uri'''
    try:
        if not marketname:
            return jsonify({'error': 'Missing market parameter'}), 400
        url = f'https://api.bittrex.com/v3/markets/{marketname}/summary'
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch cryptocurrency market updates'}), response.status_code
        market_updates = response.json()
        return jsonify({'result': market_updates})

    except request.exceptions.RequestException as error:
        return 'Error fetching updates: ' + str(error), 500


