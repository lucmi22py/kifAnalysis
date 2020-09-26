# -*- coding: utf-8 -*-
# -*- 役割: google chrome及びchromedriverのバージョンチェック -*-

# -*- ライブラリ -*-
from webdriver_manager.utils import chrome_version
from selenium import webdriver
import datetime

# -*- 処理部 -*-
chrome_ver = str(chrome_version())
chromedriver_ver = str('85.0.4183')
if chromedriver_ver == chrome_ver:
    ok = str('バージョンチェック問題なし')
    state = ok
else:
    ng = str('バージョンが違います')
    state = ng

dt_now = datetime.datetime.now()
path_w = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\errorlog.txt'
with open(path_w, mode='w') as f:
    f.write('///バージョンチェック///' + '\n' +
            'check date: \t\t' + str(dt_now) + '\n' +
            'chrome version: \t' + chrome_ver + '\n' +
            'chromedriver version: \t' + chromedriver_ver + '\n' +
            'result: \t\t' + state + '\n')
# -*- End of file -*-
