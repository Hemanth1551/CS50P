import requests
import sys
# it will requests the website data for displaying
if len(sys.argv) == 2 :
    try :
        value =float(sys.argv[1])
    except :
        print("Command-line argument is not a number")
        sys.exit(1)
else :
    print("Missing command-line argument")
    sys.exit(1)
try :
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amount = bitcoin * value
    print(f"${total_amount:,.4f}")
except :
    print("RequestException")
    sys.exit(1)
