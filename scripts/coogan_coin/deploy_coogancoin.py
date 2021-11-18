from brownie import CooganCoin, accounts, network, config
from brownie.network.main import show_active
from scripts.helpful_scripts import fund_coogan_coin

def main():
   dev = accounts.add(config['wallets']['from_key'])
   print(network.show_active())
   publish_source = False
   coogan_coin = CooganCoin.deploy(
      config['networks'][network.show_active()]['vrf_coordinator'],
      config['networks'][network.show_active()]['link_token'],
      config['networks'][network.show_active()]['keyhash'],
      {"from": dev},
      publish_source=publish_source
   )
   fund_coogan_coin(coogan_coin)
   return coogan_coin