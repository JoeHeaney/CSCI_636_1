from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]+")

class Inverted(MRJob):
    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        match = re.search(r'Document (\d+): (.+)', line)
        doc= match.group(1)
        for word in words:
            yield word, "Doc " + doc
    def reducer(self, word, docs):
        total = list(docs)
        group = ['document','1','2','3',':']
        if word.lower() not in group:
            yield word, total

if __name__ == '__main__':
    Inverted.run()