"""
009
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
を与え，その実行結果を確認せよ．
"""
import random

t = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

#t...str
def h(t):
    if len(t) > 4:
        return t[0] + "".join(random.sample(t[1:len(t)-1],len(t)-2)) + t[-1]
    return t

def g(t): return "".join([i+" " for i in map(h,t.split(" "))])

print(g(t))

#I cuo'nldt beelive that I cluod alltuacy uardntnsed what I was rndieag : the pnoanhmeel peowr of the hmuan mind .


#ひとつの関数にまとめた版
def f(t):
    y = t.split(" ")
    l = ""
    for i in y:
        if len(i) > 4:
            i = list(i)
            i[1:len(i)-1] = random.sample(i[1:len(i)-1],len(i)-2)
            l += str("".join(i))+" "
        else: l+=i+" "
    print(l)