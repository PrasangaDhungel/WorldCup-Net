import numpy as np 
import matplotlib.pyplot as plt
import csv
import gzip

def get_half_data():
    ini=True
    a_y=[]

    with open("../DATA/2014/matches.csv", newline='', encoding='latin-1') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            a_x=[]
            with open("../DATA/2014/"+str(row['home team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])

            with open("../DATA/2014/"+str(row['away team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])
            
            a_x=np.array(a_x, dtype=float)    
                        
            if row["Home Team Goals"]>row["Away Team Goals"]:
                a_y.append(2)
            
            elif row["Home Team Goals"]==row["Away Team Goals"]:
                a_y.append(1)
            
            else:
                a_y.append(0)

            if ini==True:
                X_train=a_x
                ini=False
            
            else:
                X_train=np.vstack((X_train,a_x))

    with open("../DATA/2010/matches.csv", newline='', encoding='latin-1') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            a_x=[]
            with open("../DATA/2010/"+str(row['home team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])

            with open("../DATA/2010/"+str(row['away team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])
            
            a_x=np.array(a_x, dtype=float)    
            
            if row["Home Team Goals"]>row["Away Team Goals"]:
                a_y.append(2)
            
            elif row["Home Team Goals"]==row["Away Team Goals"]:
                a_y.append(1)

            else:
                a_y.append(0)

            X_train=np.vstack((X_train,a_x))
    
    Y_train = np.array(a_y)
    X_train = X_train/100.0
    return X_train, Y_train


def get_data():
    ini=True
    a_y=[]

    with open("../DATA/2014/matches.csv", newline='', encoding='latin-1') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            a_x=[]
            with open("../DATA/2014/"+str(row['home team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])

            with open("../DATA/2014/"+str(row['away team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])
            
            a_x=np.array(a_x, dtype=float)    
                        
            if row["Home Team Goals"]>row["Away Team Goals"]:
                a_y.append(2)
            
            elif row["Home Team Goals"]==row["Away Team Goals"]:
                a_y.append(1)
            
            else:
                a_y.append(0)

            if ini==True:
                X_train=a_x
                ini=False
            
            else:
                X_train=np.vstack((X_train,a_x))

    with open("../DATA/2010/matches.csv", newline='', encoding='latin-1') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            a_x=[]
            with open("../DATA/2010/"+str(row['home team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])

            with open("../DATA/2010/"+str(row['away team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])
            
            a_x=np.array(a_x, dtype=float)    
            
            if row["Home Team Goals"]>row["Away Team Goals"]:
                a_y.append(2)
            
            elif row["Home Team Goals"]==row["Away Team Goals"]:
                a_y.append(1)

            else:
                a_y.append(0)

            X_train=np.vstack((X_train,a_x))

    with open("../DATA/2010/matches.csv", newline='', encoding='latin-1') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            a_x=[]
            with open("../DATA/2010/"+str(row['away team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])

            with open("../DATA/2010/"+str(row['home team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])
            
            a_x=np.array(a_x, dtype=float)    
            
            if row["Home Team Goals"]>row["Away Team Goals"]:
                a_y.append(0)
            
            elif row["Home Team Goals"]==row["Away Team Goals"]:
                a_y.append(1)

            else:
                a_y.append(0)

            X_train=np.vstack((X_train,a_x))
    
    with open("../DATA/2014/matches.csv", newline='', encoding='latin-1') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            a_x=[]
            with open("../DATA/2014/"+str(row['away team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])

            with open("../DATA/2014/"+str(row['home team name'])+".csv", newline='', encoding='latin-1') as csvfile1:
                    rows=csv.reader(csvfile1)
                    next(rows)
                    for row1 in rows:
                        a_x.append(row1[4])
            
            a_x=np.array(a_x, dtype=float)    
            
            if row["Home Team Goals"]>row["Away Team Goals"]:
                a_y.append(0)
            
            elif row["Home Team Goals"]==row["Away Team Goals"]:
                a_y.append(1)

            else:
                a_y.append(0)

            X_train=np.vstack((X_train,a_x))

    Y_train = np.array(a_y)
    X_train = X_train/100.0
    return X_train, Y_train

def vectorized_result(j):
    e = np.zeros((3, 1))
    e[j] = 1.0
    return e

def load_data_wrapper():
    tx, ty = get_data()
    training_inputs = [np.reshape(x, (tx.shape[1], 1)) for x in tx]
    training_results = [vectorized_result(y) for y in ty]
    training_data = list(zip(training_inputs, training_results))
    return training_data

def load_half_data_wrapper():
    tx, ty = get_half_data()
    training_inputs = [np.reshape(x, (tx.shape[1], 1)) for x in tx]
    training_results = [vectorized_result(y) for y in ty]
    training_data = list(zip(training_inputs, training_results))
    return training_data