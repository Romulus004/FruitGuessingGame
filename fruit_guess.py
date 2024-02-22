import random

fruit_list = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Watermelon", "Pineapple", "Mango", "Kiwi"]

print("Welcome to Fruit Guessing Game. \nThere are 14 fruits in the basket.")

secret_num = random.randint(0,len(fruit_list))
secret_fruit = fruit_list[secret_num]

if len(secret_fruit)%2 == 0:
    hint = f"*The length of word is even.*"
else:
    hint = f"*The length of word is odd.*"
    
print(f'{"*"*len(hint)}\n{hint}\n{"*"*len(hint)}\n')


for i in range(3):
    guess = input("Enter a guess word: ")

    if guess == secret_fruit:
        print("\n$$$Congratulations!!! You have won the game$$$")
        break
    else:
        if i < 2 :
            print(f"Incorrect guess. You can try {3-(i+1)} more time(s).")
        else:
            print(f"@@@Gameover. 3 failed attempts@@@ \nThe secret fruit is {secret_fruit}.")
