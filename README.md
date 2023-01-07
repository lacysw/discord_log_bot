# discord_log_bot
Discord bot that logs notable user actions into a channel. Supports several customization options. Work in progress.

## Functionality
When added to a Discord server, this bot writes logs into a channel upon detecting the following actions:

 - A role is added to the server; the log message includes the following:
     - The description of the action
     - The added role name
     - The added role ID
     - The new total member count
     - The timestamp associated with the action
 - User joins the server; the log message includes the following:
     - The description of the action
     - The user ID
     - The new total member count
     - The timestamp associated with the action
 - User leaves the server; the log message includes the following:
     - The description of the action
     - The user ID
     - The new total member count
     - The timestamp associated with the action
 - User is kicked from the server; the log message includes the following:
     - The description of the action
     - The user ID
     - The timestamp associated with the action
 - User is banned from the server; the log message includes the following:
     - The description of the action
     - The user ID
     - The timestamp associated with the action
 - User is unbanned the server; the log message includes the following:
     - The description of the action
     - The user ID
     - The timestamp associated with the action
 - User edits a message; the log message includes the following:
     - The description of the action
     - The user ID
     - The previous message text
     - The new, edited text
     - The link to associated message
     - The timestamp associated with the action
 - User deletes a message; the log message includes the following:
     - The description of the action
     - The user ID
     - The deleted text
     - The timestamp associated with the action
 - User adds a reaction; the log message includes the following:
     - The description of the action
     - The user ID
     - The added reaction
     - The link to associated message
     - The timestamp associated with the action
 - User removes a reaction; the log message includes the following:
     - The description of the action
     - The user ID
     - The removed reaction
     - The link to associated message
     - The timestamp associated with the action
 - User gains a role; the log message includes the following:
     - The description of the action
     - The user ID
     - The added role
     - The timestamp associated with the action
 - User loses a role; the log message includes the following:
     - The description of the action
     - The user ID
     - The removed role
     - The timestamp associated with the action
 - User creates a thread; the log message includes the following:
     - The description of the action
     - The user ID
     - The title of the thread
     - The link to the thread
     - The timestamp associated with the action
 - User deletes a thread; the log message includes the following:
     - The description of the action
     - The user ID
     - The title of the thread
     - The timestamp associated with the action
 - User joins a voice channel; the log message includes the following:
     - The description of the action
     - The user ID
     - The name of the voice channel
     - The ID of the voice channel
     - The timestamp associated with the action
 - User leaves a voice channel; the log message includes the following:
     - The description of the action
     - The user ID
     - The name of the voice channel
     - The ID of the voice channel
     - The timestamp associated with the action
 - User is server muted in a voice channel; the log message includes the following:
     - The description of the action
     - The user ID
     - The name of the voice channel
     - The ID of the voice channel
     - The timestamp associated with the action
 - User is server deafened in a voice channel; the log message includes the following:
     - The description of the action
     - The user ID
     - The name of the voice channel
     - The ID of the voice channel
     - The timestamp associated with the action
 - User pings a user/role; the log message includes the following:
     - The description of the action
     - The user ID
     - The user(s)/role(s) pinged
     - The timestamp associated with the action
 - User sends a string; the log message includes the following:
     - The description of the action
     - The user ID
     - The string detected in the user's message
     - The text of the user's message
     - The timestamp associated with the action
 - User's nickname is changed; the log message includes the following:
     - The description of the action
     - The user ID
     - The user's previous nickname
     - The user's new nickname
     - The timestamp associated with the action

## Configuration
Bot configuration can be managed within `config.yaml`. See `config_example.yaml` for an example configuration file. Note that `config.yaml` must exist for the bot to run.

## Usage
1. install Python 3 (version 3.10+) and Pip 3
2. Install the required libraries with `pip3 install -r requirements.txt` in the root directory of the bot
3. See `/config_example.yaml` for an example configuration file and populate `config.yaml` with the options of your choosing (note that the API token is a required field)
4. Add the bot to your server
5. Invoke the bot with `python3 discord_log_bot.py`
