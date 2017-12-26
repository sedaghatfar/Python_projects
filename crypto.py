# -*- encoding: utf8 -*-


import json
import requests
import datetime
import locale


def getTokenPrice(token, fiat="usd"):
    cmc_ark = json.loads(requests.get("https://api.coinmarketcap.com/v1/ticker/"+token+"/?convert="+fiat).text)
    try:
        return float(cmc_ark[0]["price_%s" % fiat])
    except requests.ConnectionError:
        return 1
    except KeyError:
         return("Currency not found")

ARK = getTokenPrice("Ark")
BTC = getTokenPrice("Bitcoin")
OMG = getTokenPrice("OmiseGO")
ETH = getTokenPrice("Ethereum")
LTC = getTokenPrice("Litecoin")
ENG = getTokenPrice("Enigma-project")
XRP = getTokenPrice("Ripple")

current = (ARK * 1 + BTC * 1 + OMG * 1 + ETH * 1 + LTC * 1 + ENG * 1 + XRP * 1)
print datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
print "ARK : " + str(ARK)
print "BTC : " + str(BTC)
print "ENG : " + str(ENG)
print "ETH : " + str(ETH)
print "LTC : " + str(LTC)
print "OMG : " + str(OMG)
print "XRP : " + str(XRP)

print "\nCurrent value is ${:,.2f}\n".format(current)
