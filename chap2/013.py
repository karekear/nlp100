"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
013
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べた
テキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""
with open("merge.txt","w") as f: f.write("")

with open("col1.txt","r") as f1: l1 = f1.readlines()
with open("col2.txt","r") as f2: l2 = f2.readlines()
for i,j in zip(l1,l2): 
    with open("merge.txt","a") as f: f.write(i.replace("\n","")+"\t"+j)

with open("merge.txt","r") as f: print(f.read())


