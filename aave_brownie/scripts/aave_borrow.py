


from scripts.helpful_scripts import get_account
from brownie import config, network
from scripts.get_weth import get_weth

def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet_fork"]:
        get_weth()
    lending_pool = get_leding_pool()

def get_lending_pool():
    