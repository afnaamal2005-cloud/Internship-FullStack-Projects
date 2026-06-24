import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
data = pd.read_csv("spam.csv")

# Split data
x = data["message"]
y = data["label"]

# Convert text into numbers
vectorizer = CountVectorizer()
x_vectorized = vectorizer.fit_transform(x)

# Train model
model = MultinomialNB()
model.fit(x_vectorized, y)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully!")