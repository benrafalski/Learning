from brownie import accounts, network

LOCAL_BLOCKCHAIN_ENVIORNMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIORNMENTS = ["mainnet-fork", "mainnet-fork-dev"]


DECIMALS = 8
STARTING_PRICE = 200000000

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIORNMENTS or network.show_active() in FORKED_LOCAL_ENVIORNMENTS):
        return accounts[0]