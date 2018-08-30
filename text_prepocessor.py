import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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

    def tokenize(self, text):
        return text.split(" ")
    
    def convert_lower_case(self, text):
        return text.lower()

    def ignore_punctuation(self, text):
        return text.translate(None, string.punctuation)

    def ignore_stopwords(self, token_list):
        return [w for w in token_list if not w in self.stop_words]

    def fix_misspelled_words(self, token_list):
        return None

    def stemming(self, text):
        return None

    def auxillary_preprocess(self, text_with_rating):
        func_list = [self.convert_lower_case, 
                     self.ignore_punctuation,
                     self.tokenize,
                     self.ignore_stopwords]
        inp = text_with_rating[0]
        for func in func_list:
            inp = func(inp)

        return (inp, text_with_rating[1])

    def process_text(self, 
                     text_generator, 
                     correct_spell=False,
                     stem=False):
        for batch in text_generator:
            print batch
            yield map(self.auxillary_preprocess, batch)
            

if __name__ == "__main__":
    from input_reader import InputReader
    input_reader = InputReader(1, 10)
    input_dir = "/home/rohittulu/Documents/aclImdb/train/pos/"
    text_generator = input_reader.get_batches(input_dir)
    text_processor = Textpreprocessor()
    for processed_batch in text_processor.process_text(text_generator):
        print processed_batch

