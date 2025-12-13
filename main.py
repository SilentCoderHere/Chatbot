from json import load

from helper import getResponse


def main() -> None:
    file = open("words.json", "r")
    words = load(file)

    while True:
        try:
            prompt = input("User: ")
        except (EOFError, KeyboardInterrupt, OSError):
            print("Bot: Goodbye!")
            break

        response = getResponse(prompt, words)

        if response == "bye!":
            print("Bot: Have a nice day! Goodbye!")
            break
        print("Bot:", response)

    file.close()


if __name__ == "__main__":
    main()
