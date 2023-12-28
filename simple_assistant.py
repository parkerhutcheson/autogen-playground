from autogen import config_list_from_json
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen import UserProxyAgent

config_list = config_list_from_json("OAI_CONFIG_LIST.json")

# creates new assistant using Assistant API
gpt_assistant = GPTAssistantAgent(
    name="Friendaiya",
    llm_config={
        "config_list": config_list,
        "assistant_id": "asst_JFyCUQbI0GdkQXnfagxunLi1"
    })


user_proxy = UserProxyAgent(name="user_proxy",
    code_execution_config={
        "work_dir": "coding"
    },
    human_input_mode="ALWAYS")

user_proxy.initiate_chat(gpt_assistant, message="Hey how are you??")