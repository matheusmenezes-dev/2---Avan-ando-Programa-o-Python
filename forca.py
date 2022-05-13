import random

words = ["Hello", "World"]

def main():
    guesses = []
    lives = 7
    word = random.choice(words) 
    # O jogador só vence quando todas as letras de "word"
    # estiverem inclusas em "guesses" (tentativas)
    while check_word(word, guesses) != word:
        desenhar_forca(check_word(word, guesses), guesses, lives)
        guess = input("Chute uma letra: \n").lower()
        if not guess in word.lower():
            lives -= 1
            if lives < 0:
                print("Fim de jogo")
                print(f"A palavra era {word}")
                return
            print("Errou! - Tente novamente.")
        guesses.append(guess)
    desenhar_forca(check_word(word, guesses), guesses, lives)
    print("Parabéns, você venceu!")

def check_word(word, guesses):
    checked_list = [letter if letter.lower() in guesses else "_" for letter in word]
    return "".join(checked_list)

# - "Abominantemente ilegivel !! -- repensar.""
# - "mas... mas... são apenas desenhos" =(
def desenhar_forca(word, guesses, lives):
    head =  " |      (_)   " if lives < 7 else " |            "
    upper = " |      \     " if lives == 5 else " |            "
    if lives == 4: upper = " |      \|    " 
    if lives <= 3: upper = " |      \|/   "
    mid = " |       |    " if lives  < 3 else " |            "
    bottom = " |      /     " if lives == 1 else " |            "
    if lives == 0: bottom = " |      / \    "

    print("  _______     ")
    print(" |/      |    ")
    print(head) 
    print(upper) 
    print(mid, "   ", " ".join(guesses)) 
    print(bottom) 
    print(" |            ")
    print(" |   ", " ".join(word))
    print("_|___         ")
    print(lives)

if __name__ == '__main__':
    main()