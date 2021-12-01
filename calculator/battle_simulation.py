import random

class battle_simulation:

  def __init__(self,offence,defence,rounds=100):
      self.offence = offence
      self.defence = defence
      self.rounds = rounds

      self.set_class_vars(self)

      self.initial_offence_attack = evaluate_ipc(self.offence)
      self.initial_defence_attack = evaluate_ipc(self.defence)

      battle_main(self.offence,self.defence,self.rounds)
  
  @classmethod
  def set_class_vars(cls,self):
    cls.offence_hand = self.offence
    cls.defence_hand = self.defence


def battle_main(offence, defence, rounds, num_sims=100):
  offence_wins = 0
  defence_wins = 0

  print("In Offence: " + str(offence))
  print("In Defence: " + str(defence))

  for i in range(1,num_sims + 1):
    print()
    print("Combat " + str(i))
    offence_instance = offence
    defence_instance = defence
    result = run_battle(offence_instance, defence_instance, rounds)
    if result == 1:
      defence_wins += 1
    elif result == 0:
      offence_wins += 1
  
  print("Offence wins " + str((offence_wins/num_sims)*100) + "% of the time")
  print("Defence wins " + str((defence_wins/num_sims)*100) + "% of the time")

def run_battle(attacker, defender, rounds):
  round_counter = 0
  while(round_counter < rounds and attacker is not None and defender is not None):
    round_counter += 1
    attacker,defender = combat_round(attacker,defender)
    print("Round: " + str(round_counter))
    print("Offence: " + str(attacker))
    print("Defence: " + str(defender))
  
  if attacker is None:
    return 1
  elif defender is None:
    return 0

def combat_round(offence, defence):
  atk_hits = evaluate_hits(offence)
  def_hits = evaluate_hits(defence,True)
  print("attacker hits: " + str(atk_hits))
  print("defender hits: " + str(def_hits))

  offence = assign_hits(offence,def_hits)
  defence = assign_hits(defence,atk_hits)
  return [offence,defence]

def evaluate_hits(hand, defence_flag=False):
  hits = 0
  for unit_type in hand.keys():
    match unit_type:
        case "infantry":
          if(defence_flag):
            hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["infantry"])])
          else:
            if(hand["artillery"] <= hand["infantry"]):
              hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["artillery"])])
              hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand["infantry"] - hand["artillery"])])
            else:
              hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["infantry"])])

        case "artillery":
          hits += sum([1 if random.randint(1,6) <= 2 else 0 for x in range(hand["artillery"])])

        case "tank":
          hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand["tank"])])

        case "fighter":
          if(defence_flag):
            hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand["fighter"])])
          else:
            hits += sum([1 if random.randint(1,6) <= 3 else 0 for x in range(hand["fighter"])])

        case "bomber":
          if(defence_flag):
            hits += sum([1 if random.randint(1,6) <= 1 else 0 for x in range(hand["bomber"])])
          else:
            hits += sum([1 if random.randint(1,6) <= 4 else 0 for x in range(hand["bomber"])])

  return hits

def assign_hits(hand, hits, def_profile=["infantry","artillery","tank","fighter","bomber"]):
  for unit_type in def_profile:
    if(hand[unit_type] > 0):
      if(hits >= hand[unit_type]):
        hits = hits - hand[unit_type]
        hand[unit_type] = 0
      else:
        hand[unit_type] = hand[unit_type] - hits
        return hand
  
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