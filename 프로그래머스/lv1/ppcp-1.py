def solution(bandage: list[int], health: int, attacks: list[list[int]]):
    excution_time, heal_amount, additional_heal = bandage

    current_health = health
    current_time = 0
    continuous_heal = 0

    while attacks:
        print(current_time, current_health, continuous_heal, attacks)
        if current_time == attacks[0][0]:
            attack = attacks.pop(0)
            attack_time, attack_damage = attack
            current_health -= attack_damage
            continuous_heal = 0
            if current_health <= 0:
                return -1

            current_time += 1

            continue

        current_time += 1

        if current_health == health:
            continuous_heal += 1
            continue

        current_health += heal_amount
        if current_health > health:
            current_health = health
        continuous_heal += 1
        if continuous_heal >= excution_time:
            current_health += additional_heal
            if current_health > health:
                current_health = health
            continuous_heal = 0

    return current_health
