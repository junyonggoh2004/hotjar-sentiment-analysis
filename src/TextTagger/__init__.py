'''
TextTagger.py
- `__init__(self)`: Initialises the `TextTagger` class.
- `load_configure_nltk(self)`: Loads and configures the NLTK dictionary. Removes certain keys from the dictionary.
- `prepare_tag_word_df(self, df)`: Prepares a DataFrame for storing tagged words. Inserts a "clean_text" column from the input DataFrame `df`.
- `populate_df_by_tag(self, df)`: Populates the DataFrame with words categorised by their part-of-speech tags (noun, verb, adjective, adverb).
- `run_tagger_pipeline(self, df)`: Runs the entire text tagging pipeline, including loading NLTK, preparing the DataFrame, and populating it with tagged words.

TextTaggerSimplifier.py
- `__init__(self)`: Initialises the `TextTaggerSimplifier` class.
- `simplify_pos_words(self, hotel, df)`: Simplifies part-of-speech words into categories such as nouns, verbs, adjectives, and adverbs.
- `top_n_words(self, words_dict, word_category, n, hotel)`: Retrieves the top `n` most common words for a given word category (noun, verb, adjective, adverb) and hotel outlet.
- `run_top_n_words(self, df)`: Runs the process of simplifying and retrieving the top n words based on user input for word category and hotel outlet.

TextTaggerCore.py
- `__init__(self, df)`: Initialises the `TextTaggerCore` class with an input DataFrame `df`.
- `run_all_pipelines(self)`: Runs all the pipelines for text tagging and simplification.
'''
