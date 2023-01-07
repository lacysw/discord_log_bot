import discord
import yaml
import csv
from datetime import datetime

# Load configuration file
with open("config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)


# Initialize Discord client
client = discord.Client(intents=discord.Intents.default())

# Fetch log channel
log_channel = client.get_channel(config["log_channel"])

# Open CSV file for local logging (if enabled)
if config["log_local"]:
    csv_file = open("log.csv", "w", newline="")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["timestamp", "event", "details"])

@client.event
async def on_ready():
    print("Log bot is ready!")

@client.event
async def on_guild_channel_create(channel):
    if config["log_server_channel_change"]:
        log_message = f"A new channel was created: {channel.name} ({channel.id})"
        await log_channel.send(log_message)
        if config["log_local"]:
            csv_writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "channel create", log_message])

@client.event
async def on_guild_channel_delete(channel):
    if config["log_server_channel_change"]:
        log_message = f"A channel was deleted: {channel.name} ({channel.id})"
        await log_channel.send(log_message)
        if config["log_local"]:
            csv_writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "channel delete", log_message])

@client.event
async def on_guild_role_create(role):
    if config["log_server_role_change"]:
        log_message = f"A new role was created: {role.name} ({role.id})"
        await log_channel.send(log_message)
        if config["log_local"]:
            csv_writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "role create", log_message])

