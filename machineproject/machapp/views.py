from django.shortcuts import render
import pandas as pd

# Create your views here.
def loading_dataset(request):
    filename="D:/articles.csv"

    data=pd.read_csv("D:/articles.csv",encoding='cp1252')
    print(data)
    print(data.head())
    print(data.isnull().sum())
    print(data.tail())
    data['Tonality']=data['Tonality'].fillna('Positive')
    print(data.tail())
    print(data.isnull().sum())