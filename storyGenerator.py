import openai
from flask import Flask, session, render_template, request, g 

app = Flask(__name__)

# Set up the OpenAI API key
openai.api_key = "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"

@app.route('/')
def hello_world():
    return render_template("generator.html")

@app.route('/submit-form', methods=["POST"])
def promptFunc():
    prompt = "Write a short " + request.form['genre'] + " story about " + request.form['subject'] + ". Let the main characters name be " + request.form['name'] 
    # Call the OpenAI API to generate completion
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
    )
    data = response.choices[0].text
    print(response.choices[0].text)
    if (data):
        return render_template("generator.html", output = data)

def main():
    print("answer each prompt in one word")
    satisfied = False
    '''while(satisfied == False):'''
    name = input("What is your name? ")
    subject = input("What would you like to write a short story about? ")
    genre = input("Name the genre of the story (horror, romance, comedy) ")
    promptFunc(name, subject, genre)
    '''done = input("Are you satisfied with the story? (y/n)")   
    if done == "n":
        promptFunc(name, subject, genre)
    else:
        satisfied = True
    satisfied = True'''

'''main()'''

if __name__ == '__main__':
    app.run()