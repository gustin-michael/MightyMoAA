from calculator import calculator_main

aggressor = {
    "infantry": 3,
    "artillery": 3,
    "tank": 0,
    "fighter": 0,
    "bomber": 2,
}

defender = {
    "infantry": 5,
    "artillery": 0,
    "tank": 1,
    "fighter": 0,
    "bomber": 0,
}

calculator_main.take_unit_count(aggressor, defender)