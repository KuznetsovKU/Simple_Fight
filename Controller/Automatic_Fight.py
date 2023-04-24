from Hero_Service import Hero_Behavior, Hero_Service


def automatic_fight():
    hero_1 = Hero_Service.create_new_hero()
    print("Created new Hero: " + hero_1.get_full_info())
    print()
    hero_2 = Hero_Service.create_new_hero()
    print("Created new Hero: " + hero_2.get_full_info())
    print()
    print("The fight is started!")
    while hero_1.get_life_status() and hero_2.get_life_status():
        Hero_Behavior.attack(hero_1, hero_2)
        Hero_Behavior.attack(hero_2, hero_1)
        print(hero_1.get_full_info())
        print(hero_2.get_full_info())
