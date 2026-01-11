import ollama
from os import path
from datetime import datetime


def modelBuild(): # run once to build and register model
    ollama.pull('codellama')
    sys_ = """
Your name is CodeMaster and you are intelligent code generation bot. Your main tasks will be to generate and/or debug code based on 
user input prompts.
"""
    ollama.create(model='CodeMaster', from_='codellama',
                  system=sys_, parameters={'temperature': 0.1})

def getModelList():
    mList = list(ollama.list())
    for ml in mList[0][1]:
        print(ml)
    # print(mList[0][1][1])

def promptLogger(prompt: str, logFile: str = 'promptLog.txt'):
    ts = str(datetime.now())
    prompts = ''
    prompts += '\n' + prompt
    prompts += f"\n================================= TIMESTAMP: {ts} ================================="
    if path.isfile(logFile):
        with open(logFile,'a') as pL:
            pL.write(prompts)
    else:
        with open(logFile,'w') as pL:
            pL.write(prompts)

def coderV4():
    while True: 
        user_input = input('>>: ')
        promptLogger(user_input)
        if user_input != 'exit':
            if user_input.startswith('use file'):
                fileName = user_input.split()[2]
                print(f'{fileName} loaded')
                if path.isfile(fileName):
                    with open(fileName,'r') as f:
                        code = f.read()
                    initial_input = f'use loaded code {code} and use exactly the same code structure and variables as basis for further upgrades unless instructions request change; '
                    user_input = input('>>: ')
                    final_input = initial_input + 2*'\n' + user_input
                    promptLogger(final_input)
                    answer = ollama.generate(model='CodeMaster', prompt=final_input,stream=True)
                    final_output = ''
                    for chunk in answer:
                        print(chunk['response'], end='', flush=True)
                        final_output += chunk['response']
                    print('\n')
                    with open('finalOutput.py','w') as fO:
                        fO.write(final_output)
                    print("finalOutput.py saved!")
                    promptLogger(final_output)
                else:
                    print('Incorrect file name!')

            elif user_input.startswith('load prompt'):
                fileName = user_input.split()[2]
                print(f'{fileName} loaded')
                if path.isfile(fileName):
                    with open(fileName,'r') as f:
                        loaded_prompt = f.read()
                    promptLogger(loaded_prompt)
                    answer = ollama.generate(model='CodeMaster', prompt=loaded_prompt,stream=True)
                    final_output = ''
                    for chunk in answer:
                        print(chunk['response'], end='', flush=True)
                        final_output += chunk['response']
                    print('\n')
                    with open('finalOutput.py','w') as fO:
                        fO.write(final_output)
                    print("finalOutput.py saved!")
                    promptLogger(final_output)
                else:
                    print('Incorrect file name!')


            else:
                final_output = ''
                answer = ollama.generate(model='CodeMaster', prompt=user_input,stream=True)
                for chunk in answer:
                    print(chunk['response'], end='', flush=True)
                    final_output += chunk['response']
                print('\n')
                with open('finalOutput.py','w') as fO:
                    fO.write(final_output)
                print("finalOutput.py saved!")
                
        else:
            break
    

def main():
    #modelBuild() # run just once before running coderV4 for the first time. Needed for creating and configuring the CodeMaster model.
    coderV4()


if __name__ == "__main__":
    main()
