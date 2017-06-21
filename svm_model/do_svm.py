from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import time

def do_svm(x_file, y_file, rate):
    start = time.time()

    x = pd.read_csv(x_file, header=None)
    y = pd.read_csv(y_file, header=None)

    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=rate, random_state= 11)

    svc_model = svm.SVC()
    svc_model.fit(train_x, train_y)
    result = svc_model.score(test_x, test_y)

    end = time.time()

    print '----------svm model leaning and show the result:', start-end, '\n', result



if __name__ =='__main__':

    x_file = '../tfidf_LDA/data/train_x.csv'
    y_file = 'data/train_y.csv'

    do_svm(x_file, y_file, rate=1/4.0)