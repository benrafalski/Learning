from scripts.helpful_scripts import get_account
from brownie import interface, network, config



def main():
    get_weth()

def get_weth():
    account = get_account(id='test-wallet')
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": .01 * 10 ** 18})
    print(f"recieved 0.01 weth")
    return tx

