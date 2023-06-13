''' this module has got 2 API endpoints implementations
1: to get the summary details of all the market
2: to get the summary details of one particular market'''


import connexion

app = connexion.App(__name__, specification_dir="../") # For swagger UI API Documentation
app.add_api('swagger.yml')  

if __name__ == '__main__':
    app.run(port=5000,debug=True)
