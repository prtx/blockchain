import flask
from blockchain import BlockChain

app = flask.Flask(__name__)
blockchain = BlockChain()


@app.route('/', methods=['GET'])
def view_chain():
    chain = blockchain.get_data()
    return flask.jsonify({
        'pickle'         : blockchain.pickle(),
        'chain'          : chain,
        'chain_length'   : len(chain),
        'unmined'        : blockchain.unmined_transactions,
        'unmined_length' : len(blockchain.unmined_transactions),
        'valid'          : blockchain.isvalid(),
    }), 200


@app.route('/add', methods=['POST'])
def add_transaction():
    transaction = flask.request.form.get('transaction')
    blockchain.add_transaction(transaction)
    return "Success", 201


@app.route('/mine', methods=['GET'])
def mine():
    chain = blockchain.mine()
    return "Success", 200


if __name__ == '__main__':
    app.run(debug=True)
