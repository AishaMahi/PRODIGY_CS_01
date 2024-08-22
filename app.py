from flask import Flask, render_template, request

app = Flask(__name__)

def encryption(plain_text, shift_key):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_text = ''

    for char in plain_text:
        if char in lower_case:
            position = lower_case.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += lower_case[new_position]
        elif char in upper_case:
            position = upper_case.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += upper_case[new_position]
        else:
            cipher_text += char

    return cipher_text

def decryption(cipher_text, shift_key):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plain_text = ''

    for char in cipher_text:
        if char in lower_case:
            position = lower_case.index(char)
            new_position = (position - shift_key + 26) % 26
            plain_text += lower_case[new_position]
        elif char in upper_case:
            position = upper_case.index(char)
            new_position = (position - shift_key + 26) % 26
            plain_text += upper_case[new_position]
        else:
            plain_text += char

    return plain_text

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        action = request.form.get('action')
        text = request.form.get('text')
        shift = request.form.get('shift')

        try:
            shift_key = int(shift)
        except ValueError:
            result = "Invalid shift key"
        else:
            if action == 'encrypt':
                result = encryption(text, shift_key)
            elif action == 'decrypt':
                result = decryption(text, shift_key)
            else:
                result = "Invalid action"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
