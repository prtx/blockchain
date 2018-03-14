import flask
import json
from blockchain import Chain as BlockChain

app = flask.Flask(__name__)
blockchain = BlockChain()


@app.route('/', methods=['GET'])
def view_chain():
    chain = blockchain.get_data()
    return flask.jsonify({
        'chain'  : chain,
        'length' : len(chain),
    }), 200


@app.route('/add', methods=['POST'])
def new_transaction_block():
    data     = flask.request.data
    index    = blockchain.register_block(json.loads(data)['transactions'])
    response = {'message': f'Transaction will be added to Block {index}'}

    return flask.jsonify(response), 201


if __name__ == '__main__':
    app.run(debug=True)