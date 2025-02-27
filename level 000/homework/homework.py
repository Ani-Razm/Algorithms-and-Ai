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
    upper = (upper // c) * c
    # გამოვითვალოთ რამდენჯერ ეტევა c მოცემულ დიაპაზონში(უმცირესი რიცხვიდან უდიდესი ჯერადის ჩათვლით)
    return (upper  - lower) // c + 1

# Test cases
print(count_multiples(15, 3, 3)) # 3, 6, 9, 12, 15 --> 5
print(count_multiples(-10, 10, 4)) # -8, -4, 0, 4, 8 --> 5
print(count_multiples(-20, -5, 5)) # -20, -15, -10, -5 --> 4
print(count_multiples(10, 16, 5)) # 10, 15 --> 2

# Second way
def count_multiples2(a, b, c):
    a, b = min(a, b), max(a, b)  
    if a % c != 0 and b % c != 0: 
        return (b - a) // c
    return (b - a) // c + 1

# Test cases
print("==========================")
print(count_multiples2(15, 3, 3)) # 3, 6, 9, 12, 15 --> 5
print(count_multiples2(-10, 10, 4)) # -8, -4, 0, 4, 8 --> 5
print(count_multiples2(-20, -5, 5)) # -20, -15, -10, -5 --> 4
print(count_multiples2(10, 16, 5)) # 10, 15 --> 2