# coding=utf-8
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
import pandas as pd
import time

def do_svm(x_file, y_file, rate):
    start = time.time()

    x = pd.read_csv(x_file, header=None)
    y = pd.read_csv(y_file, header=None)

    # 传统的验证集，测试集的划分
    # train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=rate, random_state= 11)
    #
    # svc_model = svm.SVC(kernel= 'linear', C=1)
    # svc_model.fit(train_x, train_y)
    # result = svc_model.score(test_x, test_y)

    # 交叉验证法（cross_val_score）
    svc_model = svm.SVC(kernel= 'linear', C=1)
    result = cross_val_score(svc_model, x, y, cv=2)

    end = time.time()

    print '----------svm model leaning and show the result:', start-end, '\n', result



if __name__ =='__main__':

    x_file = '../tfidf_LDA/data/train_x.csv'
    y_file = 'data/train_y.csv'

    do_svm(x_file, y_file, rate=1/3.0)