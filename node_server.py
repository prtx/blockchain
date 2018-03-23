import flask
from blockchain import Node

app = flask.Flask(__name__)
node = Node()


@app.route('/', methods=['GET'])
def view_chain():
    chain = node.chain.get_data()
    return flask.jsonify({
        'pickle'         : node.pickle(),
        'chain'          : chain,
        'chain_length'   : len(chain),
        'unmined'        : node.unmined_transactions,
        'unmined_length' : len(node.unmined_transactions),
        'valid'          : node.chain.isvalid(),
    }), 200


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    transaction = flask.request.form.get('transaction')
    node.add_transaction(transaction)
    return "Success", 201


@app.route('/mine', methods=['GET'])
def mine():
    chain = node.mine()
    return "Success", 200


@app.route('/register_peer', methods=['POST'])
def register_peer():
    peer_addr = flask.request.form.get('peer')
    node.register_peer(peer_addr)
    return "Success", 201


@app.route('/consensus')
def consensus():
    node.consensus()
    return "Success", 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int)
    args = parser.parse_args()
    port = args.port

    app.run(debug=True, port=port)
