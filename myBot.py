def do_turn(pw):
    if len(pw.my_planets()) == 0:
        return
    if len(pw.enemy_planets()) >= 1:
        dest = pw.enemy_planets()[0]
    else:
        if len(pw.neutral_planets()) >= 1:
            dest = pw.neutral_planets()[0]
    source = pw.my_planets()[0]
    num_ships = source.num_ships() / 2
    pw.debug('Num Ships: ' + str(num_ships))
    pw.issue_order(source, dest, num_ships)

def closest_neutral(pw):
    neutral_planets = pw.neutral_planets()()
    closest_planet = neutral_planets[0]
    closest_dis = 10000
    for source in pw.my_planets():
        for dest in neutral_planets:
            if(pw.distance(source,dest) < closest_dis):
                closest_distance = pw.distance(source,dest)
                if(source.num_ships() > dest.num_ships()):
                    closest_planet = dest
                    closest_dis = closest_distance
