"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
016
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ
"""
N = int(input(">>"))

with open("hightemp.txt","r") as f: 
    l = f.readlines()   # ファイル全体を1行ずつリストに格納
    n = 0
    while n < len(l):
        with open("hightemp_split{}.txt".format(n),"w") as f: f.write("".join(l[n:n+N]))
        n+=N

