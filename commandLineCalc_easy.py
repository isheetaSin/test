'''
make a command line calculator

DIFFICULTY = MEDIUM
TOPICS = strings, variables, lists

your task is to write a command line calculator
this task is easy since we can use the eval function to do most of the legwork
however, we need to parse possible invalid user input. This is your task

return None if invalid input. Otherwise return the result
'''

def calculate(s):
   
    # TODO = fill in this function


    '''    
	cases: 
		multiplication and division adjacent to each other
		any other charcater than 10 digits and 4 operations
    '''

    check = 0
    
    #check for non digit and non operation and non brackets character
    '''
    for i in range(len(s)):
        if s[i]!='0' and s[i]!='1' and s[i]!='2' and s[i]!='3' and s[i]!='4'and s[i]!='5'and s[i]!='6'and s[i]!='7'and s[i]!='8'and s[i]!='9'and s[i]!='+'and s[i]!='-'and s[i]!='/'and s[i]!='*' and s[i]!='(' and s[i]!=')':
            #print("None")
            check = 1
            break
    '''
    valid = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, -, *, /, (, )'
    
    for i in range(len(s)):
        if s[i] not in valid:
		check = 1
	
    '''	
    for i in range(len(s)):
        if s[i].isdigit() == 0 and s[i]!='+'and s[i]!='-'and s[i]!='/'and s[i]!='*' and s[i]!='(' and s[i]!=')':
            check = 1
            break   
    '''
    #check for adjacent multiplication and division

    curr_div = 0
    curr_mul = 0
    for i in range(len(s)):
        if s[i] == '/':
            curr_div = 1
        elif s[i] == '*':
            curr_mul = 1
        else: 
            curr_div = 0
            curr_mul = 0
        if curr_div == 1 and s[i] == '*':
            check = 1
            break
        elif curr_mul == 1 and s[i] == '/':
            check = 1
            break


    if check == 0:
        result = eval(s)
        print (result)

	
    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()



'''
phrase = input()
calculate(phrase)
'''
