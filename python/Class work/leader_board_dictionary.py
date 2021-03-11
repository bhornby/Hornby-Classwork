# making a dictionary for high scores
score = {'1:':0, '2:':0, '3:':0, '4:':0, '5:': 0}

new_score = input('what was your score?')
new_name = input("what's your name")

for key,value in score.items():
    if new_score > key:
        score[1] = (new_name,new_score)
        

for key, value in score.items():
    print(key,value)
#next key and value
