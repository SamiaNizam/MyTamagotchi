class Alina:
    def __init__(self, name, hunger, energy, happiness, talk):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.talk_level = talk

    def talk(self):
        self.talk_level += 10
        if self.talk_level > 100:
            self.talk_level = 100
        print(f"{self.name} is talking about her Plushes!")

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

