from scripts.helpful_scripts import get_account, get_contract
from brownie import Lottery


def deploy_lottery():
    account = get_account(id='test-wallet')
    lottery = Lottery.deploy(get_contract("eth_usd_price_feed"))
        get_contract()
    )

def main():
    deploy_lottery()