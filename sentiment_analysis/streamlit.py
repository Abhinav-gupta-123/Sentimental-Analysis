import streamlit as st
import joblib

def main():
    st.title("Customer Review Sentiment Analysis")
    st.write("Enter a review below and click **Predict Sentiment** to see the result.")
    
    # Load your saved model and vectorizer
    model = joblib.load(r'C:\Users\abhin\Desktop\sentiment_analysis\sentiment_model.pkl')
    tfidf = joblib.load(r'C:\Users\abhin\Desktop\sentiment_analysis\tfidf_vectorizer.pkl')
    
    # Text input for user
    user_review = st.text_area("Enter your review here:")
    
    if st.button("Predict Sentiment"):
        if not user_review.strip():
            st.error("Please enter a review before predicting!")
        else:
            # Vectorize the user input
            review_tfidf = tfidf.transform([user_review])
            # Predict using the loaded model
            prediction = model.predict(review_tfidf)[0]
            
            # If your model is 2-class (0/1):
            #   0 might be Negative, 1 might be Positive
            # If it's 3-class (0=Negative, 1=Average, 2=Positive), adjust accordingly
            if prediction == 0:
                sentiment_label = "Negative"
            elif prediction == 1:
                sentiment_label = "Positive"
            else:
                sentiment_label = f"Class {prediction}"  # or handle your 3-class logic here
            
            st.success(f"Predicted Sentiment: **{sentiment_label}**")

if __name__ == '__main__':
    main()
