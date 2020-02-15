"""
008
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
・英小文字ならば(219 - 文字コード)の文字に置換
・その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""
def cipher(s): return "".join([chr(219-ord(i)) if 96<ord(i)<123 else i for i in list(s)])

txt = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
txt = cipher(txt)   #暗号化
print(txt)
txt = cipher(txt)   #復号化 
print(txt)

#Nld I mvvw z wirmp, zoxlslorx lu xlfihv, zugvi gsv svzeb ovxgfivh rmeloermt jfzmgfn nvxszmrxh.
#Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.

