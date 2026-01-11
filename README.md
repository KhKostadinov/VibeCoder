**Overview**
Building more complex vibe coding engine with LangChain requires more resources and runs impressively slowly on my computer. 
That is why I decided to build it the simplest possible way - with the simplest possible LLM interaction method Ollama offers and without any vector DB memory embeddings.
Tested for relatively simple code generation and it works well, not sure what will be the result for more complex tasks.

**How to use**
You need Ollama installed on your system.
First run the **modelBuild()** function that creates the model and gives it minimalistic context (it may take a while because the codellama model needs to be downloaded first). 
Afterwards stop **modelBuild()** and execute **coderV4()** function only (easily done in **main()** function). You can run it with either **"uv run main.py"** in the terminal 
or just by double-clicking the **main.py** file.

**Workflow**
The CLI collects user input and interacts with the LLM to produce code. This code can be reloaded and forwarded as LLM input => we can request the LLM to improve/upgrade/change
the existing code. Every input/output is stored in a prompt log file. Recognizable commands:
 - use file [filename] - utilize this command if you want to load file with code only;
 - load prompt [filename] - use this command to load large prompts saved in external file;
Anything different than the 2 commands above will be treated as regular prompt for the AI.

**Code review**
Used modules:
 - **ollama** - provides the LLM needed for code generation;
 - **os** - specifically **path** module, needed to check if the file provided by the commands exist and avoid eventual program crashing due to wrong file naming.
 - **datetime** - used to create timestamps for logging needs.

Used functions:
 - **modelBuild()** - as mentioned above this function pulls codellama (you can specify different model based on your preferences) and creates our local CodeMaster model.
    Some basic model context is defined here, you can extend it if you need more specific or exact instructions. I've set the temperature parameter to 0.1 to be less "passionate"
    when answering.
   
 - **getModelList()** - prints a list of the LLMs you have available.
 - **promptLogger()** - this function creates/extends log file of the prompts and the outputs you use. Each log is separated by timestamp. It uses 2 arguments:
    - prompt: str - stores prompt/output in string format which asfterwards added to the log file.
    - logFile: str - stores the name of the log file, by default it is 'promptLog.txt' but can be changed.
 - **main()** - this is the main ("surprise") function where the magic happens - user input is collected, commands are recognized, interaction with LLM is handled, logs are
   being written and in the end we (are supposed to) have functional Python code (this isn't strictly restricted to Python code, however, and it is easily adjustable to generate
   code for other languages). 
