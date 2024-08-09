from django.test import TestCase

# Create your tests here.
import pandas as pd

filename="D:/articles.csv"

data=pd.read_csv("D:/articles.csv",encoding='cp1252')
print(data)
print(data.head())
print(data.isnull().sum())
print(data.tail())
data['Tonality']=data['Tonality'].fillna('Positive')
print(data.tail())
print(data.isnull().sum())


