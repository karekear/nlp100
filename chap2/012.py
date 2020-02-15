"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
012
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""
with open("col1.txt","w") as f1: f1.write("")
with open("col2.txt","w") as f2: f2.write("")

with open("hightemp.txt","r") as f:
    for s in f:
        l = s.split("\t")
        with open("col1.txt","a") as f1: f1.write(l[0]+"\n")
        with open("col2.txt","a") as f2: f2.write(l[1]+"\n")
        

with open("col1.txt","r") as f1: print(f1.read())
with open("col2.txt","r") as f2: print(f2.read())

