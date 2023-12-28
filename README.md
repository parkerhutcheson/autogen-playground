# Autogen Playground
This repository contains multiple test scripts to interact with various functions of Autogen, as well as custom assistants and different GPT models from providers like Llama 2 and OpenAi.

## Setting Up your Environment

1. Enter your OpenAi API Key and any other neccesary keys in `OAI_CONFIG_LIST.json`.

2. Install Python using Homebrew

```
brew install python
```

3. Setup a virtual env in Python named "myenv" (or whatever you want to call it) to avoid making changes to your global version
```
python3 -m venv myenv
```

4. Run the following command to initialize the virtual env
```
source myenv/bin/activate
```

5. You are now in the virtual environment and should see your terminal starts with (myenv). 

    Next we will install dependencies listed in `requirements.txt` (including Autogen). Run the following command to instal dependencies
```
pip install -r requirements.txt
```

6. You can now run any of the Python scripts that are available. For example, you can run the `simple_assistant.py` script like so:
```
python3 simple_assistant.py
```