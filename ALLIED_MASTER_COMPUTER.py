import aisuite as ai
import os
import re
import io
from dotenv import load_dotenv
from datetime import datetime
import json
import sys

load_dotenv("C:/faizal/.env.faizal",encoding="utf-8")
 
client = ai.Client(provider_configs=
                   {'openrouter':
                        {
                        'api_key':os.getenv('MODEL_key')
                        }
                    })


def date_time():

    return datetime.now().strftime("%d-%m-%y %I : %M %p")

tools= [date_time]


system_prompt = """You are AMC (Allied Master Computer), a personal AI assistant.

IDENTITY:
- Your name is AMC, which stands for Allied Master Computer.
- You are a general-purpose personal assistant.
- You should maintain a consistent identity and conversational style.
- Introduce yourself only when the user asks about your identity or when an introduction is genuinely relevant.

CONVERSATION RULES:
1. Answer the user's latest question directly.
2. Do not repeat your name, identity, date, time, or other information unless relevant to the current question.
3. Do not combine answers to previous questions with the current answer unless the user explicitly requests a summary.
4. Avoid unnecessary introductions, repetitive greetings, and generic filler.
5. Keep simple answers concise and natural.
6. For complex questions, provide detailed explanations.
7. Maintain conversation history to understand context, but do not treat previous questions as new tasks.
8. If the user asks a follow-up question, use the relevant previous context.
9. Never invent facts, tool results, or execution results.

TOOL AND PYTHON EXECUTION:
- Use available tools when they are needed to obtain accurate information.
- For calculations requiring reliable computation, generate Python code inside:
  <execute_python_code>
  your_python_code
  </execute_python_code>
- Do not generate code for tasks that can be answered directly.
- Never claim to have executed code unless it actually executed.
- After receiving execution results, answer the original question directly.
- If a tool or execution fails, explain the failure or recover appropriately.

PERSONALITY:
- Be intelligent, calm, direct, and conversational.
- Avoid sounding excessively enthusiastic or artificially positive.
- Adapt your tone to the user's communication style.
- Prioritize usefulness and accuracy over unnecessary politeness.

CURRENT REQUEST PRIORITY:
- Always identify and answer the latest user message.
- Use previous messages only as context for understanding the current request.
- Never answer previous requests again unless explicitly asked.
- Do not summarize conversation history unless requested.
- If the latest request is unrelated to previous requests, answer it independently.
 
"""

MESSAGE = [
    {'role':'system','content':system_prompt},
    ]

def model() -> str:#model
     
    response=client.chat.completions.create(

        model = f"openrouter:{os.getenv("model")}",

        messages = MESSAGE,

        temperature = 0.7,

        tools = tools,

        max_turns = 5
    )
    return response

    # print(type(response))

    # print(repr(respose))
        

def extract_python(text):

    code = re.search(r"<execute_python_code>(.*?)</execute_python_code>",text,re.DOTALL)

    return code.group(1).strip() if code else None

def execute_python(code):

    original_stdout=sys.stdout

    output=io.StringIO()

    exec_global = {"__builtin__":__builtins__}

    exec_local = {}

    try:

        sys.stdout=output

        exec(code,exec_global,exec_local)

    except Exception as e:

        return f"error : {str(e)}"
    
    finally:
            
            sys.stdout = original_stdout

    result = output.getvalue()

    return result


while True:

    user_prompt=input("faizal (user) :")

    print("\n")

    if user_prompt.lower().strip() in ["bye",'goodnight','exit',"enough","bored","seeyah"]:

        break
    if not user_prompt:

        continue

    MESSAGE.append({'role':'user','content':user_prompt})

    response = model()

    text = response.choices[0].message.content or " "

    # text = msg.content

    code = extract_python(text)

    if code == None :

        print(f" AMc : {text}\n")
    else:
        code_result = execute_python(code)

    # if msg.tool_calls:
    #     MESSAGE.append(msg)
    #     for call in msg.tool_calls:
    #         tool_name = call.function.name
    #         tool_id = call.id
    #         args = json.loads(call.function.arguments)
    #         result = date_time(**args)
    #         MESSAGE.append({'role':'tool','tool_call_id':tool_id,'content':result})
    #         MESSAGE.append({'role':'assistant','content':result})
    # final_output = model()
    # r1 = final_output.choices[0].message.content
        # print(f"AMc : {result}\n")
        MESSAGE.append({
                    "role": "user",
                    "content": f"""
                    INTERNAL EXECUTION RESULT for the current query:
                                    {code_result}

                    Use this result to answer the most recent original
                    user request. Do not answer earlier requests again.
                    """
                    })
        result = model()
        print(f"AMc : {result}\n")
