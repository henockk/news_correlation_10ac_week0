import os
import streamlit as st
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import load_data, count_articles_per_website, get_top_and_bottom_websites

# Set the path to the dataset directory
dataset_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dataset'))

# Load the data
rating_csv_path = os.path.join(dataset_dir, 'rating.csv')
rating_df = load_data(rating_csv_path)

# Count articles per website and get unique article_ids
articles_per_website_sorted = count_articles_per_website(rating_df)

# Get top and bottom 10 websites
top_10, bottom_10 = get_top_and_bottom_websites(articles_per_website_sorted)

# Display the results
st.write('## Top 10 Websites by Article Count')
st.write(top_10)

st.write('## Bottom 10 Websites by Article Count')
st.write(bottom_10)

# Plotting
st.write('## Plot')

# Plot top 10 websites
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_10.index, y=top_10['article_count'], ax=ax)
ax.set_xlabel('Website')
ax.set_ylabel('Article Count')
ax.set_title('Top 10 Websites by Article Count')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Plot bottom 10 websites
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=bottom_10.index, y=bottom_10['article_count'], ax=ax)
ax.set_xlabel('Website')
ax.set_ylabel('Article Count')
ax.set_title('Bottom 10 Websites by Article Count')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)
