from flask import Flask, request, jsonify
from cipher import CesarCipherAFD

app = Flask(__name__)
afd = CesarCipherAFD()

@app.route('/process', methods=['POST'])
def process_message():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    state = afd.process_string(text)

    if state == False:
        return jsonify({'error': "Texto cifrado incompleto o inválido"}), 400

    result = ''
    if state in ['q1', 'q2']:
        result = afd.encrypt(text)
    elif state == 'q5':
        result = afd.decrypt(text)

    return jsonify({'processed_text': result}), 200
