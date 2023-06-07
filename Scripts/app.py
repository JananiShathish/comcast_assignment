from flask import Flask,request
# import requests

app=Flask(__name__)

@app.route('/fetch_updates')
def fetch_updates():
    try:
        response = request.json.get('https://bittrex.github.io/api/v3')
        response.raise_for_status()  # Raises an exception for failed requests
        updates = response.text
        
        # Process the updates...
        # print(updates)
        return 'Updates fetched successfully'
    except request.exceptions.RequestException as e:
        return 'Error fetching updates: ' + str(e), 500  
    

if __name__ == '__main__':
    app.run(debug=True)    