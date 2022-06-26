from brownie import accounts, register


def test_deploy():  # this test word is fuckin important
    # arrange
    account = accounts[0]
    # act
    Register = register.deploy({"from": account})  # deploy register
    starting_value = Register.SeeRegistration()  # for retreive
    expected = 0
    # assert
    assert starting_value == expected


def test_update_deploy():  # this test word is important
    # arrange
    account = accounts[0]
    Register = register.deploy({"from": account})
    # act

    Register.RegistrationNumber(14, {"from": account})
    expected = 14
    # assert
    assert expected == Register.SeeRegistration()
