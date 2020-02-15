#003
#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ

#s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
#l = s.split()

#def a(s): return len(s)-

#sentense = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
#w = ((sentense.replace(".","")).replace(".","")).split()
#sentense = sentense.replace(",","")
#w = sentense.split()
"""
len_list = []
for i in word_list:
    len_list.append(len(i))
"""
#print([len(i) for i in w])
'[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]'

s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

print([len(i) for i in (('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'.replace(",","")).replace(".","")).split()])

