import pytest
from brownie import network, CooganCoin
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import time


def test_can_create_coogan_coin_integration(
    get_keyhash,
    chainlink_fee,
):
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    coogan_coin = CooganCoin.deploy(
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        get_keyhash,
        {"from": get_account()},
    )
    get_contract("link_token").transfer(
        coogan_coin.address, chainlink_fee * 3, {"from": get_account()}
    )
    # Act
    coogan_coin.createCollectible("None", {"from": get_account()})
    time.sleep(75)
    # Assert
    assert coogan_coin.tokenCounter() > 0