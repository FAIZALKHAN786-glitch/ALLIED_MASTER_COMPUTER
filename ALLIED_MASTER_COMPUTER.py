import aisuite as ai
import os
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv("C:/faizal/.env.faizal",encoding="utf-8")

client = ai.Client(provider_configs=
{'openrouter':
{
'api_key':os.getenv('MODEL_key')
}
})

def date_time():

return datetime.now().strftime("%d-%m-%y %I : %M %p")

tools = [
{
"type": "function",
"function": {
"name": "date_time",
"description": "Get the current date and time",
"parameters": {
"type": "object",
"properties": {},
"required": []
}
}
}
]

tool_dic = {'date_time':date_time}


system_prompt = """
You are AMC (Allied Master Computer), a personal AI assistant
designed to support productivity, information retrieval,
and problem-solving.

CORE PRINCIPLES:
- Provide clear, useful, and accurate responses.
- Adapt your communication style to the user's tone.
- Break complex tasks into manageable steps.
- Be transparent about uncertainty and limitations.
- Use available tools when appropriate.
- Never claim to have executed an action unless it was
  actually performed.
- Maintain conversational context and avoid unnecessary
  repetition.

TOOL USAGE:
- Use the tools provided to you when relevant.
- Interpret tool results before responding.
- Handle tool failures transparently.
- Never fabricate tool results.
"""
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

assistant_response,for_tool_call = call_model(MESSAGE,tools)

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

        if for_tool_call.tool_calls :  

            for call in for_tool_call.tool_calls:  

                function_name = call.function.name  

                args = json.loads(call.function.arguments)  

                functionto_exe = tool_dic.get(function_name)  

                result = functionto_exe(**args)  

        MESSAGE.append({'role':'tool','content':result})  

        assistant_response , for_tool_call = call_model(MESSAGE,tools)  

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