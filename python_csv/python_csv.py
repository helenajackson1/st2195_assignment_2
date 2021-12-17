# import pandas and beautiful soup 

import pandas as pd
import requests
from bs4 import BeautifulSoup


#read the webpage 
html_text = requests.get("https://en.m.wikipedia.org/wiki/Comma-separated_values").text

#use beautifulsoup to find and parse the table
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('table', class_= "wikitable")

#read and format the table
df2 = pd.read_html(str(table))
df2 = pd.concat(df2)
print(df2)

#export to csv
df2.to_csv (r'C:\Users\norrs\OneDrive\Documents\UNIVERSITY\Python Scripts\cars_example.csv', index = False, header=True)
