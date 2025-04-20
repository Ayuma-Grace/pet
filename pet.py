class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a nap. Energy: {self.energy}")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played and had fun!")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        print(f"{self.name} knows the following tricks:")
        for trick in self.tricks:
            print(f"- {trick}")

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(r"""
   __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/ (_/ 
""")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("-" * 30)
