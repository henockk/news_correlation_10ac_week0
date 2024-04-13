import os
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import load_data, count_articles_per_website, get_top_and_bottom_websites,\
    count_news_media_per_country, get_countries_with_most_least_news_media, get_highest_and_lowest_traffic_websites, count_sentiment_by_website_domain, get_websites_with_highest_sentiment_count

# Set the path to the dataset directory
dataset_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dataset'))

# Load the data
rating_csv_path = os.path.join(dataset_dir, 'rating.csv')
rating_df = load_data(rating_csv_path)
traffic_csv_path = os.path.join(dataset_dir, 'traffic.csv')
traffic_df = load_data(traffic_csv_path)
domains_location_csv_path = os.path.join(dataset_dir, 'domains_location.csv')
domains_location_df = load_data(domains_location_csv_path)

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

# Create a layout with two columns
col1, col2 = st.columns(2)

# Plot top 10 websites as a horizontal bar chart
with col1:
    st.write('### Top 10 Websites by Article Count')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_10.index, y=top_10['article_count'], ax=ax)
    ax.set_xlabel('Website')
    ax.set_ylabel('Article Count')
    ax.set_title('Top 10 Websites by Article Count')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

# Plot bottom 10 websites as a horizontal bar chart
with col2:
    st.write('### Bottom 10 Websites by Article Count')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=bottom_10.index, y=bottom_10['article_count'], ax=ax)
    ax.set_xlabel('Website')
    ax.set_ylabel('Article Count')
    ax.set_title('Bottom 10 Websites by Article Count')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)


# Count news media organizations per country
news_media_per_country = count_news_media_per_country(domains_location_df)

# Get countries with the most and least news media organizations
countries_with_most_news_media, countries_with_least_news_media = get_countries_with_most_least_news_media(news_media_per_country)

# Plot countries with the most news media organizations as a pie chart
st.write('### Countries with the Most News Media Organizations')
with col1:
    fig, ax = plt.subplots()
    ax.pie(countries_with_most_news_media, labels=countries_with_most_news_media.index, autopct='%1.1f%%')
    ax.set_title('Countries with the Most News Media Organizations')
    st.pyplot(fig)

# Plot countries with the least news media organizations as a bar chart
st.write('### Countries with the Least News Media Organizations')
with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    countries_with_least_news_media.plot(kind='bar', ax=ax)
    ax.set_xlabel('Country')
    ax.set_ylabel('Number of News Media Organizations')
    ax.set_title('Countries with the Least News Media Organizations')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

# Get top and bottom 10 websites with the highest traffic
top_10_traffic, bottom_10_traffic = get_highest_and_lowest_traffic_websites(traffic_df)

# Plot top 10 websites with the highest traffic as a horizontal bar chart
st.write('### Top 10 Websites with the Highest Traffic')
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    top_10_traffic.plot(kind='barh', ax=ax)
    ax.set_xlabel('Traffic Count')
    ax.set_ylabel('Website')
    ax.set_title('Top 10 Websites with the Highest Traffic')
    st.pyplot(fig)

# Plot bottom 10 websites with the lowest traffic as a horizontal bar chart
st.write('### Bottom 10 Websites with the Lowest Traffic')
with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom_10_traffic.plot(kind='barh', ax=ax)
    ax.set_xlabel('Traffic Count')
    ax.set_ylabel('Website')
    ax.set_title('Bottom 10 Websites with the Lowest Traffic')
    st.pyplot(fig)

# Count sentiment by website domain
sentiment_count_by_website = count_sentiment_by_website_domain(rating_df)

# Get websites with the highest count of sentiment
websites_with_highest_sentiment_count = get_websites_with_highest_sentiment_count(sentiment_count_by_website)

# Plot websites with the highest count of sentiment as a pie chart
st.write('### Websites with the Highest Count of Sentiment')
with col1:
    fig, ax = plt.subplots()
    ax.pie(websites_with_highest_sentiment_count, labels=websites_with_highest_sentiment_count.index, autopct='%1.1f%%')
    ax.set_title('Websites with the Highest Count of Sentiment')
    st.pyplot(fig)