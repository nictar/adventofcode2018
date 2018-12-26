def day14():
    PUZZLE_INPUT = 793031

    scoreboard = '37'
    elf1 = 0
    elf2 = 1

    while str(PUZZLE_INPUT) not in scoreboard[-7:]:
        scoreboard += str(int(scoreboard[elf1]) + int(scoreboard[elf2]))
        elf1 = (elf1 + 1 + int(scoreboard[elf1])) % len(scoreboard)
        elf2 = (elf2 + 1 + int(scoreboard[elf2])) % len(scoreboard)

    print(f'Part 1: {scoreboard[PUZZLE_INPUT:PUZZLE_INPUT+10]}')
    print(f'Part 2: {scoreboard.index(str(PUZZLE_INPUT))}')


if __name__ == "__main__":
    day14()
