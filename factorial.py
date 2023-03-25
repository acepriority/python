# number = int(input('enter the number: '))

# factorial = 1

# if number < 0: 
#    print("can't compute factorial for negative numbers")
# elif number <= 1:
#    print("{}! = {}".format(number, factorial))
# else:
#    for i in range(number,1,-1):
#       factorial = factorial * i

#    print("{}! = {}".format(number, factorial))

while True:
   def factorial(n):
      if (0 <= n <= 1):
         return 1
      else:
         return n*factorial(n-1) 

   n = int(input("enter n - value -- "))
   res = factorial(n)
   print(res)

   again = input("enter n again??: (yes/no) ")

   if again != "yes":
      break
