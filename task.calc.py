import logging
import sys
logging.basicConfig(level=logging.DEBUG)

calculation_type = float(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
number1 = float(input('Podaj składnik 1: '))
number2 = float(input('Podaj składnik 2: '))

def calculator(calculation_type, number1, number2): 
    if calculation_type == 1:
        logging.debug('dodaje %s oraz %s' % (number1, number2))
        calc = number1 + number2
    elif calculation_type == 2:
        logging.debug('odejmuje %s oraz %s' % (number1, number2))
        calc = number1 - number2
    elif calculation_type == 3:
        logging.debug('mnoze %s oraz %s' % (number1, number2))
        calc = number1 * number2
    elif calculation_type == 4: 
        logging.debug('dziele %s oraz %s' % (number1, number2))
        calc = number1 / number2
    else:
        logging.debug('sth wrong')
    if calc.is_integer():
        calc = int(calc)
    return calc

if __name__ == '__main__': 
    print('Twój wynik to: %s' %calculator(calculation_type, number1, number2))


