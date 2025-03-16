# 📝 Sentiment Analysis on Reviews  


🔍 **Analyzing customer reviews using TF-IDF and Logistic Regression**  



![Sentiment Analysis]


([screenshots/banner.png](https://github.com/Abhinav-gupta-123/Sentimental-Analysis/blob/main/sentiment_analysis/neggative%20review.jpg))


([screenshots/banner.png](https://github.com/Abhinav-gupta-123/Sentimental-Analysis/blob/main/sentiment_analysis/possitive%20review.jpg))


---

## 📖 Overview  

This project performs **Sentiment Analysis** on customer reviews using **TF-IDF Vectorization** and **Logistic Regression**. It classifies reviews as **positive or negative**, helping businesses analyze customer feedback efficiently.  



✔ **Dataset Source:** [Kaggle](https://www.kaggle.com/)  


✔ **Vectorization Method:** TF-IDF (Term Frequency-Inverse Document Frequency)  


✔ **Model Used:** Logistic Regression  


---


## 🚀 Features  


✅ Text preprocessing (stopword removal, tokenization, stemming)  


✅ TF-IDF vectorization for feature extraction  


✅ Logistic Regression for sentiment classification  


✅ Performance evaluation using accuracy, precision, recall, and F1-score  



---


## 📂 Dataset  


The dataset contains **customer reviews and their sentiment labels (Positive/Negative).**  



🔹 **Columns:**  


- `Review Text`: The actual review

- `Sentiment Label`: **1 (Positive) / 0 (Negative)**  


📁 **Dataset Location:** `[data/sentiment_reviews.csv](https://github.com/Abhinav-gupta-123/Sentimental-Analysis/blob/main/sentiment_analysis/customer_reviews.csv)`  



---



## ⚙ Installation & Setup  


To run this project, follow these steps:  


1️⃣ Clone the repository  
```bash
git clone https://github.com/Abhinav-gupta-123/Sentimental-Analysis.git
cd Sentimental-Analysis


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run the sentiment analysis script


python sentiment_analysis.py



📊 Model Performance


Accuracy: 1.0
Classification Report:
               precision    recall  f1-score   support

    negative       1.00      1.00      1.00       983
    positive       1.00      1.00      1.00      1017

    accuracy                           1.00      2000
   macro avg       1.00      1.00      1.00      2000
weighted avg       1.00      1.00      1.00      2000




🖥 Example Output


Enter your review: "The product quality is amazing!"


Predicted Sentiment: ✅ Positive






Enter your review: "Worst service ever. Very disappointed."


Predicted Sentiment: ❌ Negative






