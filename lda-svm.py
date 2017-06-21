# coding=utf-8
from tfidf_LDA import do_lda
from svm_model import do_svm
from gensim import corpora

if __name__ == '__main__':

    #给出LDA主题模型
    corpus_url = 'build_corpus/temp/vectors.mm'

    topic_num = 25

    corpus = corpora.MmCorpus(corpus_url)
    do_lda.to_ldaModel(corpus, topic_num)

    #投入svm模型中去，返回结果
    x_file = 'tfidf_LDA/data/train_x.csv'
    y_file = 'svm_model/data/train_y.csv'

    rate = 1/4.0
    do_svm.do_svm(x_file, y_file, rate)