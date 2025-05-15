def fizzBuzz(n):
    solution = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            solution.append("FizzBuzz")
        elif i % 3 == 0:
            solution.append("Fizz")
        elif i % 5 == 0:
            solution.append("Buzz")
        else:
            solution.append(str(i))
    return solution

def main(): #Easier to just copy paste examples w/ only n change
    print("Example 1:")
    print(fizzBuzz(3))  #Outputs: 1, 2, Fizz
    
    print("Example 2:")
    print(fizzBuzz(5))  #Outputs: 1, 2, Fizz, 4, Buzz
    
    print("Example 3:")
    print(fizzBuzz(15))  #Outputs: 1, ... ect, FizzBuzz

    #Extra test cases for constraints
    print("Example 4:")
    print(fizzBuzz(1))  #Outputs: 1

    print("Example 5:")
    print(fizzBuzz(0))  #Outputs: [] or empty
main()