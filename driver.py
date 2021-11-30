from calculator import calculator_main

aggressor = {
    "infantry": 2,
    "artillery": 2,
    "tank": 2,
    "fighter": 2,
    "bomber": 0,
}

defender = {
    "infantry": 20,
    "artillery": 0,
    "tank": 0,
    "fighter": 0,
    "bomber": 0,
}

calculator_main.take_unit_count(aggressor, defender)