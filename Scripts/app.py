from flask import Flask,request,jsonify
import requests
from config import Username,Password
from functools import wraps

app=Flask(__name__)
def authenticate_user(username, password):
    '''Implementing authentication logic here'''
    
    valid_username = 'Username'
    valid_password = 'Password'

    if username == valid_username and password == valid_password:
        return True
    else:
        return False   


def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = request.headers.get('Username')
        password = request.headers.get('Password')

        # Perform authentication logic
        if not authenticate_user(username, password):
            return jsonify({'error': 'Authentication failed'}), 401

        return f(*args, **kwargs)

    return decorated_function

@app.route('/fetch_updates',methods=['GET'])
# @authenticate
def fetch_updates():
    try:
        
        uname = request.args.get('Username')
        pswd = request.args.get('Password')
        # auth = (uname, pswd)
        if authenticate_user(uname,pswd):
            # if not market:
            #     return jsonify({'error': 'Missing market parameter'}), 400
            
            url = f'https://api.bittrex.com/v3/markets/summaries'  # Replace with the actual API endpoint
            response = requests.get(url)
            # response = requests.get(url,auth=auth)
            if response.status_code != 200:
                return jsonify({'error': 'Failed to fetch cryptocurrency market updates'}), response.status_code

            # Process the response and return the result
            market_updates = response.json()

        # ...

            return jsonify({'result': market_updates})
    except request.exceptions.RequestException as e:
        return 'Error fetching updates: ' + str(e), 500  
    
@app.route('/fetch_updates/summary',methods=['GET'])
# @authenticate
def summary_updates():
    try:
        uname = request.args.get('Username')
        pswd = request.args.get('Password')
        market = request.args.get('name')
        # auth = (uname, pswd)
        if authenticate_user(uname,pswd):
        
            if not market:
                return jsonify({'error': 'Missing market parameter'}), 400
            
            url = f'https://api.bittrex.com/v3/markets/{market}/summary'  # Replace with the actual API endpoint
            response = requests.get(url)
            if response.status_code != 200:
                return jsonify({'error': 'Failed to fetch cryptocurrency market updates'}), response.status_code

            # Process the response and return the result
            market_updates = response.json()

        # ...

            return jsonify({'result': market_updates})
    except request.exceptions.RequestException as e:
        return 'Error fetching updates: ' + str(e), 500      
    

if __name__ == '__main__':
    app.run(debug=True)    