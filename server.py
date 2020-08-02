from flask import Flask, render_template, request
import markovify

with open("text.txt") as f:
    text = f.read()
    text_model = markovify.Text(text)

app = Flask(__name__)

@app.route('/')
def generate():

    start_text = request.args.get('start_text', None)

    if start_text:
        try:
            first, second = start_text.split()[:2]
            generated = text_model.make_sentence(init_state=(first, second))
        except Exception as e:
            print(e)
            generated = "У меня не получилось"
    else:
        generated = text_model.make_sentence()

    return render_template('index.html', text=generated)

app.run(debug=True)