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

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 5777
my_address = "0x56FBdD547F14Afa5492067F719860a10B0BFDe4c"
# never hard code this private key -> use an env var
private_key = os.getenv("PRIVATE_KEY")
print(private_key)

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
print(signed_txn)


