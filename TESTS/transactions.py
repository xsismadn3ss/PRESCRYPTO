from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware

api = "HTTP://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(api))

key_1 = "0x736632f0a42dd0fe5027d540eb54d6fcf34190e1b93a4156e58a2a753c9af9a4"
key_2 = "0x0c8179cc4783e4d7263aa2c17a5e211fccda1366645284b0327fba28d606e21e"
account_1 = w3.eth.account.from_key(key_1)
account_2 = w3.eth.account.from_key(key_2)

balance1 = w3.from_wei(w3.eth.get_balance(account_1.address), "ether")
print(round(balance1, 4), " ETH")

# make transaction
w3.eth.send_transaction(
    {"from": account_2.address, "value": w3.to_wei(3, "ether"), "to": account_1.address}
)

# Add account_2 as auto-signer:
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account_2))

#hacer transaccion
