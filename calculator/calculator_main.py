def take_unit_count(offence, defence):
  print (offence)
  print (evaluate_ipc(offence))
  print (defence)
  print (evaluate_ipc(defence))


def round(offence, defence):
  return [offence,defence]

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