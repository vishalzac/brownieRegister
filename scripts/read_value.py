from brownie import accounts, config, register


def read_contract():
    Register = register[0]
    print(Register.SeeRegistration())


def main():
    read_contract()
