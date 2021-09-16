def string_comp(input_string: str) -> str:
    current_character = ""
    current_character_count = ""
    output_string = ""

    for character in range(len(input_string)):
        if input_string[character] == current_character:
            current_character_count += 1
        else:
            output_string += (current_character + str(current_character_count))
            current_character = input_string[character]
            current_character_count = 1
    output_string += (current_character + str(current_character_count))

    return output_string


def main():
    test_string = "aabcccccaaa"  # length 11
    test_string2 = "abbcc"
    print(string_comp(test_string))


if __name__ == "__main__":
    main()
