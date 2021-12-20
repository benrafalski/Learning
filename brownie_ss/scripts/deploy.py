from brownie import accounts, SimpleStorage, network, config

import os

def deploy_simple_storage():
    # using accounts lib
    # account = accounts[0]
    # account = accounts.load('test-account')
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1) # waits 1 block
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.load('test-account')

def main():
    print(os.getenv("WEB3_INFURA_PROJECT_ID"))
    deploy_simple_storage()