# -*- coding: utf-8 -*-
import json
import logging
from argparse import ArgumentParser

from moneybot.examples.strategies import BuffedCoinStrategy
from moneybot.examples.strategies import BuyHoldStrategy
from moneybot.examples.strategies import PeakRiderStrategy
from moneybot.fund import Fund
from moneybot.market.adapters.live import LiveMarketAdapter


strategies = {
    'buffed-coin': BuffedCoinStrategy,
    'buy-hold': BuyHoldStrategy,
    'peak-rider': PeakRiderStrategy,
}


def main(args):
    with open(args.config) as cfg_file:
        config = json.load(cfg_file)

    fund = Fund(strategies[args.strategy], LiveMarketAdapter, config)
    fund.run_live()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-c', '--config',
        default='config.json.example',
        type=str,
        help='path to config file',
    )
    parser.add_argument(
        '-l', '--log-level',
        default='INFO',
        type=str,
        choices=['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Python logging level',
    )
    parser.add_argument(
        '-s', '--strategy',
        default='buffed-coin',
        type=str,
        choices=strategies.keys(),
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)
    main(args)
