from calculator import battle_simulation as sim

aggressor = {
    "infantry": 30,
    "artillery": 0,
    "tank": 0,
    "fighter": 0,
    "bomber": 0,
}

defender = {
    "infantry": 20,
    "artillery": 0,
    "tank": 0,
    "fighter": 0,
    "bomber": 0,
}

sim1 = sim.battle_simulation(aggressor, defender)