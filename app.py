from flask import Flask, render_template
from web3 import Web3


app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
app.config['SECURITY_PASSWORD_SALT']='thisistheSALTforcreatingtheCONFIRMATIONtoken'
app.config['ETH_INFURA_MAINNET_URL'] = 'https://mainnet.infura.io/v3/47d1365cc1d94d70b061dc255574a787' 

address =  Web3.toChecksumAddress("0xea674fdde714fd979de3edf0f56aa9716b898ec8")

web3 = Web3(Web3.HTTPProvider(app.config['ETH_INFURA_MAINNET_URL']))

@app.route('/')
def index():

    is_connected = web3.isConnected()
    latestBlock = web3.eth.blockNumber
    balance = web3.eth.getBalance(address)
    balance = web3.fromWei(balance, "ether")

    return render_template('index.html', data ={"isConnected" : is_connected, "latestBlock" : latestBlock , "address" : address, "balance" : balance })


if __name__ == '__main__':
    
    app.run()
    # app.run(host='127.0.0.1',port=8889,debug=True)