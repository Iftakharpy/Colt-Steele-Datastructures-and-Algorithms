def is_alpha_numeric(character):
    if 48 <= ord(character) <= 57: #if character is [0-9]
        return True
    elif 97 <= ord(character) <= 122: #if character is [a-z]
        return True
    return False


def character_count(sentence):
    character_counts = {} # dict to keep track of character numbers
    
    for character in sentence:
        # converting the character to lower case
        character = character.lower()
        
        # checking if the character is valid for us.
        if is_alpha_numeric(character): 
            # if character exists in the dict or object then increment else initiate 1
            if character_counts.get(character):
                character_counts[character] += 1
            else:
                character_counts[character] = 1

    return character_counts

#demo
print(character_count(input("Enter some String:\n")))