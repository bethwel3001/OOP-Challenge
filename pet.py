class Pet:
    # Class constants for easy tuning
    HUNGER_REDUCTION = 3
    ENERGY_GAIN = 5
    PLAY_ENERGY_COST = 2
    PLAY_HAPPINESS_GAIN = 2
    PLAY_HUNGER_GAIN = 1

    def __init__(self, name):
        """Initialize a new pet with default stats."""
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """Reduce hunger and slightly increase happiness."""
        self.hunger = max(self.hunger - self.HUNGER_REDUCTION, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"🍗 {self.name} munches happily! (-{self.HUNGER_REDUCTION} hunger, +1 happiness)")

    def sleep(self):
        """Restore energy significantly."""
        self.energy = min(self.energy + self.ENERGY_GAIN, 10)
        print(f"💤 {self.name} takes a nap! (+{self.ENERGY_GAIN} energy)")

    def play(self):
        """Play if energy is sufficient, otherwise warn."""
        if self.energy >= self.PLAY_ENERGY_COST:
            self.energy -= self.PLAY_ENERGY_COST
            self.happiness = min(self.happiness + self.PLAY_HAPPINESS_GAIN, 10)
            self.hunger = min(self.hunger + self.PLAY_HUNGER_GAIN, 10)
            print(f"🎾 {self.name} plays excitedly! (-{self.PLAY_ENERGY_COST} energy, +{self.PLAY_HAPPINESS_GAIN} happiness)")
        else:
            print(f"😴 {self.name} is too exhausted to play!")

    def train(self, trick):
        """Teach a new trick and reward happiness."""
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)
        print(f"🌟 {self.name} learned '{trick}'! (+1 happiness)")

    def show_tricks(self):
        """Display all learned tricks with flair."""
        if self.tricks:
            print(f"🎩 {self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"🤷 {self.name} hasn't learned any tricks yet.")

    def get_status(self):
        """Show a visual status bar."""
        print(f"\n📊 {self.name}'s Status:")
        print(f"Hunger:    {'🍽️ ' * self.hunger}{'○ ' * (10 - self.hunger)}")
        print(f"Energy:    {'⚡ ' * self.energy}{'○ ' * (10 - self.energy)}")
        print(f"Happiness: {'❤️ ' * self.happiness}{'○ ' * (10 - self.happiness)}")
        self.show_tricks()