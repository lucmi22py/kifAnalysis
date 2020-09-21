# -*- coding: utf-8 -*-
# -*- 役割: 試作、例外処理実装 -*-

# -*- ライブラリ -*-
import dl_kif_class as dlkf
import kif_db as kdb
from webdriver_manager.utils import chrome_version
from selenium import webdriver
import datetime

# -*- 処理部 -*-
# 動作チェック
print('以下の実行を行います [y/n]')

# chromeとchromedriverのバージョンチェック
chrome_ver = str(chrome_version())
chromedriver_ver = str('85.0.418')
if chromedriver_ver == chrome_ver:
    ok = str('バージョンチェック問題なし')
    print(ok)
else:
    ng = str('バージョンが違います')
    print(ng)
    dt_now = datetime.datetime.now()
    path_w = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\errorlog.txt'
    with open(path_w, mode='w') as f:
        f.write('///バージョンチェック///' + '\n' +
                'check date: \t\t' + str(dt_now) + '\n' +
                'chrome version: \t' + chrome_ver + '\n' +
                'chromedriver version: \t' + chromedriver_ver + '\n' +
                'result: \t\t' + ng + '\n')

# 自身がコールする関数を調べる
try:
    test
    print('test')
except NameError:
    print('関数コールはありませんでした')

# -*- End of file -*-
