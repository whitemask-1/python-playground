def create_character(name, strength, intelligence, charisma):
    if type(name) != str:
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif name.replace(" ", "") != name:
        return "The character name should not contain spaces"
    
    attributes = [strength, intelligence, charisma]
    if not all(isinstance(attr, int) for attr in attributes):
        return "All attributes must be integers"
    elif any(attr < 1 for attr in attributes):
        return "Alls stats should be no less than 1"
    elif any(attr >4 for attr in attributes):
        return "All stats should be no more than 4"
    elif sum(attributes) != 7:
        return "The character should start with 7 points."
    
    character = f"""
        name: {name},
        strength: {strength},
        intelligence: {intelligence},
        charisma: {charisma}
    """
    return character

character1 = create_character("Aria", 3, 3, 1)
character2 = create_character("Brax", 4, 2, 1)
character3 = create_character("Luna", 2, 4, 1)
print(character1)
print(character2)
print(character3)