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

"""
def welcome():
    print(("# " *10) +'#')
    print('#' + (' '*19) + '#')
    print('#'+ (' '*6) + 'MADLIBS' + (' '*6) +'#')
    print('#' + (' '*19) + '#')
    print(("# " *10) +'#')
    print()

def input_script():
    userScript = input("Enter your script: ")
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


def questions(qOrder, script):
    print("Now ask a friend to fill in your MadLib!")
    play = input("press ENTER to continue\n")
    #later add a secret easter egg input
    print('Fill in the blanks!')
    for q in qOrder:
        if q == 'n': #nouns
            print(script)
            fill = input('Enter a noun')
        if q == 'j': #adjectives
            pass
        if q == 'v': #ver
            pass
        if q == 'm':
            pass

def play():
    welcome()
    newScript = input_script()
    blanks(newScript)
    #blanks(newScript)[0] is the order list
    #blanks(newScript)[1] is the scipt with blanks
    
    
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