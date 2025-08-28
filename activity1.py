# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power       # Encapsulated attribute
        self.origin = origin

    def introduce(self):
        print(f"🦸‍♂️ I am {self.name} from {self.origin}, and I wield the power of {self._power}!")

    def get_power(self):
        return self._power

    def set_power(self, new_power):
        self._power = new_power

# Subclass with inheritance
class TechHero(Superhero):
    def __init__(self, name, origin, gadget):
        super().__init__(name, "Tech Manipulation", origin)
        self.gadget = gadget

    def use_gadget(self):
        print(f"{self.name} activates their {self.gadget} to hack the system! 💻")

# Another subclass
class NatureHero(Superhero):
    def __init__(self, name, origin, element):
        super().__init__(name, "Nature Control", origin)
        self.element = element

    def summon_element(self):
        print(f"{self.name} summons the power of {self.element}! 🌿")

# Example usage
hero1 = TechHero("ByteBlade", "Nairobi", "Quantum Wristband")
hero2 = NatureHero("LeafStorm", "Kajiado", "Wind")

hero1.introduce()
hero1.use_gadget()

hero2.introduce()
hero2.summon_element()
