#question 3 page 183
mark = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

student  = int(input('which student are you? [1 ,2 ,3 ,4 or 5]'))
percent = int(input('what percent did you get?: '))
test = int(input('which test was it? [1, 2 or 3]'))
test = test - 1
student = student - 1

mark[student][test] = percent

#student average calculator
total = 0
for index = 0 to 2:
    total = mark[student][index] + total
#next index
avg_student = total / len(mark[student])
print('student average = '+ avg_student)

#class average
total = 0 
for row  = 0 to 4:
    for col = 0 to 3:
        total = mark[row][col] + total
    #next col
#next row
avg_class = total/len(mark)
print('class average = ' + avg_class)

