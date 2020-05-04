# 月1で解析結果をまとめる
import kif_handle
import os


# クラス表現ver.
class MonthAnalysis:
    def __init__(self, value):
        self.dst_path = ''
        self.dst_file = ''
        self.dst_file_list = []
        self.won_sente = value
        self.won_gote = value
        self.lose_sente = value
        self.lose_gote = value
        self.time_over_lose_sente = value
        self.time_over_lose_gote = value

    def select_kif(self):
        self.dst_file_list = kif_handle.file_rec()

    def kif_move(self):
        print('移動先フォルダの絶対パスを入力してください')
        dst_path = str(input())
        self.dst_file = select_kif()
        for i, item in enumerate(self.dst_file):
            kif_handle.move_glob(dst_path, item)

    def game_type(self):
        self.dst_path
        if notdef in self.dst_path:
            print('ディレクトリがありません。ディレクトリを作成します。')
            new_dir_path_10min = self.dst_path + '10min'
            new_dir_path_3min = self.dst_path + '3min'
            os.makedirs(new_dir_path_10min/new_dir_path_3min)
            self.game_type()

    def winlose_ana(self):
        for i, item in enumerate(self.dst_file):
            with open(item, 'r') as f:
                i_line = f.read()
                f.close()
                if '先手：luc22' in i_line and '先手の勝ち' in i_line:
                    self.won_sente += 1
                elif '先手：luc22' in i_line and '後手の勝ち' in i_line:
                    self.lose_sente += 1
                    if '時間切れにより' in i_line:
                        self.time_over_lose_sente += 1
                elif '後手：luc22' in i_line and '後手の勝ち' in i_line:
                    self.won_gote += 1
                elif '後手：luc22' in i_line and '先手の勝ち' in i_line:
                    self.lose_gote += 1
                    if '時間切れにより' in i_line:
                        self.time_over_lose_gote += 1

    # 戦型勝敗分析
    # 棋譜を月別ファイルに移動してから実行してください！
    def tactics_ana(self):
        for i, item in enumerate(self.dst_file):
            with open(item, 'r') as f:
                i_line = f.read()
                f.close()
                if '四間飛車' in i_line:
                    kif_move()
                if '嬉野流' in i_line:
                    kif_move()


# 対象ファイル抽出確認
def select_kif():
    dst_file_list = kif_handle.file_rec()
    print('以下のファイルが移動対象です')
    print(dst_file_list)
    return dst_file_list


# 棋譜移動
def kif_move():
    print('移動先フォルダの絶対パスを入力してください')
    dst_path = str(input())
    dst_file = select_kif()
    for i, item in enumerate(dst_file):
        kif_handle.move_glob(dst_path, item)


# 先後勝敗分析
def winlose_ana():
    dst_file = kif_handle.file_rec()
    won_sente = 0
    won_gote = 0
    lose_sente = 0
    lose_gote = 0
    time_over_lose_sente = 0
    time_over_lose_gote = 0

    for i, item in enumerate(dst_file):
        with open(item, 'r') as f:
            i_line = f.read()
            f.close()
            if '先手：luc22' in i_line and '先手の勝ち' in i_line:
                won_sente += 1
            elif '先手：luc22' in i_line and '後手の勝ち' in i_line:
                lose_sente += 1
                if '時間切れにより' in i_line:
                    time_over_lose_sente += 1
            elif '後手：luc22' in i_line and '後手の勝ち' in i_line:
                won_gote += 1
            elif '後手：luc22' in i_line and '先手の勝ち' in i_line:
                lose_gote += 1
                if '時間切れにより' in i_line:
                    time_over_lose_gote += 1

    print('先手番勝敗: ' + str(won_sente) + '勝' + str(lose_sente) + '敗' + ' (' + str(won_sente/(won_sente + lose_sente)) + ')')
    print('先手切れ負け: ' + str(time_over_lose_sente) + '回 (' + str(float(time_over_lose_sente/lose_sente)) + ')')
    print('後手番勝敗: ' + str(won_gote) + '勝' + str(lose_gote) + '敗' + ' (' + str(won_gote/(won_gote + lose_gote)) + ')')
    print('後手切れ負け: ' + str(time_over_lose_gote) + '回 (' + str(float(time_over_lose_gote/lose_gote)) + ')')


# 悪手率分析

########################
# 月一実行のメイン関数 #
########################
print('実行内容を指定してください\n'
      '！注意！通常の月次処理をする際は0番を選択して下さい(1番以降が順次実行されます)'
      '0: 通常月次処理(1～3番)\n'
      '1: 対象ファイル抽出確認\n'
      '2: 棋譜移動\n'
      '3: 先後勝敗分析')
num = int(input())
if num == 0:
    select_kif()
    kif_move()
    winlose_ana()
elif num == 1:
    select_kif()
elif num == 2:
    kif_move()
elif num == 3:
    winlose_ana()
else:
    print('その操作は規定されていません')
