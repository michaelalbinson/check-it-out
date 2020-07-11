from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from db.BillCache import BillCache

stemmer = PorterStemmer()
bill_cache = BillCache()
result = bill_cache.get_all_keywords()
for r in result:
    synonyms = []
    stemmed_word = stemmer.stem(r.get('KEYWORD'))
    print(stemmed_word)
    for syn in wordnet.synsets(stemmed_word):
        for lazy in syn.lemmas():
            synonyms.append(lazy.name())
    print(set(synonyms))

