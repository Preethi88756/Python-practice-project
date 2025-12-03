import random

world_list=["apple","mango","kivi"]
lives=6

choosen_world=random.choice(world_list)
print(choosen_world)

placeholder=""
world_length=len(choosen_world)
for position in range(world_length):
    placeholder+= "-"
print(placeholder)

game_over=False

correct_letters=[]
while not game_over:
    guess=input("guess the letter:").lower()

    display=""

    for letter in choosen_world:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
            
        else:
            display+="-"
    print(display)

    if guess not in choosen_world:
        lives-= 1
        if lives ==0:
            game_over=True
            print("you loose")

    if "-" not in display:
        game_over=True
        print("you win")
    
