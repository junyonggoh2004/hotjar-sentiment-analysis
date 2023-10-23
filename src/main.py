from colorama import Fore, Style

from DescriptiveStatistics import DescriptiveStatistics
from Processing.DataExtractor import DataExtractor
from Processing.DataProcessor import DataProcessor
from Processing.PowerBIColumnTransformer import PowerBIColumnTransformer
from Processing.TextNormaliser import TextNormaliser
from SentimentClassification.SentimentClassifierCore import SentimentClassifierCore
from SentenceSimilarity.SentenceSimilarityCore import SentenceSimilarityCore
from TextTagger.TextTaggerCore import TextTaggerCore
from utils import get_console_columns


class SurveyAnalysis:
    def __init__(self):
        self.start = None
        self.con = None
        self.df = None
        self.desc_df = None

    def intro(self):
        return f'''
Welcome to the HotJar Survey Analysis Project!

This programme employs natural language processing (NLP) and data analysis tools to conduct sentiment analysis on feedback from 
Amara Hotels' websites. The data originates from the HotJar Exit Synxis Surveys across all three establishments: 
ASIN (Singapore), ASRS (Sanctuary Resort Sentosa), and ABKK (Bangkok). It is crucial to acknowledge that the performance of the 
techniques used depends on factors like pipeline configurations, the choice of models, and the quantity and quality of the data provided,
especially their grammatical coherence and conjugation.

{'-'*get_console_columns()}
{self.describe_data_statistics()}
{'-'*get_console_columns()}
'''

    def describe_data_statistics(self):
        return DescriptiveStatistics(self.df).run_descriptive_statistics()

    def display_menu(self):
        self.start = input(
            '''
Techniques used:

1. POS-Tagging
2. Sentence Similarity
3. Sentiment Classification

Please select '1', '2', or '3' to begin your survey analysis journey.
Enter 'q' to exit the program at any point of time.

>>> ''')

    def run_analysis(self):
        processed_data, has_data = DataProcessor().run_processing_pipeline()
        PowerBIColumnTransformer(processed_data).run_transformer_pipeline()
        if has_data:
            print(f"{Fore.RED}NO DATA AVAILABLE{Style.RESET_ALL}")
        else:
            self.df = TextNormaliser().insert_normalised_text_column(processed_data)
            print(self.intro())
            while True:
                self.display_menu()

                if self.start == 'q':
                    break
                elif self.start == '1':
                    print(f'''
{'-'*get_console_columns()}
POS-Tagging categorises words from responses by their grammatical roles and analyses their frequency to identify the most frequently
mentioned topics.
{'-'*get_console_columns()}             
                            ''')
                    ttc = TextTaggerCore(self.df)
                    ttc.run_all_pipelines()
                elif self.start == '2':
                    print(f'''
{'-'*get_console_columns()}
Sentence Similarity evaluates a similarity score between pairs of most similar responses using a cosine similarity metric. The similarity score ranges from -1 to 1, 
where 1 indicates perfect similarity, 0 indicates no similarity and negative values indicate dissimilarity in direction. This helps to 
identify recurring themes or concerns among users by identifying responses that share common keywords or content.
{'-'*get_console_columns()}            
                            ''')
                    ssc = SentenceSimilarityCore(self.df)
                    ssc.run_all_pipelines()
                elif self.start == '3':
                    print(f'''
{'-'*get_console_columns()}

Sentiment Classification assesses and categorises the sentiment of responses by evaluating the intensity of the words used. 
The confidence level indicates how confident the model is in predicting a response's sentiment label. This helps to identify aspects of 
the hotels which receive the most praise or criticism.
{'-'*get_console_columns()}          
                            ''')
                    ssc = SentimentClassifierCore(self.df)
                    ssc.run_all_pipelines()
                else:
                    print("\nInvalid option. Please choose 1, 2, 3, or 'q'.")
                    continue

                self.con = input("\nBack to Main Menu? Press 'q' to quit: ")
                if self.con.lower() == 'q':
                    break


if __name__ == "__main__":
    DataExtractor().run_extraction_pipeline()
    SurveyAnalysis().run_analysis()
