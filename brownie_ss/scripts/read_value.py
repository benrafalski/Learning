from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1] # uses most recent deploy
    # abi
    # address
    print(simple_storage.retrieve())


def main():
    read_contract()