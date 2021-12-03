#from calculator import battle_instance
from calculator.battle_instance import battle_instance

def combat_main(aggressor_json,defender_json,num_sims=10000,rounds=100):
  num_atk_wins = 0
  num_def_wins = 0
  num_ties = 0
  for i in range(num_sims):
    #print("Combat: " + str(i+1))
    cur_battle = battle_instance(aggressor_json,defender_json,rounds,i)

    if(cur_battle.winner == "ATK"):
      num_atk_wins += 1
    elif(cur_battle.winner == "DEF"):
      num_def_wins += 1
    else:
      num_ties += 1

  print("Offence wins " + str((num_atk_wins/num_sims)*100) + "% of the time")
  print("Defence wins " + str((num_def_wins/num_sims)*100) + "% of the time")
  print("Ties " + str((num_ties/num_sims)*100) + "% of the time")
