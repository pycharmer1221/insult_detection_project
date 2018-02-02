from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn import metrics, ensemble, linear_model, svm
from numpy import log, ones, array, zeros, mean, std, repeat
import numpy as np
import scipy.sparse as sp
import re
import csv
from time import time



DIR_PATH = ""

TRAIN_FILE      = DIR_PATH + "train.csv"
BADWORDS_FILE   = DIR_PATH + "badwords.txt"              # attached with submission  




def normalize(f):
    f = [x.lower() for x in f]
    f = [x.replace("\\n"," ") for x in f]        
    f = [x.replace("\\t"," ") for x in f]        
    f = [x.replace("\\xa0"," ") for x in f]
    f = [x.replace("\\xc2"," ") for x in f]

    #f = [x.replace(","," ").replace("."," ").replace(" ", "  ") for x in f]
    #f = [x.replace("  "," ") for x in f]

    f = [x.replace(" u "," you ") for x in f]
    f = [x.replace(" em "," them ") for x in f]
    f = [x.replace(" da "," the ") for x in f]
    f = [x.replace(" yo "," you ") for x in f]
    f = [x.replace(" ur "," you ") for x in f]
    #f = [x.replace(" ur "," your ") for x in f]
    #f = [x.replace(" ur "," you're ") for x in f]
    
    f = [x.replace("won't", "will not") for x in f]
    f = [x.replace("can't", "cannot") for x in f]
    f = [x.replace("i'm", "i am") for x in f]
    f = [x.replace(" im ", " i am ") for x in f]
    f = [x.replace("ain't", "is not") for x in f]
    f = [x.replace("'ll", " will") for x in f]
    f = [x.replace("'t", " not") for x in f]
    f = [x.replace("'ve", " have") for x in f]
    f = [x.replace("'s", " is") for x in f]
    f = [x.replace("'re", " are") for x in f]
    f = [x.replace("'d", " would") for x in f]

    #f = [x.replace("outta", "out of") for x in f]

    bwMap = loadBW()
    for key, value in bwMap.items():
        kpad = " " + key + " "
        vpad = " " + value + " "
        f = [x.replace(kpad, vpad) for x in f]
        
    # stemming    
    f = [re.subn("ies( |$)", "y ", x)[0].strip() for x in f]
    f = [re.subn("s( |$)", " ", x)[0].strip() for x in f]
    f = [re.subn("ing( |$)", " ", x)[0].strip() for x in f]
        
    f = [re.subn(" [*$%&#@][*$%&#@]+"," xexp ", x)[0].strip() for x in f]
    f = [re.subn(" [0-9]+ "," DD ", x)[0].strip() for x in f]
    return f



def loadBW():
    f = open(BADWORDS_FILE, "r")
    bwMap = dict()
    for line in f:
        sp = line.strip().lower().split(",")
        if len(sp) == 2:
            bwMap[sp[0].strip()] = sp[1].strip()
    return bwMap



def readCsv(fname, skipFirst=True, delimiter = ","):
    reader = csv.reader(open(fname),delimiter=delimiter)
    
    rows = []
    count = 1
    for row in reader:
        if not skipFirst or count > 1:      
            rows.append(row)
        count += 1
    return rows










train_data = readCsv(TRAIN_FILE)
train  = [x[2] for x in train_data]


f = normalize(train)







print(train[166])
#print(normalize(train[166]))
#print('\n\n\n\n\n\n')
print(f[166])





#vectorizer = CountVectorizer(max_n=mx,min_n=mn,binary=True)
#X_train = vectorizer.fit_transform(f)


#print(X_train)





















