class Amalia:
    def __init__(self, name, hunger, energy, happiness, dance):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.dance_level = dance
        self.image_path = "assets/amalia.png"
    
    def dance(self):
        self.dance_level += 10
        if self.dance_level > 100:
            self.dance_level = 100
        print(f"{self.name} is dancing to Baby Shark!")

    def feed(self, food_amount):
        self.hunger = max(0, self.hunger - food_amount)
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed. Hunger level: {self.hunger}")

    def play(self, play_time): 
        self.happiness += play_time
        self.energy = max(0, self.energy - play_time // 2)
        if self.energy < 0:        
            self.energy = 0
        print(f"{self.name} played for {play_time} minutes. Happiness level: {self.happiness}, Energy level: {self.energy}")

    def sleep(self, sleep_time): 
        self.energy += sleep_time
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} slept for {sleep_time} minutes. Energy level: {self.energy}")

    def status(self):
        print(f"Status of {self.name}: Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

        