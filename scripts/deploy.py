from brownie import accounts, config, register, network

# import os  # if you are importing from env but not config


def deploy_register():
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    # account = accounts[0]
    Register = register.deploy({"from": account})  # deploy register
    stored_value = Register.SeeRegistration()  # for retreive
    print(stored_value)
    transaction = Register.RegistrationNumber(15, {"from": account})  # enter value
    # print(transaction)
    transaction.wait(1)
    updated_stored_value = Register.SeeRegistration()  # see update value
    print(updated_stored_value)
    # account = account[0]
    # print(account)
    # account = accounts.load("myaccount")  # 1 most secuere method this load will take my original account and keep private key safe(not environment variable)
    # print(account)
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)
    # 2 method to save with environment variable

    # print(account)  # advance of 2 method
    # 0xa6b38802D1C584B606Bf9413B6e343Ff38e45178


def get_account():
    if network.show_active() == "development":
        return accounts[0]
        # this keyworkd network will check the network we are working on
        # brownie run scripts/deploy.py --network rinkeby
        # brownie run scripts/deploy.py
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():  # this deifine that print what ever is inside that zac variable(which is logical operator)
    deploy_register()
