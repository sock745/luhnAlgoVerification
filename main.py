def verification(cardNumber):
    oddSum = 0
#no need for start/end index, -1 reverses
    reversedCardNumba = cardNumba[::-1]
#2 stands for the skip, starting from 0, or int 1, and going to 2, or int 3
    oddDigits = reversedCardNumba[::2]
    for digit in oddDigits:
        oddSum += int(digit)
    evenSum = 0
    evenDigits = reversedCardNumba[1::2]
#same for odd, but starting at 1, which is int 2. this leads to skipping by 2 4 6 8
    for digit in evenDigits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        evenSum += number
    total = oddSum + evenSum
    return total % 10 == 0

def main():
    cardNumber = '1234-5678-9012-345'
#swaps out the given values
    cardTranslate = str.maketrans({'-': '', ' ': ''})
#combines cardTranslate's info w CardNumber
    translatedNumba = card_number.translate(card_translation)

#checking if verification = translated num
    if verification(translatedNumba):
        print('VALID!')
    else:
        print('INVALID!')

main()
