from brownie import accounts, SimpleStorage



def deploy_simple_storage():
    # using accounts lib
    account = accounts[0]
    # account = accounts.load('test-account')
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1) # waits 1 block
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def main():
    deploy_simple_storage()