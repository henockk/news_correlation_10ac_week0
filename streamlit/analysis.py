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