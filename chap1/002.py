#002
#「パトカー」＋「タクシー」の文字を
#先頭から交互に連結して文字列「パタトクカシーー」を得よ．

pat,tax = "パトカー","タクシー"
res = ""
for i,j in zip(pat,tax):
    res += i+j
print(res)
"パタトクカシーー"


print("".join([i+j for i,j in zip("パトカー","タクシー")]))


print(len('print("".join([i+h for i,h in zip("パトカー","タクシー")]))'))
#51
print(len('pat,tax = "パトカー","タクシー"\nres = ""\nfor i,j in zip(pat,tax):\n\tres += i+j\nprint(res)'))
#80
"パタトクカシーー"