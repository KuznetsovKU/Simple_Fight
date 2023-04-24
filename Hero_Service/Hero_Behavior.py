from random import randint


def get_died(hero):
    """Метод определяющий смерть персонажа"""
    print(f"Hero {hero.get_name()} is died")
    hero.set_damage_ability(0)
    hero.set_protect_ability(0)
    hero.set_heal_ability(0)
    hero.set_life_status(False)
    print()


def get_damage(hero, hp_points):
    """Метод нанесения ущерба персонажу"""
    if hero.current_hp - hp_points <= 0:
        hero.set_current_hp(0)
        get_died(hero)
    else:
        hero.set_current_hp(hero.current_hp - hp_points)


def get_healed(hero, hp_points):
    """Метод лечения персонажа"""
    if hero.get_current_hp + hp_points >= hero.get_max_hp:
        hero.set_current_hp(hero.get_max_hp)
    else:
        hero.set_current_hp(hero.get_current_hp + hp_points)


def attack(hero, target):
    """Метод атаки одним персонажем другого"""
    if hero.life_status:
        damage_points = randint(0, round(30 * hero.damage_ability / target.protect_ability))
        print(f"Hero {hero.name} damaged hero {target.name} on {damage_points} points")
        get_damage(target, damage_points)
        hero.set_experience_points(hero.experience_points + damage_points * 2)
        if hero.experience_points >= hero.level_up_border:
            level_up(hero)
    else:
        pass
    print()


def level_up(hero):
    """Метод повышения уровня персонажа"""
    hero.set_level(hero.level + 1)
    hero.set_experience_points(0)
    hero.set_level_up_border(hero.level_up_border + 100)
    hero.set_max_hp(hero.max_hp + 100)
    hero.set_current_hp(hero.max_hp)
    hero.set_damage_ability(round(hero.damage_ability + hero.level / 20, 2))
    hero.set_protect_ability(round(hero.protect_ability + hero.level / 20, 2))
    hero.set_heal_ability(round(hero.heal_ability + hero.level / 20, 2))
    print(f"Hero {hero.get_name} got new level. Current level is {hero.get_level}.")
