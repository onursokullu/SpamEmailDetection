# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:57:19 2019

@author: ASUS
"""
import tkinter as tk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


df = pd.read_csv("spam.csv")
df.loc[df["Category"] == 'ham',"Category",] =1
df.loc[df["Category"] == 'spam',"Category",] =0

x= df["Message"]
y=df["Category"]

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2,train_size=0.8, random_state=4)


def onClick():
    input = tBox.get("1.0",tk.END)
    testInput = pd.Series(input)
    #vectorizing the test training data and test input
    tfvec = TfidfVectorizer(analyzer='word', lowercase = True)
    xTrainFeat = tfvec.fit_transform(xTrain)
    xTestFeat = tfvec.transform(testInput)
    #print(xTestFeat.toarray())
    
    #naive bayes implementing
    yTrainToInt = yTrain.astype('int')
    classifiermodel = MultinomialNB()
    classifiermodel.fit(xTrainFeat,yTrainToInt)
    predResultNb = classifiermodel.predict(xTestFeat)
    if predResultNb==1:
        label = tk.Label(text="ham",fg="green", font=("Open Sans","30","bold") )
        label.pack()
    elif predResultNb==0:
        label = tk.Label(text="spam",fg="red", font=("Open Sans","30","bold") )
        label.pack()
    #print(predResultNb)
    
    
    
    
#some interface codes
top = tk.Tk()

top.title("spam email detection")
top.geometry("550x550+320+100")

message = tk.Label(text=" Spam Email Detector",fg="blue", font=("Open Sans","30","bold") )
message.pack()

tBox = tk.Text(height = 8, width = 400)
tBox.pack()

button = tk.Button(top,text = "Find it out", command = onClick)
button.pack() 

top.mainloop()