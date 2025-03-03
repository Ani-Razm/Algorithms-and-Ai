# 1) შექმენით პროგრამა, რომელიც მიიღებს ნებისმიერ პოზიციურ სისტემაში მყოფ რიცხვსა და სასურველ პოზიციურ სისტემას, რომელშიც გადაიყვანს მიღებულ რიცხვს

def converter(n, from_base, to_base):
    decimal = int(n, from_base)

    if to_base == 10:
        return decimal

    result = ''
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while decimal > 0:
        reminder = decimal % to_base
        decimal //= to_base
        result += digits[reminder]
    
    return result[::-1]

print(converter("1000", 10, 16))