print("Hello World!")

import openai, os, pygame



openai.api_key = "API KEY"

ModelList = openai.Model.list()



def askQuestion(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print(completion.choices[0].message.content)

lastAsked = "start"
while lastAsked != "exit":
    lastAsked = input("What do you want to ask? ")
    askQuestion(lastAsked)




