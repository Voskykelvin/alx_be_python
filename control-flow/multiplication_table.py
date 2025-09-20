number = int(input("Enter a number to see its multiplication table: "))
Y = ('1','2','3','4','5','6','7','8','9','10')
product = 0
for Y in range(1 , 11):
    product = number * Y
    Y += 1
    print(product)
    
    