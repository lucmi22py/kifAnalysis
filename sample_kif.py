# -*- coding: utf-8 -*-
# -*- 役割: 試作、例外処理実装 -*-

# -*- ライブラリ -*-
import dl_kif_class as dlkf
import kif_db as kdb
from webdriver_manager.utils import chrome_version

# -*- 処理部 -*-
# 動作チェック
print('以下の実行を行います [y/n]')
print(chrome_version())

# 自身がコールする関数を調べる
try:
    test
    print('test')
except NameError:
    print('関数コールはありませんでした')

# -*- End of file -*-
