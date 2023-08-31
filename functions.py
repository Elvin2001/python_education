# Functions

def bitcoin_to_usd(btc, curs):
    amount = btc * curs
    print(amount)

def getStr(str="Hi"):
    return str + "!!!"

def wordToUpperCase(word):
    return str.upper(word)

bitcoin_to_usd(10, 4100)
bitcoin_to_usd(round(123.5), 4100)
print(getStr())
print(wordToUpperCase("my"))