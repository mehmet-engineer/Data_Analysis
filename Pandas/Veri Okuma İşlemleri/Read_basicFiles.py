import pandas as pd

dataFrame1 = pd.read_csv("sample.csv")
dataFrame2 = pd.read_json("sample.json")

# "pip install xlrd" excel dosyalarını okumak için...
dataFrame3 = pd.read_excel("sample.xlsx")  # encoding="UTF-8" parametresi eklenebilir.

# "pip install pysqlite3" database dosyalarını okumak için...
import sqlite3
connection = sqlite3.connect("sample.db")
dataFrame4 = pd.read_sql_query("SELECT * FROM Tablom", connection)

print(dataFrame3)