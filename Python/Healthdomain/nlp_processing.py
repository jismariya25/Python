from sklearn.feature_extraction.text import CountVectorizer

# Function to perform Bag of Words vectorization
def vectorize_text(df):
    vectorizer = CountVectorizer()
    X_text = vectorizer.fit_transform(df['Clean_Diagnosis'])

    # Convert to DataFrame for visualization
    text_df = pd.DataFrame(X_text.toarray(), columns=vectorizer.get_feature_names_out())
    print("Word Frequency Matrix:")
    print(text_df.head())
