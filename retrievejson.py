# This file retrieves the json data from
# https://www.alphavantage.co/support/#api-key
import json, requests
API_key = 'ZLP5TK3FDZ1EGJ7V'
def exchg_rate(from_rate, to_rate):
    """   exchg_rate: A function that takes in
                from _rate and to _rate(strings) : Strings consisting of three capital letters, that is a currency code
                existing in  physical_currency_list.csv
                return list of len 3 [string, string, float]:   From_currency_name, To_currency_name,
                                                            exchange rate rounded to third decimal for from_rate/ to_rate """
    #retrieve json with alphavantage API
    url = '''https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'''.format(from_rate, to_rate, API_key)
    response = requests.get(url)
    response.raise_for_status()

    # Load Json data into Python variable
    currencydata = json.loads(response.text)['Realtime Currency Exchange Rate']
    rate = float(currencydata ['5. Exchange Rate'])
    from_cur = currencydata["1. From_Currency Code"]
    to_cur = currencydata['3. To_Currency Code']
    return list([from_cur, to_cur, round(rate, 3)])


