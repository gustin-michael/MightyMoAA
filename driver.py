from calculator import battle_simulation as sim

aggressor = {
    "infantry": 5,
    "artillery": 0,
    "tank": 0,
    "fighter": 0,
    "bomber": 0,
}

defender = {
    "infantry": 10,
    "artillery": 0,
    "tank": 0,
    "fighter": 0,
    "bomber": 0,
}

#sim1 = sim.battle_simulation(aggressor, defender)
#print(id(aggressor))
sim.battle_main(aggressor,defender)