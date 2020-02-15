#000
#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ
text = "stressed"
print(text[::-1])
#desserts

l = list("stressed")
res = ""
while len(l)>0:
    res += l.pop()
print(res)
#desserts

print("".join(reversed("stressed")))
#desserts

s = list("stressed")
s.reverse()
print("".join(s))
#desserts

#print("".join(list("stressed")).reverse())


print("stressed"[::-1])
#desserts

print(len('print("stressed"[::-1])'))
print(len('print("stressed".reverse())'))
