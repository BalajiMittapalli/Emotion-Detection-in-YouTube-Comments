import json
import pandas as pd
from results import YouTubeCommentsAnalyzer
from extractingcomments import YouTubeCommentsExtractor
  
class  SentimentResults():
    def __init__(self, api_key):
        self.api_key = api_key
        self.analyzer = YouTubeCommentsAnalyzer(api_key)
        self.extractor = YouTubeCommentsExtractor(api_key)
    def analyze_and_save(self, video_id):
        result = self.analyzer.get_sentiment_for_each_comment(videoID=video_id)
        self.extractor.extract_comments(video_id)
        df = pd.read_csv('youtube_comments.csv')
        df['Sentiment Type'] = result
        df.to_csv('Sentiment_final_results.csv', index=False)
        df = pd.read_csv('Sentiment_final_results.csv')
        value_counts_yearwise = df.groupby(['Published Year', 'Sentiment Type']).size().unstack(fill_value=0)
        value_counts_dict = value_counts_yearwise.to_dict()
        return value_counts_dict
