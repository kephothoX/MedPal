from web3 import Web3
import os

web3 = Web3(Web3.HTTPProvider(f"{os.environ.get('INFURA_ENDPOINT')}"))


def completeTransaction(sender_address: str, receiver_address: str, amount: int) -> str:
    if web3.isConnected():
        sender = Web3.toChecksumAddress(sender_address)
        receiver = Web3.toChecksumAddress(receiver_address)
        private_key = os.environ.get("PRIVATE_KEY")

        tx = {
            "from": sender,
            "to": receiver,
            "value": amount,
            "gas": 21000,
            "gasPrice": web3.toWei("50", "gwei"),
            "nonce": web3.eth.getTransactionCount(sender),
        }

        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return f"{web3.toHex(tx_hash)}"

    else:
        return "Web3 is not connected"

    return "Transaction Failed"
