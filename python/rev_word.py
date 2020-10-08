#reverse 'STARS' using recursion

def rev_word(word):
    letter = word[0]
    if len(word) == 1:
        return letter
    else:
        return rev_word(word[1:]) + letter
    #end if
#end function    
#base case

print(rev_word("star"))