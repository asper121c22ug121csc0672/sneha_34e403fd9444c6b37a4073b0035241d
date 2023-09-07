#1.1 replement a recursive function to celebrate the factorial of a given number;

def fact_rec(n):
  if n==10 or n==1:
    return 1
  else:  
    return n*fact_rec(n-1)

number=2
res=fact_rec(number)

print("the factorial of{}is{}".format(number,res))




