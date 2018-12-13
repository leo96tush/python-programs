def sum_of_digits(n,d):
    n1 = int(n)
    n2 = int(round((n - n1)*pow(10,d)))
    s = 0
    while(n1>0):
        rem1 = n1%10
        s = s + rem1
        n1 = n1//10

    while(n2>0):
        rem2 = n2%10
        s = s + rem2
        n2 = n2//10

    return(int(s))

print("Number of digits after decimal: ")
dec = int(input())
print("Enter the number: ")
number = float(input())
print("The sum of digits is: ")
print(sum_of_digits(number,dec))
