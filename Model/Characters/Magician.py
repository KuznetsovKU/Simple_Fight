from Model.Characters.Hero_Base import HeroBase


class Magician(HeroBase):
    """Тип персонажа "Маг", наследуется от базовой реализации "Hero_Base"."""
    max_mana = 100
    current_mana = 100
    damage_index = 0.8
    protect_index = 0.8
    heal_index = 1

    def __init__(self, name):
        super().__init__(name)
        self.hero_type = self.__class__.__name__
        self.damage_ability = super().get_damage_ability() * Magician.damage_index
        self.protect_ability = super().get_protect_ability() * Magician.protect_index
        self.heal_ability = super().get_heal_ability() * Magician.heal_index

    def get_max_mana(self):
        return self.max_mana

    def get_current_mana(self):
        return self.current_mana

    def set_max_mana(self, max_mana):
        self.max_mana = max_mana

    def set_current_mana(self, current_mana):
        self.current_mana = current_mana

    def get_full_info(self):
        return super().get_full_info() + f", max_mana = {self.max_mana}, current_mana = {self.current_mana}"
