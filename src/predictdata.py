import numpy as np 
import matplotlib.pyplot as plt
import csv
import gzip

def vectorized_result(j):
    e = np.zeros((3, 1))
    e[j] = 1.0
    return e

def get_test_data(home_team, away_team):
    a_x = []
    with open ("../DATA/2018/"+home_team+".csv", newline='', encoding='latin-1') as csvfile:
        rows = csv.reader(csvfile)
        next(rows)
        for row in rows:
            a_x.append(row[4])

    with open ("../DATA/2018/"+away_team+".csv", newline='', encoding='latin-1') as csvfile:
        rows = csv.reader(csvfile)
        next(rows)
        for row in rows:
            a_x.append(row[4])


    X_test=np.array(a_x, dtype=float)   
    X_test = X_test/100.0 
    Y_test=np.array([0])

    test_inputs = [np.reshape(X_test, (len(a_x), 1))] 
    test_results = [vectorized_result(y) for y in Y_test]
    test_data = list(zip(test_inputs, test_results))
    return test_data




