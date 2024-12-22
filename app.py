from flask import Flask, render_template, request

app = Flask(__name__)

# Caesar Cipher Function
def caesar(original_text, shift_amount, encode_or_decode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter.isalpha():
            is_upper = letter.isupper()
            base = ord('A') if is_upper else ord('a')
            shifted_char = chr((ord(letter) - base + shift_amount) % 26 + base)
            output_text += shifted_char
        else:
            output_text += letter
    return output_text

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        direction = request.form.get("direction")
        text = request.form.get("text")
        shift = int(request.form.get("shift"))
        result = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        return render_template("index.html", result=result, original_text=text, direction=direction)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1')
