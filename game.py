import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))

# Bild laden
amalia_img = pygame.image.load("assets/amalia.png")

# Bild anzeigen
screen.blit(amalia_img, (100, 100))
pygame.display.update()

from amalia import Amalia
from alina import Alina

def main():
    while True:
        print("Welcome to MyTamagotchi!")
        print("Take care of your virtual baby by feeding, playing, talking, dancing and letting it sleep.")
        break
    
    while True:
        print("Let's choose your pet!")
        print("You have Motchi #1 Amalia.")
        print("She is a party animal who loves to dance and have fun!")
        print("Motchi #2 is Alina.")
        print("She loves to talk and eat a lot!")
        pet_choice = input("Which pet would you like to choose? (1 or 2): ")
        if pet_choice == "1":
            print("You have chosen Amalia!")
            my_pet = Amalia("Amalia", hunger=30, energy=70, happiness=90, dance=80)
            break
        elif pet_choice == "2":
            print("You have chosen Alina!")
            my_pet = Alina("Alina", hunger=70, energy=60, happiness=80, talk=90)
            break
        else:
            print("Invalid choice. Please choose again.")
           
    while True:
        print("\nWhat would you like to do with your pet?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Check Status")
        if pet_choice == "1":  
            print("5. Dance")
        elif pet_choice == "2":
            print("5. Talk")
        print("6. Quit")

        action = input("Enter the number of your choice: ")

        if action == "1":
            food_amount = int(input("Enter the amount of food to feed your pet: "))
            my_pet.feed(food_amount)
        elif action == "2":
            play_time = int(input("Enter the amount of time to play with your pet: "))
            my_pet.play(play_time)
        elif action == "3":
            sleep_time = int(input("Enter the amount of time for your pet to sleep: "))
            my_pet.sleep(sleep_time)
        elif action == "4":
            my_pet.status()
        elif action == "5":
            if pet_choice == "1":
                my_pet.dance()
            elif pet_choice == "2":
                my_pet.talk()   
        elif action == "6":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

main()