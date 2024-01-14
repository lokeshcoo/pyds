import matplotlib.pyplot as plt                                                 #Importing matplotlib to plot and analyse data.
import pandas as pd
import plotly.express as px                                                  
from pandas import read_csv                                                 
import yfinance as yf    
df=df.load_dataset(r"C:\Users\ASUS\Desktop\major_project\code")
ticker = input("ENTER THE STOCK WHOSE PREDICTION YOU WANT : ") #taking stock name from the user. e.g.TCS
df = yf.download(ticker+'.NS', start='2017-01-01' , end='2022-07-30') #using yf.download() downloading historic data for a stock for previous 5 years.
print(df.tail())