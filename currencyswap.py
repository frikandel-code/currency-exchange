# currencyswap.py
import requests

def get_currency_swap_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

def main():
    base_currency = input("enter the base currency(exampe: USD, EUR): ").upper()
    target_currency = input("enter the target currency(exampe: INR, GBP): ").upper()
    amount = float(input(f"enter the amount in {base_currency}: "))

    try:
        rate = get_currency_swap_rate(base_currency, target_currency)

        swapped_amount = amount * rate
        print(f"{amount} {base_currency} is equal to {swapped_amount:.2f} {target_currency} at a rate of {rate:.4f}.")
    except:
        print("An error occurred while fetching the exchange rate. Please check the currency codes and try again.")

if __name__ == "__main__":
            main()
