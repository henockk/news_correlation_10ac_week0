import os
import unittest
import pandas as pd

class TestData(unittest.TestCase):
    def setUp(self):
        # Get the current directory
        current_dir = os.path.dirname(__file__)
        # Load the data
        data_path = os.path.join(current_dir, '..', 'dataset', 'rating.csv')
        self.data = pd.read_csv(data_path)

    def test_data_columns(self):
        # Ensure that the dataset contains the expected columns
        expected_columns = [
            'article_id', 'source_id', 'source_name', 'author', 'title',
            'description', 'url', 'url_to_image', 'published_at', 'content',
            'category', 'article', 'title_sentiment'
        ]
        actual_columns = self.data.columns.tolist()
        self.assertEqual(actual_columns, expected_columns, 
                         "Columns in the dataset do not match the expected columns")

if __name__ == '__main__':
    unittest.main()