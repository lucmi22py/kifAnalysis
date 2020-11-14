#import pandas as pd
#import numpy as np
#import plotly
#import missingno as msno
#import sqlite3

# サードパーティーライブラリ
import sys
import glob
import shutil

'''
file_dir = r'huga'
file_name = r'hoge'
df = pd.read_csv(file_dir + file_name)
db_name = r'kif_db.db'
conn = sqlite3.connect(file_dir + db_name)
df.to_sql('kif_class', conn, if_exists='replace')
c = conn.cursor()
query = 'SELECT * FROM kif_class'
conn.close()
'''


class KifDataBase:
    g_src_path = ''
    g_dst_path = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def tactics(cls, src_path, dst_path, tactics_name):
        dst_list = glob.glob(dst_path + r'\*.kif')
        list_count = len(dst_list)
        for num in range(list_count):
            file = dst_list[num]
            with open(file) as f:
                line = f.readlines()
                f.close()
                for num_line in range(len(line)):
                    if tactics_name in line[num_line]:
                        if '右四間飛車' in line[num_line]:
                            #print('右四間飛車だったので、コピーしません: ' + file)
                            break
                        try:
                            shutil.copy2(file, src_path)
                            #print('copy完了：' + file)
                        except SyntaxError:
                            print("Syntax Error !")

    def separate_sengo(self, sente_src_path, gote_src_path, dst_path):
        sengo_list = glob.glob(dst_path + r'\*.kif')
        list_count = len(sengo_list)
        sente = '先手：' + self.name
        gote = '後手：' + self.name

        print('対象ファイル： ' + str(list_count) + '局')
        if list_count == 0:
            print('分類対象ファイルが0件のようです。設定を見直してください')
            sys.exit(0)
        for num in range(list_count):
            file = sengo_list[num]
            with open(file) as f:
                line = f.readlines()
                f.close()
                for i in range(16):
                    if sente in line[i]:
                        shutil.move(file, sente_src_path)
                        #print(sente_src_path + 'へ移動しました')
                    elif gote in line[i]:
                        shutil.move(file, gote_src_path)
                        #print(gote_src_path + 'へ移動しました')
