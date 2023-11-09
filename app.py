from flask import Flask, render_template, jsonify, redirect, url_for, request, json
from dotenv import load_dotenv
import openai
import textwrap
import os

load_dotenv()
API_KEY="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"
openai.api_key = API_KEY

app = Flask(__name__)

#Hima
job=''
company=''
background=''

@app.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        job = request.form.get('job')
        company = request.form.get('company')
        occupation = request.form.get('occupation')
        city = request.form.get('city')
        state =  request.form.get('state')
        currentstudy = request.form.get('currentstudy')
        courseofstudy = request.form.get('courseofstudy')
        university = request.form.get('university')
        yearsofexperience = request.form.get('yearsofexperience')
        skillset = request.form.get('skillset')
        experience = request.form.get('experience')
        interests = request.form.get('interests')
        signature = request.form.get('signature')
       
        prompt = f"Write a professional cover letter of 150 words for {job} role at {company} company considering the job description the company provided for the {job} role. Here is My information - My occupation is {occupation} and I live in {city}, {state} .I'm currently pursuing my {currentstudy} in the course {courseofstudy} at{university}. I have {yearsofexperience} years of experience and my skillset is {skillset}. I worked as a {experience}. My further inerests are {interests} My signature/Name = {signature} . Generate a professional cover letter of 300 words which includes all the information I provided ."
        response = openai.Completion.create(
            model = 'text-curie-001',
            prompt = prompt,
            max_tokens = 1000,
            temperature=0.99,
            frequency_penalty=0.3,
            n=1,
        )
        
        text = format_text(response['choices'][0]['text'])
        
        
        return render_template("coverletter.html", text = text)
    return render_template("index.html")

def format_text(text):
    # Remove leading and trailing whitespace
    text = text.strip()

    # Split the text into paragraphs
    paragraphs = text.split('\n\n')

    # Format each paragraph
    formatted_paragraphs = []
    for paragraph in paragraphs:
        # Wrap the paragraph text to a line width of 80 characters
        wrapped_lines = textwrap.wrap(paragraph, width=80)

        # Add a blank line between each wrapped line
        formatted_paragraph = '\n'.join(wrapped_lines)

        # Add the formatted paragraph to the list
        formatted_paragraphs.append(formatted_paragraph)

    # Join the formatted paragraphs with double line breaks
    formatted_text = '\n\n'.join(formatted_paragraphs)

    return formatted_text

@app.route("/gotohome")
def gotohome():
    return redirect(url_for("home"))

if __name__ == '__main__':
    print("running py app")
    app.run(debug=True)