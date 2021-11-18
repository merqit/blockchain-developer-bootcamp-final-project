from brownie import CooganCoin, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_coog


def main():
    print("Working on " + network.show_active())
    coogan_coin = CooganCoin[len(CooganCoin) - 1]
    breakpoint()
    number_of_coogan_coins = coogan_coin.tokenCounter()
    print(number_of_coogan_coins)