from brownie import CooganCoin
from scripts.helpful_scripts import fund_coogan_coin

def main():
    coogan_coin = CooganCoin[len(CooganCoin)-1]
    fund_coogan_coin(coogan_coin)