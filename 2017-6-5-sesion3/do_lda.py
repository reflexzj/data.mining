from gensim import corpora, models

def to_ldaModel(corpus):

    lda = models.LdaModel(corpus, num_topics= 20)

    fopen = open('data/lda_file.csv', 'w')
    for each in lda[corpus]:
        fopen.write(str(each)+ '\n')



if __name__ == '__main__':
    corpus_url = '../2017-6-2-sesion2/temp/vectors.mm'
    corpus = corpora.MmCorpus(corpus_url)
    to_ldaModel(corpus)