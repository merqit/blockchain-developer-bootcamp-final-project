
(1)
Please install or have installed the following:

    https://nodejs.org/en/download/
    https://www.python.org/downloads/

Install Brownie, if you haven't already. Here is a simple way to install brownie.

    https://eth-brownie.readthedocs.io/en/stable/install.html

sudo npm install -g solc



(2)
git clone https://github.com/merqit/blockchain-developer-bootcamp-final-project.git
cd blockchain-developer-bootcamp-final-project/

$ brownie compile


(3)

Running Scripts

I defaulted to rinkeby since that seems to be the testing standard for NFT platforms. You will need testnet rinkeby ETH and testnet Rinkeby LINK. You can find faucets for both in the Chainlink documentation.

    brownie run scripts/CooganCoin/deploy_coogancoin.py
    brownie run scripts/CooganCoin/fund_collectible.py --network rinkeby
    brownie run scripts/CooganCoin/create_collectible.py --network rinkeby
    brownie run scripts/CooganCoin/create_metadata.py --network rinkeby
    brownie run scripts/CooganCoin/set_tokenuri.py --network rinkeby



(4)

Running Tests