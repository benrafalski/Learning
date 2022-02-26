


from scripts.helpful_scripts import get_account
from brownie import config, network, interface
from scripts.get_weth import get_weth
from web3 import Web3

# 0.1
amount = Web3.toWei(0.01, "ether")


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    # print(network.show_active())
    if network.show_active() in ["mainnet-fork"]:
        get_weth(ID=None)
    lending_pool = get_lending_pool()
    approve_erc20(amount, lending_pool.address, erc20_address, account)
    print("depositing")
    tx = lending_pool.deposit(erc20_address, amount, account.address, 0, {"from": account})
    tx.wait(1)
    print("deposited!")
    borrowable_eth, total_debt = get_borrowable_data(lending_pool=lending_pool, account=account)
    # borrowing dai
    dia_eth_price = get_assest_price(config["networks"][network.show_active()]["dai_eth_price_feed"])

def get_assest_price(price_feed_address):
    dai_eth_price_feed = interface.IAggregatorV3(price_feed_address)

   
    latest_price = dai_eth_price_feed.latestRoundData()[1]
    print(f"dai/eth price : {latest_price}")
    return (float(latest_price))


def get_borrowable_data(lending_pool, account):
    (total_collateral_eth, total_debt_eth, available_borrow_eth, current_liquidation_threshold, ltv, current_health_factor) = lending_pool.getUserAccountData(account.address)
    available_borrow_eth = Web3.fromWei(available_borrow_eth, "ether")
    total_collateral_eth = Web3.fromWei(total_collateral_eth, "ether")
    total_debt_eth = Web3.fromWei(total_debt_eth, "ether")
    print(f"available to borrow : {available_borrow_eth}")
    print(f"total collateral : {total_collateral_eth}")
    print(f"total debt : {total_debt_eth}")
    return (float(available_borrow_eth), float(total_debt_eth))

def approve_erc20(amount, spender, erc20_address, account):
    print("approving erc20")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from": account})
    tx.wait(1)
    print("approved!")
    return tx

def get_lending_pool():
    lending_pool_addresses_provider = interface.ILendingPoolAddressProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
