from brownie import network, config, accounts, MockV3Aggregator, LinkToken, Contract, VRFCoordinatorMock
from web3 import Web3

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
    # else:
    #     return accounts.load('test-wallet')

contract_to_mock = {
    "eth_usd_price_feed": MockV3Aggregator,
    "vrf_coordinator": VRFCoordinatorMock,
    "link_token": LinkToken
}

def get_contract(contract_name, ):
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIORNMENTS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)
    return contract



def deploy_mocks():

    # print(f"an active network is {network.show_active()}")
    print("Deploying mocks...")

    address = get_account()

    if len(MockV3Aggregator) <= 0 :
        MockV3Aggregator.deploy(DECIMALS ,Web3.toWei(STARTING_PRICE, "ether"), {"from": address})
        link_token = LinkToken.deploy({"from": address})
        VRFCoordinatorMock.deploy(link_token.address, {"from": address})
    print("Mocks deployed...")
    