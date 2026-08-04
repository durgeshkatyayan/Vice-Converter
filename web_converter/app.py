from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Route 2: API endpoint to handle text translation
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text_to_translate = data.get('text', '')
    target_lang = data.get('target_lang', 'es') 

    if not text_to_translate:
        return jsonify({'error': 'No text provided'}), 400

    try:
        translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text_to_translate)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Running on port 5000. '0.0.0.0' allows access from your local network (like your phone)
    app.run(host='0.0.0.0', port=5000, debug=True)