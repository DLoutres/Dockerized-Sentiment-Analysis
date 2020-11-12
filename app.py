import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
    	details = request.form
    	if details['form_type'] == 'answer':
    		int_features = request.form.values()
    		sentence = pd.Series(int_features)
    		predictions = model.predict(sentence)
    		prediction_text='This sentence has a {} sentiment'.format(predictions[0])
    		return prediction_text

    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
