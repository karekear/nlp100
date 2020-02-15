"""
006
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

def make_Ngram(l,n): return [l[i:i+n] for i in range(len(l)-n+1)]

if __name__ == "__main__":
    X = set(make_Ngram("paraparaparadise",2))
    Y = set(make_Ngram("paragraph",2))
    print(X)
    print(Y)
    print(X|Y)
    print(X&Y)
    print(X-Y)
    print('se' in X)
    print('se' in Y)
"""
{'ad', 'di', 'se', 'ra', 'ap', 'pa', 'ar', 'is'}
{'gr', 'ag', 'ap', 'ra', 'ph', 'pa', 'ar'}
{'gr', 'ad', 'di', 'se', 'ra', 'ag', 'ap', 'ph', 'pa', 'ar', 'is'}
{'ra', 'ar', 'pa', 'ap'}
{'se', 'di', 'ad', 'is'}
True
False
"""

