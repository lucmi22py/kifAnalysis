# 月1で解析結果をまとめる
import kif_handle


# 対象ファイル抽出
dat_file = kif_handle.file_rec()
print("以下dat_file内容")
print(dat_file)

# 棋譜移動
print('移動先フォルダの絶対パスを入力してください')
dst_path = str(input())
for i, item in enumerate(dat_file):
    kif_handle.move_glob(dst_path, item)

# 勝敗分析

# 戦型分析

# 悪手率分析
