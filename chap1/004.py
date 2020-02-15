#004
#"Hi He Lied Because Boron Could Not Oxidize Fluorine. 
# New Nations Might Also Sign Peace Security Clause. Arthur King Can."
#という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
#それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置
#（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

sentence = sentence.replace(".","")
sentence = sentence.replace(",","")
word_list = sentence.split()


print(word_list)
n = [1, 5, 6, 7, 8, 9, 15, 16, 19]
my_dic = {}

number = 1
for i in word_list:
    if number in n:
        my_dic[i[0]] = number
    else:
        my_dic[i[0:2]] = number
    number += 1
print(my_dic)

print(dict([(w[0],i) if i in [1,5,6,7,8,9,15,16,19] else (w[0:2],i) for i,w in enumerate("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split(),1)]))



"""
{'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 
'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
"""