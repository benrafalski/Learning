from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIORNMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIORNMENTS = ["mainnet-fork", "mainnet-fork-dev"]


DECIMALS = 8
STARTING_PRICE = 200000000


def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIORNMENTS or network.show_active() in FORKED_LOCAL_ENVIORNMENTS):
        return accounts[0]
    else:
        return accounts.load('test-wallet')


def deploy_mocks():

    print(f"an active network is {network.show_active()}")
    print("Deploying mocks...")

    if len(MockV3Aggregator) <= 0 :
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS ,Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
    
    print("Mocks deployed...")
    