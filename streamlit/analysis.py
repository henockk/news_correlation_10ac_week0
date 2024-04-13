import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a DataFrame.
    
    Args:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)

def count_articles_per_website(rating_df):
    """
    Count articles per website and get unique article_ids.
    
    Args:
    rating_df (pd.DataFrame): DataFrame containing ratings data.
    
    Returns:
    pd.DataFrame: DataFrame with counts of articles per website and unique article_ids.
    """
    articles_per_website = rating_df.groupby('source_name')['article_id'].agg(['count', 'nunique'])
    articles_per_website.columns = ['article_count', 'unique_article_count']
    articles_per_website_sorted = articles_per_website.sort_values(by='article_count', ascending=False)
    return articles_per_website_sorted

def get_top_and_bottom_websites(articles_per_website_sorted):
    """
    Get top and bottom 10 websites based on the number of articles.
    
    Args:
    articles_per_website_sorted (pd.DataFrame): DataFrame with articles count per website sorted.
    
    Returns:
    pd.DataFrame: DataFrames containing top 10 and bottom 10 websites.
    """
    top_10 = articles_per_website_sorted.head(10)
    bottom_10 = articles_per_website_sorted.tail(10)
    return top_10, bottom_10


def count_news_media_per_country(domains_location_df):
    """
    Count news media organizations per country.

    Args:
    domains_location_df (pd.DataFrame): DataFrame containing domain and country information.

    Returns:
    pd.Series: Series with counts of news media organizations per country.
    """
    return domains_location_df['Country'].value_counts()

def get_countries_with_most_least_news_media(news_media_per_country):
    """
    Get countries with the highest and lowest number of news media organizations.

    Args:
    news_media_per_country (pd.Series): Series with counts of news media organizations per country.

    Returns:
    pd.Series, pd.Series: Series with counts of news media organizations for countries with the most and least, respectively.
    """
    countries_with_most_news_media = news_media_per_country.head(10)
    countries_with_least_news_media = news_media_per_country.tail(10)
    return countries_with_most_news_media, countries_with_least_news_media

def get_highest_and_lowest_traffic_websites(traffic_df):
    """
    Get websites with the highest and lowest traffic.

    Args:
    traffic_df (pd.DataFrame): DataFrame containing traffic information.

    Returns:
    pd.Series, pd.Series: Series with counts of traffic for websites with the highest and lowest, respectively.
    """
    highest_traffic_websites = traffic_df.groupby('Domain')['TldRank'].count()
    highest_traffic_websites_sorted = highest_traffic_websites.sort_values(ascending=False)
    top_10 = highest_traffic_websites_sorted.head(10)
    bottom_10 = highest_traffic_websites_sorted.tail(10)
    return top_10, bottom_10

def count_sentiment_by_website_domain(rating_df):
    """
    Count sentiment by website domain.

    Args:
    rating_df (pd.DataFrame): DataFrame containing rating information.

    Returns:
    pd.Series: Series with counts of sentiment by website domain.
    """
    sentiment_count_by_website = rating_df.groupby('source_name')['title_sentiment'].value_counts()
    return sentiment_count_by_website

def get_websites_with_highest_sentiment_count(sentiment_count_by_website):
    """
    Get websites with the highest count of sentiment.

    Args:
    sentiment_count_by_website (pd.Series): Series with counts of sentiment by website domain.

    Returns:
    pd.Series: Series with websites having the highest count of sentiment.
    """
    websites_with_highest_sentiment_count = sentiment_count_by_website.groupby(level=0).nlargest(1)
    return websites_with_highest_sentiment_count