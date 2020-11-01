# -*- coding: utf-8 -*-
# -*- 役割: 日々の棋譜解析 -*-

# -*- ライブラリ -*-
import dl_kif_class as dlkf
import Game_per_Day

# -*- 処理部 -*-
# インスタンス化
dl = dlkf.DLKifClass('luc22')

# 棋譜ダウンロード
gpd = Game_per_Day.game_per_day()
dl.dl_kif(loop_num=gpd)
dl.daily_kifana_log()

# 棋譜解析
dl.kifana(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu',
          r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu2',
          loop_num=gpd)

# 実行ログ

# -*- End of file -*-
