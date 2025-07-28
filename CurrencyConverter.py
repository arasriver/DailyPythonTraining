print("***Currency Convertor***")


def amount():
    value = int(input("Enter the amount: "))
    return value


def currency():
    currency_name = input("Enter the currency(USD/EUR): ").lower().strip()
    return currency_name


def convert(amount, first_currency, second_currency):
    if first_currency == "usd":
        print(f"{amount} USD is equal to {amount * 0.5} EUR")
    else:
        print(f"{amount} EUR is equal to {amount * 2} USD")


while True:
    value = amount()
    if value > 0:
        break
    else:
        print("Enter a valid amount")
        continue


while True:
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



