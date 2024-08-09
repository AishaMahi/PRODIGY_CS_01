from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def caesar_cipher(text, shift, operation):
    lower_case = list("abcdefghijklmnopqrstuvwxyz")
    upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    result_text = ""

    for char in text:
        if char in lower_case:
            position = lower_case.index(char)
            new_position = (position + shift) % 26 if operation == "encrypt" else (position - shift + 26) % 26
            result_text += lower_case[new_position]
        elif char in upper_case:
            position = upper_case.index(char)
            new_position = (position + shift) % 26 if operation == "encrypt" else (position - shift + 26) % 26
            result_text += upper_case[new_position]
        else:
            result_text += char
    
    return result_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    text = data['message']
    shift = int(data['shift'])
    operation = data['operation']
    
    result = caesar_cipher(text, shift, operation)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
