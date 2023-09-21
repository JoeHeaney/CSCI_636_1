from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]+")

class Bigram(MRJob):
    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        for i in range(len(words)-1):
            x = words[i]
            y = words[i+1]
            z = x + "," + y
            yield z, 1

    def reducer(self, word, counts):
        total = sum(counts)
        yield word, total

if __name__ == '__main__':
    Bigram.run()