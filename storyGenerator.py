import openai
from flask import Flask, session, render_template, request, g 

app = Flask(__name__)

openai.api_key = "INSERT API KEY HERE"

@app.route('/')
def hello_world():
    return render_template("generator.html")

@app.route('/submit-form', methods=["POST"])
def promptFunc():
    option = request.form['option']
    print(option)
    prompt = "Write a short story where the story genre is" + request.form['genre'] + ", the stories main event is: " + request.form['event'] + ", express that the character felt like this: " + request.form['feeling'] + ", also express this lesson that they learned" + request.form['lesson'] + ", Express this story " + option +"."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
    )
    data = response.choices[0].text
    print(response.choices[0].text)
    if (data):
        return render_template("generator.html", output = data)



if __name__ == '__main__':
    app.run()