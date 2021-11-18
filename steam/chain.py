import json
import time
from dataclasses import dataclass, field
from hashlib import sha256
from typing import List


@dataclass
class Chain:
    blockchain: List = field(default_factory=list)
    pending: List = field(default_factory=list)

    def __post_init__(self):
        self.add_block(proof=123, prev_hash="Genesis")

    def add_block(self, proof: int, prev_hash: str = None):
        block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "transactions": self.pending,
            "proof": proof,
            "prev_hash": prev_hash or self.compute_hash(self.blockchain[-1]),
        }
        self.blockchain.append(block)
        self.pending = []

    def add_transaction(self, sender: str, receiver: str, amount: float):
        transaction = {"sender": sender, "receiver": receiver, "amount": amount}
        self.pending.append(transaction)
        return transaction

    def compute_hash(self, block):
        json_block = json.dumps(block, sort_keys=True).encode()
        current_hash = sha256(json_block).hexdigest()
        return current_hash


if __name__ == "__main__":
    chain = Chain()

    t1 = chain.add_transaction(sender="Alice", receiver="Bob", amount=10)
    t2 = chain.add_transaction(sender="Bob", receiver="Charlie", amount=125)
    t3 = chain.add_transaction(sender="Jobs", receiver="Bob", amount=665)

    chain.add_block(1001)

    t4 = chain.add_transaction(sender="Julie", receiver="Allen", amount=50)
    t5 = chain.add_transaction(sender="Spidey", receiver="Miles", amount=2)
    t6 = chain.add_transaction(sender="Gretta", receiver="Vikas", amount=1000)

    chain.add_block(1002)

    for blk in chain.blockchain:
        print(blk)
