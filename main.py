from gameModes import playGame

if __name__ == "__main__":

    print("""select game mode:
          1 -> bvb
          2 -> pvb
          3 -> pvp""")
    console_input = input()
    match console_input:
        case '1': playGame(True, True)
        case '2': playGame(False, True)
        case '3': playGame(False, False)
