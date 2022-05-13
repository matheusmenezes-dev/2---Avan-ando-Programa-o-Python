def desenhar_forca(lives, word):
    sep = "            "
    head =  " |      (_)   " if lives < 7 else " |            "
    upper = " |      \     " if lives == 6 else " |            "
    if lives == 4: upper = " |      \|    " 
    if lives < 3: upper = " |      \|/   "
    mid = " |       |    " if lives  < 3 else " |            "
    bottom = " |      /     " if lives == 1 else " |            "
    if lives == 0: bottom = " |      / \    "

    print("  _______     ")
    print(" |/      |    ")
    print(head) 
    print(upper) 
    print(mid) 
    print(bottom) 
    print(" |            ")
    print(" |   ", " ".join(word))
    print("_|___         ")
    
if __name__ == '__main__':
    desenhar_forca(0, "tes_")