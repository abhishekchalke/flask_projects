from flask import Flask
from flask import jsonify, request, current_app

import json
import utils


# create flask app instance
app = Flask(__name__)


# In-memory storage for processed data
processed_data_storage = {}



@app.route('/fetch-data/')
def fetchData():
    # create a mock data
    mock_data = {'id': 1, 'name': 'Sample Product', 'price': 100.0}

    # process data
    processed_data = utils.process_data(mock_data)

    # store in data 
    processed_data_storage[mock_data['id']] = processed_data

    return jsonify({"message": "Data fetched and processed successfully."})



@app.route('/get-processed-data/')
def getProcessedData():
    return jsonify(processed_data_storage)





if __name__ == '__main__':
    app.run(debug=True)






