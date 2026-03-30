s = "nithish"
h = ""
if (s == "a" or s == "e" or s == "i" or s == "o" or s == "u"):
    h = h + s
    print(h)
for i in range(len(h)):
    temp = h[i]
    h[i] = h[len(h)-1-i]
    h[len(h)-1-i] = temp
s = s.replace("nithish" , h)

