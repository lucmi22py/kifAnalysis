import xlrd
import numpy as np
import pandas as pd
import time
bef_t = time.time()

df = pd.read_excel(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\記録\3_tetsume_handbook_record.xlsx')
df.to_csv(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\記録\csv\3_tetsume_handbook_record.csv', index=False, encoding='utf_8_sig')

#csv_rawdata = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\記録\csv\3_tetsume_handbook_record.csv'
#df = pd.read_csv(csv_rawdata)

aft_t = time.time()
elapsed_time = aft_t - bef_t
print(f"経過時間:{elapsed_time}" + 'sec') # 単位はsec
