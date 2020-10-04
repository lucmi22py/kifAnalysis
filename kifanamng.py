import dl_kif_class as dlkf
# import kif_handle as kh
import kif_db as kdb

# kif = kh.KifHandle()
# kif.save_kif('_ana')

# インスタンス化
dl = dlkf.DLKifClass('luc22')
siken = kdb.KifDataBase('luc22')

karioki = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\studykif'
dst_path = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu2'
src_path = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu'
loop_num = 50
# 注意！下記パラメータは変更の可能性有り
tac = r'嬉野流'
sente_path = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\vskif\対' + str(tac) + r'\sente'
gote_path = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\vskif\対' + str(tac) + r'\gote'

# 動作チェック
# ファイルがなかったら作っておく。
# 対象戦型は意図通りか？

# '''
# kifのDL
# dl.dl_kif(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu\\')
# kif解析
dl.kifana(src_path, dst_path, loop_num)
# '''

'''
# 戦型抽出
siken.tactics(karioki, dst_path, tac)
'''

# 先後分類
# siken.separate_sengo(sente_path, gote_path, karioki)
