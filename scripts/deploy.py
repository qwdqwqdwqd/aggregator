#!/usr/bin/python3
import os
from brownie import Aggregator, accounts, network


def main():
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    publish_source = True if os.getenv("BSCSCAN_TOKEN") else False

    contract = Aggregator.deploy(
        os.getenv("ROUTERS").split(','),
        os.getenv("CONNECTORS").split(','), 
        {"from": dev},
        publish_source=publish_source
    )
    print("Aggregator deployed:", contract.address)