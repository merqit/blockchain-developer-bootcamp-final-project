from brownie import CooganCoin, accounts, config
from scripts.helpful_scripts import get_coog
import time

STATIC_SEED = 123

def main():
    dev = accounts.add(config['wallets']['from_key'])
    coogan_coin = CooganCoin[len(CooganCoin) - 1]
    transaction = coogan_coin.createCollectible("None", {"from": dev})
    transaction.wait(1)
    time.sleep(45)
    requestId = transaction.events['requestedCollectible']['requestID']
    token_id = coogan_coin.requestIdToTokenId(requestId)
    coog = get_coog(coogan_coin.tokenIdToCoog(token_id))
    print('Coogan appreciation level of tokenID {} is {}'.format(token_id, coog))