import requests
import json
import random


def trump_quote():
    url = 'https://api.whatdoestrumpthink.com/api/v1/quotes/random'
    r = requests.get(url)
    quote = json.loads(r.text)
    return quote["message"]


def kanye_quote():
    url = 'https://api.kanye.rest'
    r = requests.get(url)
    quote = json.loads(r.text)
    return quote["quote"]


def main():
    print("Who said what...\n")
    score = 0

    for i in range(10):
        print(f"Question {i+1}\n")
        quotes = [[trump_quote(), "t"], [kanye_quote(), "k"]]

        random.shuffle(quotes)

        print(f'"{quotes[0][0]}"')

        print("Who do you think said the quote, Trump or Kanye? \n")
        while True:
            user_input = input("Press t for trump or press k for Kanye: ")

            if user_input not in ["t", "k"]:
                print("\nInvalid input, try again")
            else:
                break

        if quotes[0][1] == user_input:
            print("\n\nWell done you got it right!")
            score += 1
        else:
            if quotes[0][1] == "t":
                name = "Trump"
            else:
                name = "Kanye"
            print(f"\n\nUnlucky, it was actually {name}")

    print(f"You got {score}/10")


main()
