from calculator import battle_simulation as sim

aggressor = {
    "infantry": 15,
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

sim.combat_main(aggressor,defender)