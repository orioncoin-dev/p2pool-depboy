import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'af4576ee'.decode('hex')
P2P_PORT = 10888
ADDRESS_VERSION = 50
RPC_PORT = 10889
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'myriadcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1000*100000000 >> (height + 1)//967680
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('skein_hash').getPoWHash(data))
BLOCK_PERIOD = 30 # s
SYMBOL = 'MYR'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'myriadcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/myriadcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.myriadcoin'), 'myriadcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://altexplorer.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://altexplorer.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://altexplorer.net/tx/'
SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**26 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.0001
