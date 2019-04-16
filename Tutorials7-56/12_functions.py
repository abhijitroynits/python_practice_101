# Breaking a big computer program into manageable chunks
# is akin to the idea of creating functions


def print_msg():
    print('print_msg() called \n')


def bitcoin_to_usd(btc):
    print('bitcoin_to_usd() called')
    amount = btc * 5056.31;
    print(btc,"bitcoins=", amount, "USD \n")


print_msg()
print_msg()
bitcoin_to_usd(3)
bitcoin_to_usd(0.87)

