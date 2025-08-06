from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/prices', methods=['GET'])
def get_prices():
    data = pd.read_csv("data/BrentOilPrices_Preprocessed.csv")
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
    events = pd.read_csv("data/Events.csv")
    return jsonify(events.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
