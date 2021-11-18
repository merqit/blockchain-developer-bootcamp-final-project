import pytest
from brownie import network, CooganCoin
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def test_can_create_coogan_coin(
    get_keyhash,
    chainlink_fee,
):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
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
    transaction_receipt = coogan_coin.createCollectible(
        "None", {"from": get_account()}
    )
    requestId = transaction_receipt.events["requestedCollectible"]["requestId"]
    assert isinstance(transaction_receipt.txid, str)
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, 777, coogan_coin.address, {"from": get_account()}
    )
    # Assert
    assert coogan_coin.tokenCounter() > 0

   