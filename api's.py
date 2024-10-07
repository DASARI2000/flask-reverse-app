from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.json
    original_string = data.get('string', '')
    reversed_string = original_string[::-1]
    uppercased_string = original_string.upper()
    trimmed_string = original_string.strip()

    return jsonify({
        'reversed': reversed_string,
        'uppercased': uppercased_string,
        'trimmed': trimmed_string
    }), 200

@app.route('/strings', methods=['GET'])
def get_strings():
    return jsonify({"message": "This endpoint is not implemented here only api's implemented."}), 501

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
