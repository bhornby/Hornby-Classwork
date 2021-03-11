f = open('highscore2.txt','r')
data = f.read()
f.close()
print(data)

for c in data:
    print(c)