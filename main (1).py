print("lets do some multiplication")
x = int(input("Enter one number: "))
y = int(input("Enter another number: "))

result = 0 

if y < 0:   
    count = -y 
else:
    count = y

while count > 0:  
    if x == 0: 
        count = 0      
    result += x        
    count -= 1         

print ("here is the result:", result)