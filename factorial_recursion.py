# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)
def sumofnumbers(n):
    if(n==1):
        return 1
    return n+sumofnumbers(n-1)
def main():
    n=int(input("Enter a number: "))
    print(f"sum of numbers till {n} is {sumofnumbers(n)}")
    b=int(input("Enter a number: "))
    print(f"Factorial of {b} is {factorial(b)}")
if __name__=="__main__":
    main()