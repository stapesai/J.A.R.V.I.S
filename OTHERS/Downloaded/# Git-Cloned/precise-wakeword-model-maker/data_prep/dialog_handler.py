import json

class DialogHandler:
    def __init__(self, dialog_file, dialog_name):
        with open(dialog_file) as json_file:
            dialog_data = json.load(json_file)
        self.dialog_data = dialog_data

        for dialogs in self.dialog_data:
            if dialogs["dialog_name"] == dialog_name:
                self.dialogs = dialogs
#TODO: refactor for dialog_name as a parameter

    def get_text_for_matching_intent(self, cli_intent):
        for dialog_content in self.dialogs["dialog_content"]:
            if dialog_content["dialog_type"] == cli_intent:
                if 'input-' in dialog_content["dialog_type"]:
                    return input(dialog_content["text"])
                elif 'inform-' in dialog_content["dialog_type"]:
                    return dialog_content["text"]
                else:
                    return print(f'No matching intent found for {cli_intent}')

    def get_dialog_template_text(self, cli_intent):
        for dialog_content in self.dialogs["dialog_content"]:
            if dialog_content["dialog_type"] == cli_intent:
                return dialog_content["text"]

    def render_template(self, cli_intent, **args):
        dialog_template_text = self.get_dialog_template_text(cli_intent)
        return dialog_template_text.format(**args)

'''
    def get_slot_filled_text(self, cli_intent):
        def fstr(template):
            return eval(f"f'{template}'")
        for dialog_content in self.dialogs["dialog_content"]:
            if dialog_content["dialog_type"] == cli_intent:
                if 'inform-' in dialog_content["dialog_type"]:
                    return fstr(dialog_content["text"])
'''




    # TODO: pass f string to print with dialog class
    # TODO: think out response_types: numbered (ie choices 1,2, 3, etc.), string inputs, etc.
    # TODO: make sub classes for each flow of dialog with their dialog_content and dialog_response
    # TODO: create json files for each dialog flow and load them in the DialogHandler
    # TODO: refactor other code to implement DialogHandler

"""
dialog_name = 'base_model_menu_dialog'

dialog_handler_instance = DialogHandler("dialog.json", dialog_name)

print(dialog_handler_instance.get_text_for_matching_intent("inform-splitting_data"))

cli_intent = 'inform-splitting_data'
source_directory = 'test/'


print(dialog_handler_instance.get_slot_filled_text(cli_intent))
"""#dialog_contents = dialog_handler_instance.get_dialog_contents()

#print(dialog_contents)

# prints the keys of the dictionaries in the list
#print([item for sublist in dialog_handler_instance.dialog_data for item in sublist])

# prints a list in a list of the dialog_content dictionaries
#print([dialog['dialog_content'] for dialog in dialog_handler_instance.dialog_data])

# TODO: this works, but it's not the best way to do it

# test
'''
cli_intents = ['input-string-wakeword_recordings_directory', 'input-numbered-main_choice' , 'inform-training_complete']
for cli_intent in cli_intents:
    output = dialog_handler_instance.get_text_for_matching_intent(cli_intent)
    print(output)
'''
# create summary of code
# 1. when script starts, print directory and wake word from json config
# 2. prompt user for input from main_menu_dialog (choice 1, 2, 3, etc.)
# 3. if user input is 1, prompt user for input from menu_dialog_1
# 4. if user input is 2, prompt user for input from menu_dialog_2
# 5. if user input is 3, prompt user for input from menu_dialog_3
# What to do if there is just information, is it part of this? Where do print statements go?
# What about slots?

# How does it work?
# 1. get dialog_types from json file
# 2. function to pass dialog_type to get_dialog_content
# 3. get text from json file
# 4. function to pass text to print