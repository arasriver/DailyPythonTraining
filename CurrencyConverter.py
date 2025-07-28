print("***Currency Convertor***")


def amount():
    value = int(input("Enter the amount: "))
    return value


def currency():
    currency_name = input("Enter the currency: ").lower().strip()
    return currency_name


rates = {
    ("usd", "eur"): 0.5,
    ("eur", "usd"): 2
}


def convert(amount, from_currency, to_currency):
    rate = rates.get((from_currency, to_currency))
    if rate:
        result = amount * rate
        print(f"{amount} {from_currency.upper()} is equal to {result} {to_currency.upper()}")
    else:
        print("Conversion not supported.")

while True:
    value = amount()
    if value > 0:
        break
    else:
        print("Enter a valid amount")
        continue


while True:
    print("Available currencies: ", rates)
    print("Source Currency ")
    first_currency = currency()
    print("Target Currency ")
    second_currency = currency()

    if (first_currency == "usd" or first_currency == "eur") and (second_currency == "usd" or second_currency == "eur"):
        if second_currency != first_currency:
            break
        else:
            print("Enter different currencies")
    else:
        print("Enter a valid currency")
        continue


convert(value, first_currency, second_currency)



