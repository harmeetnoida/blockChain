import hashlib
import json
from time import time
chain = []
def block(proof, previous_hash=None):
    transaction = {
        'sender': 'Satoshi',
        'recipient': 'Mike',
        'amount': '5 ETH'
    }
    data = {
        'block height': 1,
        'timestamp': time(),
        'transactions': transaction,
        'Block Reward':'2.51335502599523068 Ether (2 + 0.45085502599523068 + 0.0625)',
        'Uncles Reward':'1.75 Ether (1 uncle at Position 0)',
        'Difficulty':'7,289,581,486,456,702',
        'Total Difficulty':'28,070,564,887,730,925,559,072',
        'Size':'66,736 bytes',
        'Gas Used':'14,974,639 (99.93%)',
        'Gas Limit':'14,985,274',
        'proof': proof,
        'previous_hash': previous_hash,
    }
    chain.append(data)
    print("block information:", data)
    string_object = json.dumps(data)
    block_string = string_object.encode()
    raw_hash = hashlib.sha512(block_string)
    hex_hash = raw_hash.hexdigest()
    print("Hash code of block:", hex_hash)
block(previous_hash="No previous Hash. Since this is the first block.", proof=000)