# units.py
class Unit:
    def __init__(self, name, strength, agility, hp, field_position):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.hp = hp
        self.field_position = field_position

def create_unit(stats):
    required_fields = ["Name:", "Strength:", "Agility:", "HP:", "Field Position:"]
    
    for field in required_fields:
        if not stats[field]:
            print(f"Error: {field} cannot be empty.")
            return None

    try:
        strength = float(stats["Strength:"]) if stats["Strength:"] else 0.0
        agility = float(stats["Agility:"]) if stats["Agility:"] else 0.0
        hp = float(stats["HP:"]) if stats["HP:"] else 0.0
    except ValueError:
        print("Invalid input for numeric stats. Please enter valid numeric values.")
        return None

    name = stats["Name:"]
    field_position = stats["Field Position:"]
    
    return Unit(name, strength, agility, hp, field_position)
