'''
SentenceSimilarity.py
- `__init__(self)`: Initialises the `SentenceSimilarity` class with configuration options and variables.
- `compute_embeddings_and_similarity(self, hotel, df)`: Computes embeddings and calculates sentence similarity for the specified hotel's responses.
- `display_cos_sim_matrix(self)`: Displays the cosine similarity matrix.
- `create_sentence_similarity_df(self)`: Creates a DataFrame containing information about sentence similarity between responses.
- `print_sentence_similarity_df(self, hotel, n)`: Prints the top `n` most similar responses for the specified hotel.
- `run_sentence_similarity(self, df)`: Runs the entire sentence similarity analysis process, including input collection and displaying results.

SentenceSimilarityCore.py
- `__init__(self, df)`: Initialises the `SentenceSimilarityCore` class with an input DataFrame `df`.
- `run_all_pipelines(self)`: Runs all the pipelines for sentence similarity analysis.
'''