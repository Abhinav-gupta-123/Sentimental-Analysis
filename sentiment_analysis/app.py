# app.py
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load(r'C:\Users\abhin\Desktop\sentiment_analysis\sentiment_model.pkl')
tfidf = joblib.load(r'C:\Users\abhin\Desktop\sentiment_analysis\tfidf_vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    review = data['review']
    review_tfidf = tfidf.transform([review])
    prediction = model.predict(review_tfidf)
    return jsonify({'sentiment': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True,port=5000)