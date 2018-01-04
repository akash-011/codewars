# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

#     each taken only once - coming from s1 or s2. #Examples: ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```




def longest(s1, s2):
    new_list = []
    for i in s1:
        if i in new_list:
            pass  
        else:
            new_list.append(i)
    
    for i in s2:
         if i in new_list:
            pass
         else:
            new_list.append(i)
    
    new_list = sorted(new_list)
    new_str = ''.join(new_list)
    return new_str