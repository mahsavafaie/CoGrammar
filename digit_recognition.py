""" This piece of code reads data from the disk and after
preprocessing, stores data in trainig, development and test
sets. The following section make models based on logistic regression
and knn algorithms. The model is then used to predict unseen data from
the test set. Accuracy, precision, recall and F-score are calculated
at the end and the confusion matrix is printed.
""""

#PREPROCESSING

import numpy, codecs, os, pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix
from sklearn import neighbors


path = '/mnt/c/users/mahsa/Downloads/MNIST/'
files = os.listdir(path)

def get_int(b):   # CONVERTS 4 BYTES TO AN INT
    return int(codecs.encode(b, 'hex'), 16)

data_dict = {}

for file in files:
    with open (path + file ,'rb') as f:
        data = f.read()
        length = get_int(data[4:8])  # LENGTH OF THE ARRAY
        if 'labels' in file:
            category = 'labels'
            parsed = numpy.frombuffer(data, dtype=numpy.uint8, offset=8) # READ THE LABEL VALUES AS INTEGERS
            parsed = parsed.reshape(length)  # RESHAPE THE ARRAY AS [NO_OF_SAMPLES]
        elif 'images' in file:
            category = 'images'
            num_rows = get_int(data[8:12])  # NUMBER OF ROWS  (DIMENSION 1)
            num_cols = get_int(data[12:16])  # NUMBER OF COLOUMNS  (DIMENSION 2)
            parsed = numpy.frombuffer(data,dtype = numpy.uint8, offset = 16)  # READ THE PIXEL VALUES AS INTEGERS
            parsed = parsed.reshape(length,num_rows*num_cols)  # RESHAPE THE ARRAY AS [NO_OF_SAMPLES x HEIGHT x WIDTH]\
        if length == 10000:
            set = 'test'
        elif length == 60000:
            set = 'train'
        data_dict[set + '_' + category] = parsed  # SAVE THE NUMPY ARRAY TO A CORRESPONDING KEY IN DATA_DICT

train_images,train_labels,test_images,test_labels = data_dict['train_images'], data_dict['train_labels'], data_dict['test_images'] , data_dict['test_labels']

train_images,val_images,train_labels,val_labels = train_test_split(train_images, train_labels, test_size = 0.1)    # CREATE TRAIN AND VALIDATION SETS



# LOGISTIC REGRESSION MODEL AND PERFORMANCE SCORES

iterations = range(50,300,50)
acc = []

for i in range (50,300,50):
    logistic_regr = LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=i)   #SOLVER IS SET TO lbfgs TO INCREASE SPEED
    logistic_regr.fit(train_images, train_labels)
    score = logistic_regr.score(val_images, val_labels)
    print(i , "accuracy=%.2f%%" % (score*100))
    acc.append(score)

i = numpy.argmax(acc)   #GET THE INDEX OF HIGHEST ACCURACY

best_lr = LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=iterations[i])
best_lr = best_lr.fit(train_images, train_labels)
test_pred = best_lr.predict(test_images)

print("accuracy=%.2f%%" % (best_knn.score(test_images, test_labels)*100))
print(precision_recall_fscore_support(test_labels, test_pred, average='micro'))
print(confusion_matrix(test_labels, test_pred))


# KNN MODEL AND PERFORMANCE SCORES

k_values = range(1,20,2)
accuracies = []

for k in range (1,20,2):
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_images,train_labels)
    score = knn.score(val_images, val_labels)
    print("k=%d, accuracy=%.2f%%" % (k, score * 100))
    accuracies.append(score)

j = numpy.argmax(accuracies)   #GET THE INDEX OF HIGHEST ACCURACY

best_knn = neighbors.KNeighborsClassifier(k_values[i])
best_knn.fit(train_images, train_labels)
test_pred = best_knn.predict(test_images)

print("accuracy=%.2f%%" % (best_knn.score(test_images, test_labels)*100))
print(precision_recall_fscore_support(test_labels, test_pred, average='micro'))
print(confusion_matrix(test_labels, test_pred))
