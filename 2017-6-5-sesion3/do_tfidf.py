# coding=utf-8
from gensim import corpora,models



def to_Tfidmodle(corpus):
    tfidf = models.TfidfModel(corpus)
    tfidf.save('../2017-6-5-sesion3/data/corpus.tfidf_model')

    #输出所有的结果
    fopen = open('data/tfidf.csv', 'w')
    for doc in tfidf[corpus]:
        fopen.write(str(doc)+'\n')


if __name__ == '__main__':
    corpus_url = '../2017-6-2-sesion2/temp/vectors.mm'
    corpus = corpora.MmCorpus(corpus_url)
    to_Tfidmodle(corpus)

    #查看处理好的语料
    fopen = open('data/corpus.csv', 'w')
    for each in corpus:
        fopen.write(str(each)+'\n')

    to_Tfidmodle(corpus)
