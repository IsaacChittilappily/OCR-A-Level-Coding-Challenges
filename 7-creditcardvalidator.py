cardNum = input("Enter a credit card number: ")

def validate_credit_card(card_num):
    
    card_digits = [int(x) for x in card_num if x.isdigit()]
    for i in range(len(card_digits)-2, -1, -2):
        card_digits[i] *= 2
      
        if card_digits[i] > 9:
            card_digits[i] -= 9
          
    return sum(card_digits) % 10 == 0


print(validate_credit_card(cardNum))