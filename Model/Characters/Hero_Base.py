
class HeroBase:
    """Базовый вариант игрового персонажа"""

    @staticmethod
    def get_new_id(id_num):
        HeroBase.id_num += 1
        return id_num

    name = ""
    id_num = 1
    hero_type = "no_type"
    level = 0
    max_hp = 100
    current_hp = max_hp
    experience_points = 0
    damage_ability = 1
    protect_ability = 1
    heal_ability = 1
    level_up_border = 100
    life_status = True

    def __init__(self, name):
        self.name = name
        self.id_num = HeroBase.get_new_id(HeroBase.id_num)

    def get_full_info(self):
        l_s = "Alive"
        if not self.life_status:
            l_s = "Died"
        return (f"id = {self.id_num}, name = {self.name}, type = {self.hero_type}, level = {self.level}, "
                f"max_HP = {self.max_hp}, current_HP = {self.current_hp}, exp_points = {self.experience_points}, "
                f"damage_ability = {self.damage_ability}, protect_ability = {self.protect_ability}, "
                f"heal_ability = {self.heal_ability}, level_up_border = {self.level_up_border}, "
                f"life_status = {l_s}")

    def get_basic_info(self):
        return f"id = {self.id_num}, name = {self.name}, type = {self.hero_type}, level = {self.level}"

    def get_name(self):
        return self.name

    def get_id_num(self):
        return self.id_num

    def get_hero_type(self):
        return self.hero_type

    def get_level(self):
        return self.level

    def get_max_hp(self):
        return self.max_hp

    def get_current_hp(self):
        return self.current_hp

    def get_experience_points(self):
        return self.experience_points

    def get_damage_ability(self):
        return self.damage_ability

    def get_protect_ability(self):
        return self.protect_ability

    def get_heal_ability(self):
        return self.heal_ability

    def get_level_up_border(self):
        return self.level_up_border

    def get_life_status(self):
        return self.life_status

    def set_name(self, name):
        self.name = name

    def set_id_num(self, id_num):
        self.id_num = id_num

    def set_hero_type(self, hero_type):
        self.hero_type = hero_type

    def set_level(self, level):
        self.level = level

    def set_max_hp(self, max_hp):
        self.max_hp = max_hp

    def set_current_hp(self, current_hp):
        self.current_hp = current_hp

    def set_experience_points(self, experience_points):
        self.experience_points = experience_points

    def set_damage_ability(self, damage_ability):
        self.damage_ability = damage_ability

    def set_protect_ability(self, protect_ability):
        self.protect_ability = protect_ability

    def set_heal_ability(self, heal_ability):
        self.heal_ability = heal_ability

    def set_level_up_border(self, level_up_border):
        self.level_up_border = level_up_border

    def set_life_status(self, life_status):
        self.life_status = life_status

