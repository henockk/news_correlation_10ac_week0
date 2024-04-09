import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Read the CSV file
df = pd.read_csv('rating.csv')

# Assuming the text data is stored in a column named 'text'
text_data = df['usa']

# TF-IDF Keyword Extraction
def extract_keywords_tfidf(text, n_keywords=5):
    # Initialize TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_features=1000)
    
    # Fit and transform the text
    tfidf_matrix = tfidf_vectorizer.fit_transform(text)
    
    # Get feature names
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    # Get top N keywords based on TF-IDF scores
    top_keywords_indices = (-tfidf_matrix.toarray().mean(axis=0)).argsort()[:n_keywords]
    keywords_tfidf = [feature_names[idx] for idx in top_keywords_indices]
    
    return keywords_tfidf

# Extract keywords using TF-IDF
print("Keywords extracted using TF-IDF:")
keywords_tfidf = extract_keywords_tfidf(text_data)
print(keywords_tfidf)