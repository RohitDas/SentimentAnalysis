import pickle

class BagOfWordsGenerator(object):
    """
        This class create the bag of words list that will be used later 
        to represent a document.
    """
    def __init__(self, outfile):
        self.outfile = outfile

    def calculate(self,
                  batch_generator):

        bow = set()
        with open(self.outfile, "w") as fp:
            for idx, batch in enumerate(batch_generator):
                if idx % 10 == 0:
                    print("Batches read:" + str(idx))
                for (tokens, rank) in batch:
                    bow.update(tokens)
            for token in bow:
                fp.write(token)
                fp.write("\n")
    

if __name__ == "__main__":
    bag_of_words_generator = BagOfWordsGenerator("bow.txt")
    from input_reader import InputReader
    from text_preprocessor import Textpreprocessor
    input_dir = "/home/rohittulu/Documents/aclImdb/train/pos/" 
    input_reader = InputReader(10,-1)
    x = input_reader.get_batches(input_dir)
    text_preprocessor = Textpreprocessor()
    batch_generator = text_preprocessor.process_text(x)
    bag_of_words_generator.calculate(batch_generator)
    print("BOW CREATED")
