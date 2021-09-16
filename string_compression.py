def string_comp(string: str) -> str:

    current_character = ""
    current_character_count = 0
    output_string = ""
    character_list = string.split("") // ['a', 'a', 'b', ...]
    for character in range(len(character_list)):
        if character_list[character] == current_character:
            current_character_count += 1
    else:
        output_string.append(current_character + current_character_count)
        current_character = character_list[character]
    current_character_count = 0
    return output_string
