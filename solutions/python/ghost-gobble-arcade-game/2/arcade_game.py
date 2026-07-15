def eat_ghost(power_pellet_active, touching_ghost):   
    return power_pellet_active and touching_ghost
    pass


def score(touching_power_pellet, touching_dot):   
    return touching_power_pellet or touching_dot
    pass


def lose(power_pellet_active, touching_ghost):
    return not power_pellet_active and touching_ghost
    pass


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and (power_pellet_active or not touching_ghost)
    pass
