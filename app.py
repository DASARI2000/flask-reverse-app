from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/strings_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class StringEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(255), nullable=False)
    reversed = db.Column(db.String(255), nullable=False)
    uppercased = db.Column(db.String(255), nullable=False)
    trimmed = db.Column(db.String(255), nullable=False)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.json
    original_string = data.get('string', '')
    reversed_string = original_string[::-1]
    uppercased_string = original_string.upper()
    trimmed_string = original_string.strip()

    # Store in database
    entry = StringEntry(
        original=original_string,
        reversed=reversed_string,
        uppercased=uppercased_string,
        trimmed=trimmed_string
    )
    db.session.add(entry)
    db.session.commit()

    return jsonify({
        'reversed': reversed_string,
        'uppercased': uppercased_string,
        'trimmed': trimmed_string
    }), 200

@app.route('/strings', methods=['GET'])
def get_strings():
    entries = StringEntry.query.all()
    return jsonify([{
        'original': e.original,
        'reversed': e.reversed,
        'uppercased': e.uppercased,
        'trimmed': e.trimmed
    } for e in entries]), 200

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
