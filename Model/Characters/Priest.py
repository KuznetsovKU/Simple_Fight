from Model.Characters.Hero_Base import HeroBase


class Priest(HeroBase):
    """Тип персонажа "Жрец", наследуется от базовой реализации "Hero_Base"."""
    max_elixir = 100
    current_elixir = 100
    damage_index = 1
    protect_index = 0.6
    heal_index = 1.2

    def __init__(self, name):
        super().__init__(name)
        self.hero_type = self.__class__.__name__
        self.damage_ability = super().get_damage_ability() * Priest.damage_index
        self.protect_ability = super().get_protect_ability() * Priest.protect_index
        self.heal_ability = super().get_heal_ability() * Priest.heal_index

    def get_max_elixir(self):
        return self.max_elixir

    def get_current_elixir(self):
        return self.current_elixir

    def set_max_elixir(self, max_elixir):
        self.max_elixir = max_elixir

    def set_current_elixir(self, current_elixir):
        self.current_elixir = current_elixir

    def get_full_info(self):
        return super().get_full_info() + f", max_elixir = {self.max_elixir}, current_elixir = {self.current_elixir}"
