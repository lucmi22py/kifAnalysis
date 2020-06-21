import os
import kif_handle
copy = './kifAnalysis/dl.kif'
dest = './kifAnalysis/dl.kif'
os.rename(copy, dest)


# kifファイルの移動
kif_handle.kif_classify()

# 改行の削除
# gllib化すべき？


# 評価値抽出


# 一局評価値グラフ化


# 着手前後の評価値変化 手数x 前の手との差y
