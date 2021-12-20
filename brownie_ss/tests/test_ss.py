from brownie import SimpleStorage, accounts

# test function
def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0 # passed because 0 is expected value to start
    # expected = 9 # does not pass, should be 0 to start
    # assert
    assert starting_value == expected



def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # act
    expected = 15 
    simple_storage.store(expected, {"from": account})
    # assert
    assert expected == simple_storage.retrieve() # gets the new stored value