# -*- coding: utf-8 -*-
# -*- 役割: 試作、例外処理実装 -*-

# -*- ライブラリ -*-

# -*- 処理部 -*-
# 動作チェック
print('以下の実行を行います [y/n]')

# 自身がコールする関数を調べる
try:
    test
    print('test')
except NameError:
    print('関数コールはありませんでした')

# -*- End of file -*-
