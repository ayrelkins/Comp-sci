binary = input ("Input a number in Binary:")
denary = 0
for digit in binary:
  denary = denary*2 + int(digit)
print ("Your Denary number is: "+str (denary))

denary = int(input("Input a denary number:"))
binary=""
while denary>0:
  binary = str(denary%2)+ binary
  denary = denary//2
  print("Your binary number is: " +binary)