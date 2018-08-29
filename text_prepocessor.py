import nltk
import nltk.corpus import stopwords
import nltk.tokenize import word_tokenize
import string

class Textpreprocessor(object):
    def __init__(self):
        self.init_stopwords()

    def init_stopwords(self):
        try:
            self.stop_words = set(stopwords.words("english"))
        except:
            nltk.download("stopwords")
            self.stop_words = set(stopwords.words("english"))

    def tokenize(self, text)
        return text.split(" ")
    
    def convert_lower_case(self, text):
        return text.lower()

    def ignore_punctuation(self, text):
        return text.translate(None, string.punctuation)

    def ignore_stopwords(self, token_list):
        return [w for w in tokens if not w in stop_words]

    def fix_misspelled_words(self, token_list):
        return None

    def stemming(self, text):
        return None

    def process_text(self, 
                     text_generator, 
                     correct_spell=False,
                     stem=False):
        for batch in text_generator:
            #convert to lower case
            #ignore punctuation
            #remove stop_words
            #fix misspelled words
            #Stemming
            pass

