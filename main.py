import random
import time

sequence = ["q","w","e","r","t","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","1","2","3","4","5","6","7","8","9",",",".","/","!","£","$","%","^","&","*","(",")","-","+","=","~","@","'",";",":","?","<",">","¬","|"]
final = []

userInput = True
while userInput == True:
  try:
    letters = int(input("How many characters would you like to have in your password? "))
    userInput = False
  except:
    print("Invalid input - Not a number")  
    time.sleep(1)

for x in range(letters):
  final.append(random.choice(sequence))

print(''.join(final))