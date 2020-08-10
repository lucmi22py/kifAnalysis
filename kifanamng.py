#import dl_kif_class as dlkf
import kif_handle as kh
import kif_db as kdb

#dl = dlkf.DLKifClass()
#dl.dl_kif()

#kif = kh.KifHandle()
#kif.save_kif('_ana')

# インスタンス化
siken = kdb.KifDataBase('luc22')
karioki = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\studykif'
dst_path = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu2'
# 注意！下記パラメータは変更の可能性有り
tac = r'嬉野流'
sente_path = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\vskif\対' + str(tac) + r'\sente'
gote_path = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\vskif\対' + str(tac) + r'\gote'

# 動作チェック
# ファイルがなかったら作っておく。
# 対象戦型は意図通りか？

# 戦型抽出
siken.tactics(karioki, dst_path, tac)

# 先後分類
siken.sep_sengo(sente_path, gote_path, karioki)
