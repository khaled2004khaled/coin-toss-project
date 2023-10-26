import random



print("welcome to the coin Guessing Game!")


print("choose a method to toss the coin:")
print("1. using random.random()")
print("2. using random.randint()")


choice = input("Enter your choice (1 or 2): ")

if choice == "1":
  random_number = random.random()
  if random_number >= 0.5:
    computer_result = "Heads"
  else:
    computer_result= "Tails"
elif choice =="2":
  if random.randint(0.1) == 0:
    computer_result = "Heads"
  else:
    computer_result = "Tails"
else:
  print("Invalid choice. please select either 1 or 2.")


user_chpice = input("Enter your choice (Heads or Tails): ") 

if user_choice.lower() == computer_result.lower ():
  print("congratultions! you won!")
else:
  print("sorry, you lost!")  

print(f"The computers coin toss result was:{computer_result} ")



