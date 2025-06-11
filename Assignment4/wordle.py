from basic_funcs import generate_word, generate_result

words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
print("Welcome to Wordle!")

while True:
    secret_word, secret_word_length = generate_word(words)
    tries = 6
    print(f"\nGuess the {secret_word_length} - letter word. You have {tries} tries.")
    while tries != 0:
        guess = input(f"Attempt {7 - tries}/6 – Enter guess: ").lower()

        if len(guess) != secret_word_length:
            print("Wrong length. Expected", secret_word_length)
            continue
        if guess == secret_word:
            print("You win!!! The word was:", secret_word)
            break

        print("Result:", generate_result(guess, secret_word, secret_word_length), "\n")
        tries -= 1
    else:
        print("You lose! The word was:", secret_word)
    cont = input("\nShall we continue (type 'e' to exit)? ").lower()
    if cont == "e":
        break
