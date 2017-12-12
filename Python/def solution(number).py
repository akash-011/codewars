# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.


def solution(number):
    multiples = []
    total = 0
    for num in range(1, number):
            if (num % 3 == 0) | (num % 5 == 0):
                multiples.append(num)

    for nums in multiples:
        total += nums 
    
    return total


print (solution(10))