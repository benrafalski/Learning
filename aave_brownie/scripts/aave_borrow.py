


from scripts.helpful_scripts import get_account
from brownie import config, network, interface
from scripts.get_weth import get_weth

def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet_fork"]:
        get_weth()
    lending_pool = get_lending_pool()
    approve_erc20()

def approve_erc20(amount, spender, erc20_address, account):
    print("approving erc20")
    erc20 = interface.IERC20(erc20_address)

def get_lending_pool():
    lending_pool_addresses_provider = interface.ILendingPoolAddressProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
