from mrjob.job import MRJob
from mrjob.step import MRStep
import re

# Word frequency from book sorted by frequency
# File: book.txt  

# regular expression used to identify word
WORD_RE = re.compile(r"[\w]+")

class StopWords(MRJob):

    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        for w in words:
            yield w, 1

    def reducer(self, word, counts):
        group = ['and','a','of','to','it','is','in','the']
        if word.lower() not in group:
            yield word, sum(counts)


if __name__ == '__main__':
    StopWords.run()