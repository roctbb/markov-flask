# pip3 install markovify

import markovify

with open("text.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

first, second = input().split()[:2]

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence(tries=100, init_state=(first, second)))
