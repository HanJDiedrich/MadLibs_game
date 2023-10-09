#madlibs game
"""
User inputs a string containing special phrases where you want to place the word that signify noun, adjective, adverb, number
noun singular = **nos**
noun plural = **nop**
verb = **ver**
adjective = **adj**
adverd = **adv**
number = **num**

Then it prompts the string with ____s and begins with a prompt for each sig phrase
asks a friend to input their own answers to each box
returns the completed string


INSTRUCTIONS

Welcome to MADLIBS!
To create your mad lib, write a scentence or few while leaving indicators for the places you wa
"""
#title card
def welcome():
    print(("# " *10) +'#')
    print('#' + (' '*19) + '#')
    print('#'+ (' '*6) + 'MADLIBS' + (' '*6) +'#')
    print('#' + (' '*19) + '#')
    print(("# " *10) +'#')
    print()

def input_script():
    userScript = input("Enter your script: ")
    print()
    return userScript

def blanks(script):
    indicators = ['**nos**','**nop**','**ver**','**adj**','**adv**','**num**']
    qOrder = [] #n, v, j, d, m
    
    #check every 7 characters to find our indicators
    for i in range(0, len(script)):
        segment = script[i:i+7]
        if segment in indicators:
            #noun singular (s)
            if segment == indicators[0]:
                qOrder.append('s')
            #noun plural (p)
            if segment == indicators[1]:
                qOrder.append('p')
            #verb (v)
            if segment == indicators[2]:
                qOrder.append('v')
            #adjective (j)
            if segment == indicators[3]:
                qOrder.append('j')
            #adverb (d)
            if segment == indicators[4]:
                qOrder.append('d')
            #number (m)
            if segment == indicators[5]:
                qOrder.append('m')
                
            #replace indicator in the script with a blank
            script = script[:i] + "_______" + script[i+7:]
            
        #End when the final segment covers the end of the script
        if (i + 7) == len(script):
            break
    #Now we get the order of and questions that should be asked to fill in the madlib
    return qOrder, script

def initiatePlay(script):
    print(f'Here is your MADLIB!\n{script}\n')
    print("Now ask a friend to fill in your MadLib!")
    play = input("press ENTER to continue\n")
    #later add a secret easter egg input
    
def replaceblank(fill, script):
    fill_script = script.replace("_______", fill, 1)
    return fill_script   
 
'''
when the player inputs a word into the blank, it reprints the script with the filled word.
do this for every question.

use a recursive function 

def recursion(order, script): #fill_script
    print(script)
    if len(order) == 0: #go through the list of indicators
        return script
    else:
        if order[0] == 'n':
            pass
            
ask user for their input
replace their input in the first underscore
remove the first index of qOrder
send that new string and new order through
    
'''
def questionsRecursive(order, script): #fill_script
    if len(order) == 0: #go through the list of indicators
        print('Here is your MADLIB:')
        print(script +'\n')
        print('Hahahaha, thanks for playing!')
    else:
        print(script)
        if order[0] == 's':
            fill = input('Enter a singular noun: ') 
        elif order[0] == 'p':
            fill = input('Enter a plural noun: ')
        elif order[0] == 'v':
            fill = input('Enter a verb: ')
        elif order[0] == 'j':
            fill = input('Enter a adjective: ')
        elif order[0] == 'd':
            fill = input('Enter a adverb: ')
        elif order[0] == 'm':
            fill = input('Enter a number: ')
        print()
        #update the script
        updated = replaceblank(fill, script)
        order.remove(order[0])
        #call recursive
        questionsRecursive(order, updated)
        
def play():
    welcome()
    newScript = input_script()
    info = blanks(newScript)
    order = info[0]
    blank_script = info[1]
    initiatePlay(blank_script)
    questionsRecursive(order,blank_script)
    
play()


'''
TEST SCRIPT
noun singular = **nos**
noun plural = **nop**
verb = **ver**
adjective = **adj**
adverd = **adv**
number = **num**

One **adj** day, **nos** went to visit the **nos**. The weather was **adj** and the temperature was **num** degrees. **nos** **ver** to the **nos**. At the **nos**, there were many **nop**. **nos** **adv** said "This is **adj**!!!

'''