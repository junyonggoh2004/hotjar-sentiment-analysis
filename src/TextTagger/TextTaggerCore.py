from TextTagger.TextTagger import TextTagger
from TextTagger.TextTaggerSimplifier import TextTaggerSimplifier


class TextTaggerCore():

    def __init__(self, df):
        self.df = df
        self.text_tagger = TextTagger()
        self.text_tagger_simplifier = TextTaggerSimplifier()

    def run_all_pipelines(self):
        self.df = self.text_tagger.run_tagger_pipeline(self.df)
        self.text_tagger_simplifier.run_top_n_words(self.df)
