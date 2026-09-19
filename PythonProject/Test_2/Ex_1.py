import json

class Warrior:
    def __init__(self):
        self._health = 30
        self.attack = 5

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

    @property
    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_target(self, target):
        target.take_damage(self.attack)

    def __str__(self):
        base_info = f"{self.__class__.__name__}, HP: {self.health}, ATK: {self.attack}"
        if hasattr(self, 'magic'):
            base_info += f", MAG: {self.magic}"
        return base_info

    def __add__(self, other):
        new_unit = self.__class__()
        new_unit.health += other
        new_unit.attack += other
        return new_unit

    def __mul__(self, other):
        new_unit = self.__class__()
        new_unit.health *= other
        new_unit.attack *= other
        return new_unit


class Fighter(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Mage(Warrior):
    def __init__(self):
        super().__init__()
        self.magic = 6

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.magic)
        super().take_damage(actual_damage)

    def attack_target(self, target):
        if target.attack < self.magic:
            target.take_damage(self.attack + self.magic)
        else:
            target.take_damage(self.attack)


class Paladin(Warrior):
    def __init__(self):
        super().__init__()
        self._health = 50
        self.attack = 6

    @Warrior.health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 50:
            self._health = 50
        else:
            self._health = value

    def attack_target(self, target):
        target.take_damage(self.attack)
        heal_amount = self.attack * 0.2
        self.health += heal_amount


def fight(unit1, unit2):
    while unit1.is_alive and unit2.is_alive:
        unit1.attack_target(unit2)
        if not unit2.is_alive:
            break
        unit2.attack_target(unit1)
    return unit1.is_alive

class Army:
    def __init__(self):
        self.units = []

    def add_members(self, unit_class, count):
        for _ in range(count):
            self.units.append(unit_class())

    def __len__(self):
        return len(self.units)

    def __getitem__(self, item):
        return self.units[item]

    def __iter__(self):
        return iter(self.units)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_army = Army()
            new_army.units = [warrior + other for warrior in self.units]
            return new_army
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_army = Army()
            new_army.units = [warrior * other for warrior in self.units]
            return new_army
        return NotImplemented