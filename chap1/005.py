"""
005
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

def make_Ngram(l,n): return [l[i:i+n] for i in range(len(l)-n+1)]

if __name__ == "__main__":
    text,n = "I am an NLPer",2
    #単語bi-gram
    print(make_Ngram(text.split(" "),n))
    #文字bi-gram
    print(make_Ngram(text,n))

"""
[['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
"""
