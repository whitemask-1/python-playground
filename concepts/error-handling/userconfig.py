#freeCodeCamp user configuration settings project
# Script using functions to add, update, delete, and view user settings stored in a dictionary
# Each setting is a key-value pair where both key and value are strings
# Project enforces understanding of function definitions, dictionary manipulations, and string operations
test_settings = {}
def add_setting(settings, setting_tuple) : 
    key = setting_tuple[0].lower()
    value = setting_tuple[1].lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    if key not in settings.keys():
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting_tuple) :
    key = setting_tuple[0].lower()
    value = setting_tuple[1].lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
        
    
def delete_setting(settings, setting_key):
    setting_key = setting_key.lower()
    if setting_key in settings:
        del settings[setting_key]
        return f"Setting '{setting_key}' deleted successfully!"
    else:
        return 'Setting not found!'

def view_settings(settings):
    if not settings:
        return 'No settings available.'
    if settings:
        formatted_settings = ''
        for key, value in settings.items():
            format_setting = key.capitalize() + ": " + value + '\n'
            formatted_settings += format_setting
        
        return 'Current User Settings:\n' + formatted_settings 

add_setting(test_settings, ('theme', 'dark'))
print(view_settings(test_settings))
update_setting(test_settings, ('theme', 'light'))
print(repr(view_settings(test_settings))) #Using repr to show newline characters and debug formatting