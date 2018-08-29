import os, sys
import re

class InputReader(object):
    """
        This class is custom made for the BoW model.
    """
    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.split_re = re.compile(r'<br /><br />')
        self.rating_re = re.compile(r'[\w/]+_(\d+).\w*')

    def get_fnames(self, input_dir):
        """
            It takes an INPUT_DIR and returns all the files in the directories.
        """
        if not os.path.exists(input_dir):
            raise Exception("Error! Invalid input dir")
        return os.listdir(input_dir)

    def read_file(self, f_path):
        """
            Reads the review and returns (review, rating).
        """
        with open(f_path, "r") as fp:
            try:
                content = "".join(self.split_re.split(fp.read()))
                rating = int(self.rating_re.match(f_path).group(1))
            except Exception as e:
                print "Warning!! probable wrong file name: {}".format(f_path)
        return content, rating

    def is_batch_limit_reached(self, n):
        return (n+1) % self.batch_size

    def get_batches(self, input_dir):
        files = self.get_fnames(input_dir)
        full_paths = [os.path.join(input_dir, fn) for fn in files]
        for full_path in full_paths:
            batch = list()
            content, rating = self.read_file(full_path)
            batch.append((content, rating))
            
            #Check if batch limit reached.
            if self.is_batch_limit_reached(len(batch)):
                yield batch
                batch = list()


if __name__ == "__main__":
    input_reader = InputReader(10)
    input_dir = "/home/rohittulu/Documents/aclImdb/train/pos2/"
    for batch in input_reader.get_batches(input_dir):
        print batch
