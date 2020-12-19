# -*- coding: utf-8 -*-
# -*- 役割: 日々の棋譜解析 -*-

# -*- ライブラリ -*-
import dl_kif_class as dlkf
import Game_per_Day
import glob

# -*- 処理部 -*-
# インスタンス化
dl = dlkf.DLKifClass('luc22')
dl2 = dlkf.KifHandle('luc22')

# 棋譜ダウンロード
gpd = Game_per_Day.game_per_day()
dl.dl_kif(loop_num=gpd)
dl.daily_kifana_dllog()

# 日々の棋譜解析
dl2.mojicheck(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu')
dl2.mojicheck()
dl2.kifana(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu',
           loop_num=gpd)

# 余り分の棋譜解析
kif_list = glob.glob(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu1101\*.kif')
nkif = len(kif_list)
dl2.kifana(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu1101',
           nkif)

# -*- End of file -*-
