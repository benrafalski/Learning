from brownie import FundMe, network, config, MockV3Aggregator
from brownie_fund_me.scripts.helper_functions import deploy_mocks
from scripts.helper_functions import get_account
from web3 import Web3

def deploy_fund_me():
    account = get_account()
    # if on a persistent network like rinkeby use the associated address
    # else, deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address # uses the most recently deployed mock aggregator

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()