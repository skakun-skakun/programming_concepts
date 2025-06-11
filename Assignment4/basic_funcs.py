from random import choice


def generate_word(lst):
    word = choice(lst)
    return word, len(word)


def generate_result(guess, secret_word, secret_word_length):
    result = ''
    for i in range(secret_word_length):
        ch = guess[i]
        if ch == secret_word[i]:
            result += "[" + ch.upper() + "]"
        elif ch in secret_word:
            result += "(" + ch + ")"
        else:
            result += ch
        result += " "
    return result

