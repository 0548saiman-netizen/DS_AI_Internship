# Task 1

import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/0548s/OneDrive/Desktop/database/internship.db")

df = pd.read_sql_query("SELECT * FROM interns",conn)
df = pd.read_sql_query("SELECT name, track FROM interns",conn)

print(df)

