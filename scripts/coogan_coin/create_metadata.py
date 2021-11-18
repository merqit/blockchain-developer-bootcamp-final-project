from brownie import CooganCoin, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_coog
from pathlib import Path
import os
import requests
import json

coog_to_image_uri = {
    "superfan": "https://ipfs.io/ipfs/QmWXCtjwzRPrf6bFRzh58BNd9FaQPySPUdMXek4tMYrnoo?filename=superfan.png",
    "fanatic": "https://ipfs.io/ipfs/QmWYDwuPjZnE5yzxN4K2LbX4B6gMumjWMbFRswFQJekWym?filename=fanatic.png",
    "fan": "https://ipfs.io/ipfs/QmcDYq1zuyqPUP6PNRw16LTsNLD6sFpQo2QRv1YjRZNrwE?filename=fan.png"

}

def main ():
    print("Working on " + network.show_active())
    coogan_coin = CooganCoin[len(CooganCoin) - 1]
    number_of_tokens = coogan_coin.tokenCounter() 
    print("The number of people you have helped in their journey to Web3 is {}".format(number_of_tokens))
    write_metadata(number_of_tokens, coogan_coin)

def write_metadata(number_of_tokens, nft_contract):
    for token_id in range(number_of_tokens):
        collectible_metadata = sample_metadata.metadata_template
        coog = get_coog(nft_contract.tokenIdToCoog(token_id))
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active()) + str(token_id)
            + "-" + coog + ".json"
        )
        # ./metadata/rinkeby/0-FANATIC.json
        if Path(metadata_file_name).exists():
            print("{} already found!".format(metadata_file_name))
        else:
            print("Creating Metadata File {}".format(metadata_file_name))
            collectible_metadata["name"] = get_coog(
                nft_contract.tokenIdToCoog(token_id))
            collectible_metadata["description"] = "A grateful student and not weird {}".format(
                collectible_metadata["name"])
            image_to_upload = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_path = "./img/{}.png".format(
                    coog.lower().replace("_", "-"))
                image_to_upload = upload_to_ipfs(
                    image_path)
            image_to_upload = coog_to_image_uri[coog] if not image_to_upload else image_to_upload
            collectible_metadata["image"] = image_to_upload
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)




# http://127.0.0.1:5001
# curl -X POST -F file=@img/fan.png http://127.0.0.1:5001/api/v0/add
# curl -X POST -F file=@img/fanatic.png http://127.0.0.1:5001/api/v0/add
# curl -X POST -F file=@img/superfan.png http://127.0.0.1:5001/api/v0/add

def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://localhost:5001"
        response = requests.post(
            ipfs_url + "/api/v0/add", files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        uri = "https://ifps.io/ipfs/{}?filename={}".format(
            ipfs_hash, filename)
        print(uri)
        return uri
    return None
        
            


            


        