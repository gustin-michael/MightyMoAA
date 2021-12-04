from calculator.land_hand import land_hand
import random


class battle_instance:
    def __init__(self,offence,defence,rounds,combat_num):
        self.bat_num = combat_num
        self.off = offence
        self.dfn = defence
        self.rnds = rounds
        self.winner = None
        self.winner_hand = None

        self.initial_ipc_off = evaluate_ipc(self.off)
        self.initial_ipc_def = evaluate_ipc(self.dfn)

        # prep battle
        self.battle_log = []
        self.build_hands()

        # execute battle
        self.run_battle()

        #if(self.winner == "A")

    def build_hands(self):
        offn = land_hand(self.off["infantry"],
                         self.off["artillery"],
                         self.off["tank"],
                         self.off["fighter"],
                         self.off["bomber"])
        defn = land_hand(self.dfn["infantry"],
                         self.dfn["artillery"],
                         self.dfn["tank"],
                         self.dfn["fighter"],
                         self.dfn["bomber"])

        first_turn = {"offence": offn,
                      "defence": defn}
        
        self.battle_log.append(first_turn)

    def run_battle(self):
        round_counter = 0

        new_atk = 1
        new_defr = 1

        while(round_counter < self.rnds and new_atk is not None and new_defr is not None):
            round_counter += 1
            new_atk = self.battle_log[len(self.battle_log)-1]["offence"]
            new_defr = self.battle_log[len(self.battle_log)-1]["defence"]
            #
            combat_return = combat_round(new_atk,new_defr)
            new_atk = combat_return["offence"]
            new_defr = combat_return["defence"]
            self.battle_log.append(combat_return)


  
        if new_atk is None and new_defr is None:
            self.winner = None
        elif new_atk is None:
            self.winner = "DEF"
        elif new_defr is None:
            self.winner = "ATK"

def combat_round(attack,defence):

    atk_hits = evaluate_hits(attack)
    def_hits = evaluate_hits(defence,True)

    ret_atk = assign_hits(attack,def_hits)
    ret_def = assign_hits(defence,atk_hits)
    return {"offence": ret_atk,
            "defence": ret_def}

######################################################################################
## #  # ########################################################################
######################################################################################
def evaluate_hits(hand, defence_flag=False):
    hits = 0
    if(defence_flag):
        hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.infantry)])
    else:
        if(hand.artillery <= hand.infantry):
            hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.artillery)])
            hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand.infantry - hand.artillery)])
        else:
            hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.infantry)])
    hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand.artillery)])
    hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand.tank)])
    if(defence_flag):
        hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand.fighter)])
    else:
        hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand.fighter)])
    if(defence_flag):
        hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand.bomber)])
    else:
        hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand.bomber)])
    return hits

### ##################################################################################
## #  # ########################################################################
######################################################################################
def assign_hits(hand, hits, def_profile=["infantry","artillery","tank","fighter","bomber"]):

    hand_holder = {"infantry": hand.infantry,
                   "artillery": hand.artillery,
                   "tank": hand.tank,
                   "fighter": hand.fighter,
                   "bomber": hand.bomber}

    for unit_type in def_profile:
        if(hand_holder[unit_type] > 0):
            if(hits >= hand_holder[unit_type]):
                hits = hits - hand_holder[unit_type]
                hand_holder[unit_type] = 0
            else:
                hand_holder[unit_type] = hand_holder[unit_type] - hits

                return land_hand(hand_holder["infantry"],
                                 hand_holder["artillery"],
                                 hand_holder["tank"],
                                 hand_holder["fighter"],
                                 hand_holder["bomber"])

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