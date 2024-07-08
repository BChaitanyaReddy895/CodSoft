import random
n=int(input("Enter the desired length for your password:"))
character=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
         "A","B","C","D","E","F","I","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","+","-","_","=","[","]","{","}","|",".",",","?","/","<",">"]
password_list=[]
for i in range(0,n):
    password_list+=random.choice(character)
password=""
for i in password_list:
    password+=i
print("Your generated password is:",password)
    
