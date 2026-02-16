from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import AgentTemplate

event_files = {
    "goblin": "lab04/lab04_goblin.json",
    "enemy": "lab04/lab04_enemy.json",
    "npc": "lab04/lab04_npc.json",
    "dm": "lab04/lab04_dm.json"
}

def run_event_chat(event_name, event_template_file_path, context, **event_kwargs):
    agent_chat = AgentTemplate.from_file(event_template_file_path, **event_kwargs)
    agent_chat.messages.append(context)

    first_event_response = agent_chat.start_chat()
    print(f'{event_name.capitalize()}: {first_event_response}')

    while True:
        try:
            event_response = agent_chat.send(input('You: '))
            print(f'{event_name}: {event_response}')

        except StopIteration as e:
            break

def run_dm_chat(**kwargs):
    dm_chat = AgentTemplate.from_file(event_files["dm"], **kwargs)
    dm_response = dm_chat.start_chat()
    print(f'{"Dungeon Master"}: {dm_response}\n')

    #check which event should be started
    agent_line = dm_response.split('\n')[0].lower()
    selected_event_name = None
    selected_event_template_file_path = None
    for event_name, file_path in event_files.items():
        if event_name in agent_line:
            selected_event_name = event_name
            selected_event_template_file_path = file_path
            break
    
    if not selected_event_name: return


    event_kwargs = {}
    if selected_event_name == "goblin":
        event_kwargs = {
            "user_gold": "30",
            "armor" : ''
        }

    dm_context = {"role": "user", "content" : f"Dungeon Master: {dm_response}"}
    #start the event
    run_event_chat(selected_event_name, selected_event_template_file_path, dm_context, **event_kwargs)




if __name__ ==  '__main__':
    # Add code here to start DM chat
    run_dm_chat(encounters = "goblin, enemy, npc")

    # But before here.
    pass