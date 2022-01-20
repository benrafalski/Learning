from brownie import network
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIORNMENTS, get_account, fund_with_link
import pytest
from scripts.deploy_lottery import deploy_lottery
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIORNMENTS:
        pytest.skip
    lottery = deploy_lottery()
    account = get_account(id='test-wallet')
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    fund_with_link(lottery)
    lottery.endLottery({"from": account})
    time.sleep(60)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0