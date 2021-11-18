from brownie import CooganCoin, network, config, accounts
from scripts.helpful_scripts import get_coog

coog_metadata_dic = {
    "superfan": "https://ipfs.io/ipfs/QmWXCtjwzRPrf6bFRzh58BNd9FaQPySPUdMXek4tMYrnoo?filename=superfan.png",
    "fanatic": "https://ipfs.io/ipfs/QmWYDwuPjZnE5yzxN4K2LbX4B6gMumjWMbFRswFQJekWym?filename=fanatic.png",
    "fan": "https://ipfs.io/ipfs/QmcDYq1zuyqPUP6PNRw16LTsNLD6sFpQo2QRv1YjRZNrwE?filename=fan.png"
}

def main ():
    print("Working on " + network.show_active())
    coogan_coin = CooganCoin[len(CooganCoin)-1]
    number_of_coogan_coins = coogan_coin.tokenCounter()
    print("The number of Coogan Coins you've deployed is: "
    + str(number_of_coogan_coins)
    )
    for token_id in range(number_of_coogan_coins):
        coog = get_coog(coogan_coin.tokenIdToCoog(token_id))
        if not coogan_coin.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, coogan_coin, coog_metadata_dic[coog])

def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Thank you Coogan! You can forever see all our appreciation at {}".format(


        )


    )
