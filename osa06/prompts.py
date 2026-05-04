import sys

def ask_number(question: str, min_limit=0, max_limit=100) -> int:
    """
    Asks the user for a number input with the given text.
    Repeats the question if invalid number is given.
    """
    if min_limit > max_limit:
        raise ValueError(f"Maximum ({max_limit}) must always be larger than minimum ({min_limit})")

    while True:
        try:
            number = int(input(question))

            if number < min_limit or number > max_limit:
                print(f"Give number between {min_limit} and {max_limit}")
                continue

        except ValueError:
            print("Invalid number, try again.")
            continue

        except KeyboardInterrupt:
            print("Goodbye!")
            sys.exit()

        return number
