import random

#Characters the generator takes from
sequence = ["q","w","e","r","t","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","1","2","3","4","5","6","7","8","9",",",".","/","!","£","$","%","^","&","*","(",")","-","+","=","~","@","'",";",":","?","<",">","¬","|"]
final = []

#Max and minmum inputs
Minimal = 4
Maximal = 100

userInput = True

while userInput == True:
  try:
    letters = int(input("How many characters would you like to have in your password? "))
    # Overhead checking
    if letters < Minimal:
      print("Invalid input - Input cannot be less than 4")  
      print(
     )
      userInput = True
    elif letters > Maximal:
      print("Invalid input - Input cannot be greater than 100")
    else:
      Looping = True
      while Looping == True:
        for x in range(letters):
          final.append(random.choice(sequence))
          Looping = False
        print(''.join(final))
        final = []
        letters = 0
        print("Input '1' to generate another password")
        print("Input '2' to change the parameters")
        try:
          regen = int(input(""))
          if regen == 1:
            print("Regenerating..")
            Looping = True
          elif regen == 2:
            Looping = False
            userInput = True
            print("Reloading..")
          else:
            print("Ok Dumb")
            break
        except ValueError:
          regen = str(input(""))
          if regen == "one" or "One" or "ONe" or "ONE" or "oNE" or "onE":
            print("Regenerating..")
            Looping = True
          elif regen == "two" or "Two" or "TWo" or "TWO" or "tWO" or "twO":
            Looping = False
            userInput = True
            print("Reloading..")
        except:
          print("Invalid input - Not a number")
          Looping = False
          break
  except: 
    print("ARE YOU SKUNKED FAM")