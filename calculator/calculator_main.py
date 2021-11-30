import random

def take_unit_count(offence, defence):
  print(offence)
  #print(evaluate_ipc(offence))
  print(defence)
  #print(evaluate_ipc(defence))

  combat_round(offence,defence)


def combat_round(offence, defence):
  atk_hits = evaluate_hits(offence)
  def_hits = evaluate_hits(defence,True)
  print("attacker hits: " + str(atk_hits))
  print("defender hits: " + str(def_hits))

  assign_hits(offence,def_hits)
  assign_hits(defence,atk_hits)
  print(offence)
  print(defence)
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