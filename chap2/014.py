"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
014
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""
N = int(input(">>"))

"""
with open("hightemp.txt","r") as f: 
    for i,name in enumerate(f.readlines()): 
        if i<N: print(name,end="")
"""

with open("hightemp.txt","r") as f: 
    l = f.readlines()
    for i in enumerate(l[:N:]): print(i,end="")

