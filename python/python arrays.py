x = 5
y = 5.1
print(x + y)

#declare my_array[0..9] of interger
my_array_list = [0 for x in range(10)]
'''for i in range(10):
    my_array_list.appends(0)'''
#next i
print(my_array_list)

my_array_list[4] = 1

print(my_array_list)

#2d arrays
my_array = [[x for x in range(4)] for x in range(10)]

print(my_array)

# tuples
my_tuple = (1,2,3)
# 1 2 3 is imutable but my_tuple is just a reference
print(my_tuple)

#my_tuple[2] = 1 cant change the value and all tuples in python have round brackets

'''my_tuple = (1,2,4)
print(my_tuple)'''

my_tuple = ('c','a','t')
my_string ='cat'
my_list = ['c','a','t']

my_list[2] = 'p'


print(my_list, my_string, my_tuple)

# slicing strings
my_string = 'impossible'
my_sting = my_string[0:3] + '0 ' +  my_string[4:len(my_string)] #up to but not including the final index point

# or my_string[0:3:1] will take every letter [:3:2] every other letter [:3:-1] negative step so going backwards
#pure reversed is just [0:0:-1]


