import pandas as pd
import numpy as np
import plotly
import missingno as msno
import sqlite3

file_dir = r'huga'
file_name = r'hoge'
df = pd.read_csv(file_dir + file_name)
db_name = r'kif_db.db'
conn = sqlite3.connect(file_dir + db_name)
df.to_sql('kif_class', conn, if_exists='replace')
c = conn.cursor()
query = 'SELECT * FROM kif_class'
conn.close()
