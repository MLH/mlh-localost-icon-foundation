import ast

from iconsdk.builder.call_builder import CallBuilder
from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet

import config

CASINO_SCORE_ADDRESS = config.CASINO_SCORE_ADDRESS
BET_AMOUNT = config.BET_AMOUNT

icon_service = IconService(HTTPProvider(config.ICON_SERVICE_PROVIDER_URL))

player_wallet = KeyWallet.load(
    config.PLAYER_WALLET_PRIVATE_KEY_FILE_PATH, config.PLAYER_WALLET_PASSWORD
)


def get_wallet_balance(wallet_address):
    # Write code here


def get_casino_balance():
    # Write code here


def get_player_balance():
    # Write code here


# Returns a list of recent transactions
def get_transactions():
    # Write code here


# Create a new transaction and returns its hash
def create_transaction(multiplier=1):
    # Write code here


# Find a transaction by its hash in the list of recent transactions
def get_transaction(txhash):
    # Write code here
