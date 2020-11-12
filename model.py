import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv('Sentiment.csv')
df.head(5)

processed_features = []

for sentence in range(0, len(features)):
    # Remove all the special characters
    processed_feature = re.sub(r'\W', ' ', str(features[sentence]))

    # remove all single characters
    processed_feature= re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature)

    # Remove single characters from the start
    processed_feature = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_feature) 

    # Substituting multiple spaces with single space
    processed_feature = re.sub(r'\s+', ' ', processed_feature, flags=re.I)

    # Removing prefixed 'b'
    processed_feature = re.sub(r'^b\s+', '', processed_feature)

    # Converting to Lowercase
    processed_feature = processed_feature.lower()

    processed_features.append(processed_feature)


X_train, X_test, y_train, y_test = train_test_split(processed_features, df['sentiment'], test_size=0.33, random_state=42)

text_clf = Pipeline([
     ('vect', CountVectorizer(token_pattern=r'\b\w+\b')),
     ('lr', LogisticRegression())
])

text_clf.fit(X_train, y_train)

predicted = text_clf.predict(X_test)
accuracy_score(y_test, predicted)

pickle.dump(text_clf, open('model.pkl','wb'))
