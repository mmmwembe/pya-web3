from flask import Flask, render_template
from web3 import Web3
import os
import json
from brownie import accounts, network, config, Contract

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
app.config['SECURITY_PASSWORD_SALT']='thisistheSALTforcreatingtheCONFIRMATIONtoken'
app.config['ETH_INFURA_MAINNET_URL'] = 'https://mainnet.infura.io/v3/47d1365cc1d94d70b061dc255574a787'
app.config['polygon_testnet_url'] = 'https://rpc-mumbai.matic.today'
app.config['test_token_contract_address'] = '0x96Af83fdD4F82e392a853EDF0Cb989bBb7d1ddb4'
app.config['owner_address'] = '0x8c2282726D51cCdFB9997ede68Be69B9E71cd1F4'  # Token Owner Address
app.config['owner_private_key'] = '0xa4ccdff39271a8135c9336142fb2b59936bb4657088fa03fe28547819ab5ae06'  # Token Owner Private Key


address =  Web3.toChecksumAddress("0xea674fdde714fd979de3edf0f56aa9716b898ec8")

web3 = Web3(Web3.HTTPProvider(app.config['ETH_INFURA_MAINNET_URL']))
web3_polygon_testnet = Web3(Web3.HTTPProvider(app.config['polygon_testnet_url']))

f = open('build/contracts/TestAminaToken.json')
TestAminaToken = json.load(f)

user_eth_address = Web3.toChecksumAddress(os.environ['USER_ETH_ADDRESS']) 


def limitDecimalPlaces(v, decimals):

    if v:
        s1 ="{:.{}f}".format(v, decimals)
    else:
        s1 = v
    return s1

def fromWeiToEth(x):
    return web3.fromWei(x,'ether')

# Get checksum address
def getCheckSumAddress(_address):
    return web3.toChecksumAddress(_address)


def fromWeiToEth2(_web3_connection, x):
    return _web3_connection.fromWei(x,'ether')

# Get checksum address
def getCheckSumAddress2(_web3_connection,_address):
    return _web3_connection.toChecksumAddress(_address)

def getBalanceFromAddress2(_web3_connection,_address, _token):
    _account = getCheckSumAddress2(_web3_connection,_address)
    _bal_in_wei = _web3_connection.eth.get_balance(_account)
    _bal_in_eth = fromWeiToEth2(_web3_connection,_bal_in_wei)
    print('Balance', _bal_in_eth, _token)

    return _bal_in_eth


def updateAccountBalances():

    erc20_address = app.config['test_token_contract_address'] # Token address on polygon_testnet_url
    # erc20 = web3_polygon_testnet.eth.contract(erc20_address, abi=TestAminaToken["abi"])
    erc20 = Contract.from_abi("Arbitrary ERC20", erc20_address, abi=TestAminaToken["abi"])

    user_account = user_eth_address
    balance_in_wei = erc20.balanceOf(user_account)
    balance_in_eth = fromWeiToEth(balance_in_wei)
    balance_formatted = limitDecimalPlaces(balance_in_eth, 5)
    token_name = erc20.name()
    token_symbol = erc20.symbol()

    balance_in_MATIC = getBalanceFromAddress2(web3_polygon_testnet,user_account, 'MATIC')
    balance_formatted_MATIC = limitDecimalPlaces(balance_in_MATIC, 5)

    amina_balance = balance_formatted
    matic_balance = balance_formatted_MATIC 

    return amina_balance, matic_balance


@app.route('/')
def index():

    is_connected = web3.isConnected()
    latestBlock = web3.eth.blockNumber
    balance = web3.eth.getBalance(address)
    balance = web3.fromWei(balance, "ether")
    env = os.environ['SECRET_KEY'] # os.getenv("SECRET_KEY")


    amina_bal, matic_bal = updateAccountBalances()

    return render_template('index.html', data ={"isConnected" : is_connected, "latestBlock" : latestBlock , "address" : address, "balance" : balance , "env" : env , "amina" : amina_bal, "matic": matic_bal})


if __name__ == '__main__':

    app.run()
    # app.run(host='127.0.0.1',port=8889,debug=True)