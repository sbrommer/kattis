def win(word, guesses):
    guessed = set()
    gallows = 0

    for guess in guesses:
        guessed.add(guess)

        if word.issubset(guessed):
            return True

        gallows += guess not in word

        if gallows == 10:
            return False


word = set(input())
guesses = input()


print('win' if win(word, guesses) else 'lose')
