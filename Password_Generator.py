#importing random module to generate random numbers or choices
import random
#prompting the user to enter the desired length of the password required
n=int(input("Enter the desired length for your password:"))
# storing all characters required in password in a list
character=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
         "A","B","C","D","E","F","I","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","+","-","_","=","[","]","{","}","|",".",",","?","/","<",">"]
password_list=[] #initialising the password list with empty list
for i in range(0,n):
    #using choice() function in random module to generate random choices
    password_list+=random.choice(character)
password=""
for i in password_list:
    password+=i # converting password list to string
print("Your generated password is:",password)
    

    
