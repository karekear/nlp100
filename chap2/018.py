"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
018
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

with open("hightemp.txt","r")as f:
    l = f.readlines()   # とりあえずファイルをリストに
    for i,name in enumerate(l): l[i] = name.replace("\n","").split("\t")
    l = sorted(l,key=lambda x:x[2])
    for i in l: print("\t".join(i))