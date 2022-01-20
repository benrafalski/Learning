from typing import Collection
from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

# get the .env file contents
load_dotenv()

# opening simple storage solidity file
with open("./simple_storage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)

#  compile the solidity
install_solc("0.6.0")
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"simple_storage.sol": {"content": simple_storage_file}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        },
    },
}, solc_version="0.6.0")

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["simple_storage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["simple_storage.sol"]["SimpleStorage"]["abi"]

# for connecting to rinkeby
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/dd876b0fea794eb28e8022cb127e0f2e"))
chain_id = 4
my_address = "0xb6e2549f020Be31f56C2Eac1E8787b514Fb53Dd6"
# never hard code this private key -> use an env var
private_key = os.getenv("PRIVATE_KEY")
# print(private_key)

# create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# get latest transaction
nonce = w3.eth.getTransactionCount(my_address)
# 1. build a transaction
# 2. sign a transaction
# 3. send a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# send the signed transaction
print("deploying contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("deployed!")

# working with the contract, you always need
# contract address
# contract abi
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi= abi)
# call =  simulate making the call and getting a return value
# transact = actually make a state change
print(simple_storage.functions.retrieve().call()) # returns 0 initially
print(simple_storage.functions.store(15).call()) # doesn't actually store the number, just simulating it with call()

print("updating contract...")
store_transaction = simple_storage.functions.store(15).buildTransaction({
    "chainId": chain_id,
    "gasPrice": w3.eth.gas_price,
    "from": my_address,
    "nonce": nonce+1, # must increment here
})

signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)

store_tx_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
store_tx_receipt = w3.eth.wait_for_transaction_receipt(store_tx_hash)
print("updated!")



