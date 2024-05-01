star_wars_characters = ["Luke Skywalker", "Darth Vader", "Leia Organa", "Han Solo", "Obi-Wan Kenobi", "Yoda", "Darth Maul", "Hera Syndulla", "Lando Calrissian"]

sorted_characters = sorted(star_wars_characters)

print("Characters sorted alphabetically:")
for character in sorted_characters:
    print(character)

if "Darth Maul" in star_wars_characters:
    position = star_wars_characters.index("Darth Maul")
    print("Darth Maul is at position:", position)
else:
    print("Darth Maul is not in the list")

hera_index = star_wars_characters.index("Hera Syndulla")
characters_before = star_wars_characters[:hera_index]
characters_after = star_wars_characters[hera_index+1:]

print("Characters before Hera Syndulla:")
for character in characters_before:
    print(character)

print("Characters after Hera Syndulla:")
for character in characters_after:
    print(character)

l_characters = [character for character in star_wars_characters if character.startswith("L")]
print("Characters starting with 'L':")
for character in l_characters:
    print(character)