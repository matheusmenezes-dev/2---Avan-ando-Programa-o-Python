import forca

def test_check_word(word, guesses, target_checked_word):
    result_checked_word = forca.check_word(word, guesses)
    print(result_checked_word)
    assert result_checked_word == target_checked_word
    print("CHECK WORD PASSED")


if __name__ == '__main__':
    test_check_word("Hello", ["h", "o"], "H***o")