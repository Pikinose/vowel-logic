#code to check wether the given word is a vowel or not.

def checkin(word):
    vowel = "aeiou"
    vowel2 = "AEIOU"
    for characters in vowel, vowel2:
        if characters in vowel and vowel2:
            return True
        else:
            print("Brooo Yoo, its not a vowel word> hehehhe")
