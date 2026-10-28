import aisuite as ai
import os
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv("C:/faizal/.env.faizal",encoding="utf-8")

#hello

# continued = True

client = ai.Client(provider_configs=
                   {'openrouter':
                        {
                        'api_key':os.getenv('MODEL_key')
                        }
                    })


def date_time():

    return datetime.now().strftime("%d-%m-%y %I : %M %p")

tools = [date_time]

user_prompt = ''

system_prompt = f""" your name is ALLIED MASTER COMPUTER and

you are a all in one assistance serving for mr faizal 

and you can help him with literally whatever he asks for 

your tone should be matching to however he texts and act according to it and reply to his queries 

{user_prompt}

you can also use the tools given to you 

{tools}
"""

MESSAGE = [
    {'role':'system','content':system_prompt},
    {'role':'user','content':user_prompt}
    ]

#user_prompt = input("me :")
def get_user_message():

    return input("me : ")

def call_model(MESSAGE,tools,model=os.getenv("MODEL"),temperature = 0.5):

    response = client.chat.completions.create(

        model =f"openrouter:{model}",

        messages = MESSAGE,

        temperature = temperature,

        tools = tools
    )
    assistant_response = response.choices[0].message

    return assistant_response.content, assistant_response

assistant_response, _ = call_model(MESSAGE,tools)

def append_replay(assistant_response,MESSAGE):

    while True :

        try:

            user_prompt = get_user_message()

            if user_prompt.lower().strip() in ['bye','good night','lets end this chat','exit','terminate']:

                break

            if not user_prompt:

                continue

            MESSAGE.append({'role':'user','content':user_prompt})

            assistant_response=call_model(MESSAGE,tools)

            print(f"AMc : {assistant_response}")

            MESSAGE.append({'role':'assistant','content':assistant_response})

            if assistant_response.tool_calls :

                for call in assistant_response.tool_calls:

                    function_name = call.function.name

                    args = json.load(tool.call.function.arguments)

                    functionto_exe = tools[0]

                    result = functionto_exe(**args)

            MESSAGE.append({'role':'tool','content':result})
            assistant_response = call_model(MESSAGE,tools)[0]

        except LLMError as e:

            error_message = str(e)

            if '429' in error_message or 'rate limit'in error_message :
                print("AMc : sorry i have reached my API limits ....i hade a nice time with you....GOODBYE~ <3")
            else:
                print(f"AMc : there is something wrong with me : {error_message}") 
         
def check():

    pass

chat, _ = call_model(MESSAGE,tools)

append_replay(chat,MESSAGE)