import requests

API_KEY = "fca_live_0deHEPBBnmx3RCHrcMXu5ErsM2ECkXv7LsSpZKiq"
BASE_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES= ["USD", "EUR", "RON", "GBP"]

def convert_currency(base):
    #Format as a comma separateed list
    currencies =",".join(CURRENCIES)
    #Construct the URL string 
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    #Make request to the API
    try: 
        response = requests.get(url)
        data = response.json()
        print(data)
        return data
    except Exception as e:
        print(e)
        return None


user_input = input("Enter the currency you want to convert from: ").upper()
convert_currency(user_input)