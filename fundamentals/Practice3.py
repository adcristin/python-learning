#Q1: Calculate Simple Interest.

principal = int(input("Enter the original sum of money borrowed or invested: "))
rate = int(input("Enter the interest rate per period: "))
time = int(input("Enter the length of time for which the money is borrowed or invested(in years): "))

SimpleInterest = (principal*rate*time)/100

TotalAmount = principal+SimpleInterest

print("If you invest", principal ,"at a", rate,"% annual interest rate for", time ,"years, the calculation is:")
print("The Simple Interest will be: ", SimpleInterest)
print("The Total Repayment will be: ", TotalAmount)

#Q2: Sum of first 'n' natural numbers.

n = int(input("Enter the range till you want to calculate the sum of natural numbers: "))
add = 0

for i in range(1, n+1):
    add += i 

print("Sum of first", n, "natural numbers is: ", add)