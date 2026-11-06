# this is a personal project of mine
# as im currently learning LLMs and AGENTIC WORKFLOW
# i have a lot to learn and my philosophy 
# is that it nothing beats learning while building 
# so 
# i build it with what all i know and ofc im working to improve it everyday by 1% by learning new new concepts and the code 
# in the comment lines ?.......nah im not gonna erase it 
# as it shows how i approached the problem and how i came up with a optimised solution by learning new things its like a lookback history

import aisuite as ai
import os
import re 
from dotenv import load_dotenv
from datetime import datetime
import subprocess

load_dotenv(encoding="utf-8")
 
client = ai.Client(provider_configs=
                   {'openrouter':
                        {
                        'api_key':os.getenv('MODEL_key')
                        }
                    })


def date_time():

    return datetime.now().strftime("%d-%m-%y %I : %M %p")

tools= [date_time]


system_prompt = os.getenv("system_prompt")

MESSAGE = [
    {'role':'system','content':system_prompt},
    ] #0

def model() -> str:#model

    response=client.chat.completions.create(

        model = f"openrouter:{os.getenv('model')}",

        messages = MESSAGE,

        temperature = 0.7,

        tools = tools,

        max_turns = 5
    )
    return response

def trim_messages(MAX,MESSAGE):

    MESSAGE = [MESSAGE[0]] + MESSAGE[1:][-MAX:]

    return MESSAGE

    # print(type(response))

    # print(repr(respose))
        

def extract_python(text):

    code = re.search(r"<execute_python_code>(.*?)</execute_python_code>",text,re.DOTALL)

    return code.group(1).strip() if code else None

def execute_python(code):

    # with tempfile.TemporaryDirectory(prefix="amc_") as tempfile:

    #     code_path = os.path.join(temp_file,"code.py")

    #     with open(code_path,"w") as f:

    #         f.write(code)

    command = ['docker','run','--rm','--network','none','--memory',
                   '128m','--cpus','0.5','--pids-limit','32','--read-only',
                   '--tmpfs','/tmp:rw,noexec,nosuid,size=16m',
                   '--cap-drop','ALL','--security-opt','no-new-privileges',
                   '--user','10001:10001','amc-sandbox']
    if code != None:

        try:
        
            result = subprocess.run(command,input=code,capture_output=True,text=True,timeout=10)

            return {
                "stdout":result.stdout} 
        
        except subprocess.TimeoutExpired:

            return {"stdout": ""}
                
        
        except FileNotFoundError :

            return {
                "stdout":""}
        
        except Exception as e:

            return {
                "stdout":"",
                }
    else:
        return {
                "stdout":"",
                }    
    # with tempfile.TemporaryDirectory(prefix='amc_') as temp_file :

    #     code_path = os.path.join(temp_file,"code.py")

    #     with open(code_path,"w") as f:

    #         f.write(code)

    # result = subprocess.run(["docker","run","-rm","--network=none",])


    # original_stdout=sys.stdout

    # output=io.StringIO()

    # exec_global = {"__builtin__":__builtins__}

    # exec_local = {}

    # try:

    #      sys.stdout=output

    #      exec(code,exec_global,exec_local)

    # except Exception as e:

    #      return f"error : {str(e)}"
    
    # finally:
            
    #      sys.stdout = original_stdout

    # result = output.getvalue()

    # return result


while True:

    user_prompt=input("faizal (user) :")

    print("\n")

    if user_prompt.lower().strip() in ["bye",'goodnight','exit',"enough","bored","seeyah"]:

        break
    if not user_prompt:

        continue

    MESSAGE.append({'role':'user','content':user_prompt}) #1

    response = model()

    text = response.choices[0].message.content or " "

    # MESSAGE.append({'role':'assistant','content':response}) #2

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
        #print(f"AMc : {result}\n")
        MESSAGE.append({
                     "role": "user",
                     "content": f"""
                     INTERNAL EXECUTION RESULT for the current query:
                                     {code_result}

                     Use this result to answer the most recent original
                     user request. Do not answer earlier requests again.
                     make it short as possible
                     and doesnt need to explain just format it nicely
                     """
                    })#2
        result = model()
        print(f"AMc : {result}")
        print('\n')
        trim_messages(2)
    
