#  1. მოცემული 3 მთელი a,b,c != 0 რიცხვებისთვის მოძებნეთ a და
#  b რიცხვებს შორის მოხვედრილი c რიცხვის ჯერადი რიცხვების
#  რაოდენობა ყველა შესაძლო ვარიანტისთვის. თუ რომელიმე
#  a, b-დან ჯერადია c-ს, მაშინ ჩათვალეთ შესაბამისი საზღვარი.
#  მოიფიქრეთ ამოცანის ამოხსნის ალგორითმი, დაწერეთ და გაუშვით პროგრამა ციკლის და რეკურსიის (აგრეთვე range) კონსტრუქციის გამოყენების გარეშე.

# First way
def count_multiples(a, b, c):
    # ვიპოვოთ a-დან და b-დან, რომელია უმცირესი და რომელია უდიდესი
    lower, upper = min(a, b), max(a, b)
    # გამოვითვალოთ უდიდესი ჯერადი
    end = (upper // c) * c
    # გამოვითვალოთ რამდენჯერ ეტევა c მოცემულ დიაპაზონში(უმცირესი რიცხვიდან უდიდესი ჯერადის ჩათვლით)
    return (end - lower) // c + 1

print(count_multiples(15, 3, 3)) # 3, 6, 9, 12, 15 --> 5
print(count_multiples(-10, 10, 4)) # -8, -4, 0, 4, 8 --> 5
print(count_multiples(-20, -5, 5)) # -20, -15, -10, -5 --> 4
print(count_multiples(10, 16, 5)) # 10, 15 --> 2

# Second way(doesn't work when a > b)
def count_multiples2(a, b, c):
    if a % c != 0 and b % c != 0: 
        return (b - a) // c
    return (b - a) // c + 1


print('===========================')
print(count_multiples2(15, 3, 3)) # 3, 6, 9, 12, 15 --> 5
print(count_multiples2(-10, 10, 4)) # -8, -4, 0, 4, 8 --> 5
print(count_multiples2(-20, -5, 5)) # -20, -15, -10, -5 --> 4
print(count_multiples2(10, 16, 5)) # 10, 15 --> 2


def count_multiples(a, b, c):
    # რომელია უდიდესი და რომელია უმცირესი a-დან და b-დან
    lower = min(a, b)
    upper = max(a, b)
    
    # გავიგოთ რომელი ჯერიადია უდიდესი მოცემულ დიაპაზონში(lower to upper)
    greatest = (upper // c) * c
    
    return (greatest - lower) // c + 1

print('===========================')
print(count_multiples(15, 3, 3)) # 3, 6, 9, 12, 15 --> 5
print(count_multiples(-10, 10, 4)) # -8, -4, 0, 4, 8 --> 5
print(count_multiples(-20, -5, 5)) # -20, -15, -10, -5 --> 4
print(count_multiples(10, 16, 5)) # 10, 15 --> 2


