''' this module has got 2 API endpoints implementations
1: to get the summary details of all the market
2: to get the summary details of one particular market'''

from flask import Flask, request, jsonify
import requests
from config import USERNAME, PASSWORD


app = Flask(__name__)


def authenticate_user(username, password, uname, pwd):
    '''Implementing authentication logic here'''

    # valid_username = 'Username'
    # valid_password = 'Password'
    valid_username = uname
    valid_password = pwd

    if username == valid_username and password == valid_password:
        return True
    else:
        return False


@app.route('/fetch_updates', methods=['GET'])
def fetch_updates():
    ''' To fetch all the markets summary details'''
    try:

        uname = request.args.get('Username')
        pswd = request.args.get('Password')
        if authenticate_user(uname, pswd, USERNAME, PASSWORD):
            # if not market:
            #     return jsonify({'error': 'Missing market parameter'}), 400

            # Replace with the actual API endpoint
            url = 'https://api.bittrex.com/v3/markets/summaries'
            response = requests.get(url, timeout=10)
            # response = requests.get(url,auth=auth)
            if response.status_code != 200:
                return jsonify({'error': 'Failed to fetch cryptocurrency market updates'}), response.status_code

            # Process the response and return the result
            market_updates = response.json()
            return jsonify({'result': market_updates})
        else:
            return 'Credentials are not correct'
    except request.exceptions.RequestException as error:
        return 'Error fetching updates: ' + str(error), 500


@app.route('/fetch_updates/summary', methods=['GET'])
def summary_updates():
    '''This function is to get the particular market summary details by 
    sending the symbol name as query string in the uri'''
    try:
        uname = request.args.get('Username')
        pswd = request.args.get('Password')
        market = request.args.get('name')

        if authenticate_user(uname, pswd, USERNAME, PASSWORD):

            if not market:
                return jsonify({'error': 'Missing market parameter'}), 400

            # Replace with the actual API endpoint
            url = f'https://api.bittrex.com/v3/markets/{market}/summary'
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return jsonify({'error': 'Failed to fetch cryptocurrency market updates'}), response.status_code

            # Process the response and return the result
            market_updates = response.json()

        # ...

            return jsonify({'result': market_updates})
        else:
            return 'Credentials are not correct'
    except request.exceptions.RequestException as error:
        return 'Error fetching updates: ' + str(error), 500


if __name__ == '__main__':
    app.run(debug=True)
