import random
#from calculator.land_hand import land_hand
#import land_hand

class battle_simulation:

  def __init__(self,atkr,dfdr,rounds=100):
    self.offence_cls = atkr
    self.defence_cls = dfdr
    self.rounds = rounds

    self.initial_offence_attack = evaluate_ipc(atkr)
    self.initial_defence_attack = evaluate_ipc(dfdr)

    ################################################################################
    ## # STEP 1 # ##################################################################
    ################################################################################
    #battle_main(self.offence_cls,self.defence_cls,self.rounds)

class land_hand:
    def __init__(self,inf=0,art=0,tan=0,fig=0,bom=0,ant=0,prev=None):
        self.infantry = inf
        self.artillery = art
        self.tank = tan
        self.fighter = fig
        self.bomber = bom
        self.anti_aircraft = ant

    def toString(self):
      return ("i: " + str(self.infantry))


######################################################################################
## # STEP 2 # ########################################################################
######################################################################################
def battle_main(offence, defence, rounds=100, num_sims=5):
  offence_wins = 0
  defence_wins = 0
  tie_count = 0
  battle_log = {}

  print("In Offence: " + str(offence))
  print("In Defence: " + str(defence))

  for i in range(num_sims):
    print()
    print("Combat " + str(i + 1) + "-----------------------")

    #loggin()
    atk = land_hand(offence["infantry"],
                    offence["artillery"],
                    offence["tank"],
                    offence["fighter"],
                    offence["bomber"])

    dfn = land_hand(offence["infantry"],
                    offence["artillery"],
                    offence["tank"],
                    offence["fighter"],
                    offence["bomber"])

    result = run_battle(atk, dfn, rounds)

    if result == 1:
      defence_wins += 1
    elif result == 0:
      offence_wins += 1
    else:
      tie_count += 1
  
  print("Offence wins " + str((offence_wins/num_sims)*100) + "% of the time")
  print("Defence wins " + str((defence_wins/num_sims)*100) + "% of the time")
  print("Ties " + str((tie_count/num_sims)*100) + "% of the time")
  
  return battle_log

######################################################################################
## # STEP 3 # ########################################################################
######################################################################################
def run_battle(attr, defr, rounds):
  round_counter = 0
  new_atk = attr
  new_defr = defr
  while(round_counter < rounds and new_atk is not None and new_defr is not None):
    round_counter += 1
    
    #
    combat_return = combat_round(new_atk,new_defr)
    new_atk = combat_return[0]
    new_defr = combat_return[1]

    print("Defence: " + str(new_defr.toString()))
  
  if new_atk is None and new_defr is None:
    return 2
  elif new_atk is None:
    return 1
  elif new_defr is None:
    return 0

######################################################################################
## # STEP 4 # ########################################################################
######################################################################################
def combat_round(offence, defence):
  atk_hits = evaluate_hits(offence)
  def_hits = evaluate_hits(defence,True)
  print("attacker hits: " + str(atk_hits))
  print("defender hits: " + str(def_hits))

  offence = assign_hits(offence,def_hits)
  defence = assign_hits(defence,atk_hits)
  return [offence,defence]

######################################################################################
## # STEP 5 # ########################################################################
######################################################################################
def evaluate_hits(hand, defence_flag=False):
  hits = 0
  # for unit_type in hand.keys():
  #   match unit_type:
  #       case "infantry":
  #         if(defence_flag):
  #           #hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["infantry"])])
  #           hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.infantry)])
  #         else:
  #           if(hand["artillery"] <= hand["infantry"]):
  #             #hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["artillery"])])
  #             #hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand["infantry"] - hand["artillery"])])
  #             hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.artillery)])
  #             hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand.infantry - hand.artillery)])
  #           else:
  #             #hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["infantry"])])
  #             hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.infantry)])

  #       case "artillery":
  #         #hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["artillery"])])
  #         hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.artillery)])

  #       case "tank":
  #         #hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand["tank"])])
  #         hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand.tank)])

  #       case "fighter":
  #         if(defence_flag):
  #           #hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand["fighter"])])
  #           hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand.fighter)])
  #         else:
  #           #hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand["fighter"])])
  #           hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand.fighter)])

  #       case "bomber":
  #         if(defence_flag):
  #           #hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand["bomber"])])
  #           hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand.bomber)])
  #         else:
  #           #hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand["bomber"])])
  #           hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand.bomber)])

  if(defence_flag):
    #hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["infantry"])])
    hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.infantry)])
  else:
    if(hand.artillery <= hand.infantry):
      #hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["artillery"])])
      #hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand["infantry"] - hand["artillery"])])
      hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.artillery)])
      hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand.infantry - hand.artillery)])
    else:
      #hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["infantry"])])
      hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.infantry)])
  hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.artillery)])
  hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand.tank)])
  if(defence_flag):
    #hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand["fighter"])])
    hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand.fighter)])
  else:
    #hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand["fighter"])])
    hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand.fighter)])
  if(defence_flag):
    #hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand["bomber"])])
    hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand.bomber)])
  else:
    #hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand["bomber"])])
    hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand.bomber)])
  return hits

######################################################################################
## # STEP 6 # ########################################################################
######################################################################################
def assign_hits(hand, hits, def_profile=["infantry","artillery","tank","fighter","bomber"]):
  #for unit_type in def_profile:
  #  if(hand[unit_type] > 0):
  #    if(hits >= hand[unit_type]):
  #      hits = hits - hand[unit_type]
  #      hand[unit_type] = 0
  #    else:
  #      hand[unit_type] = hand[unit_type] - hits
  #      return hand
  if(hand.infantry > 0):
    if(hits >= hand.infantry):
      hits = hits - hand.infantry
      hand.infantry = 0
    else:
      hand.infatry = hand.infantry - hits
      return hand
    
  if(hand.artillery > 0):
    if(hits >= hand.artillery):
      hits = hits - hand.artillery
      hand.artillery = 0
    else:
      hand.artillery = hand.artillery - hits
      return hand
  





######################################################################################
## # # # #############################################################################
######################################################################################
def evaluate_ipc(hand):
  ipc_value = 0
  for unit_type in hand.keys():
    match unit_type:
      case "infantry":
        ipc_value += hand["infantry"] * 3
      case "artillery":
        ipc_value += hand["artillery"] * 4
      case "tank":
        ipc_value += hand["tank"] * 6
      case "fighter":
        ipc_value += hand["fighter"] * 10
      case "bomber":
        ipc_value += hand["bomber"] * 12
  return ipc_value