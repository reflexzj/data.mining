# coding=utf-8
from tfidf_LDA import do_lda
from svm_model import do_svm
from gensim import corpora

if __name__ == '__main__':
    '''
        期间所有的中间文件，存储在data_mining_learning/data下
    '''

    # 给出LDA主题模型，自己定义LDA的主题数目
    corpus_url = 'build_corpus/temp/vectors.mm'

    topic_num = 20

    corpus = corpora.MmCorpus(corpus_url)
    do_lda.to_ldaModel(corpus, topic_num)

    # 投入svm模型中去（LDA的主题分布函数，则为SVM模型的属性）
    x_file = 'data/train_x.csv'
    y_file = 'data/train_y.csv'

    rate = 1/4.0
    do_svm.do_svm(x_file, y_file, rate)