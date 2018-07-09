'''
You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even,
 return the middle 2 characters.

 Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

'''

#My Solution
def get_middle(s):
    #your code here
    if len(s) % 2 ==0:
        mid = len(s) / 2
        middle_letters = []
        middle_letters.append(s[mid-1])
        middle_letters.append(s[mid])
        str = ''.join(middle_letters)
        return str
    else:
        mid = (len(s) -1) /2
        return s[mid]


#Best Solution 
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]