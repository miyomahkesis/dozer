import discord
import commands
import data.albums as music
from misc import out


async def message(message):
# SECTION M1 //////////////////////////////////////////////////////////////////////
    # To enter multiple things into a command, we first need
    # to break the message down into multiple strings in a
    # list for the bot to understand the full sentence, also
    # for convienence sake.
    message_received = message.content.lower() # Lower the sentence in case a user capitalizes a word.
    message_received = message_received.split() # Then split the words into a list.
    COMMAND_NAMES = ['.hello', '.uinfo', '.sinfo', '.alte', '.rs', '.ra', '.soap']
    try:
        if message_received[0] in COMMAND_NAMES:
            command_index = -1
            for names in COMMAND_NAMES:
                command_index += 1
                if message_received[0] == names:
                    break
    # SECTION M2 //////////////////////////////////////////////////////////////////////
            # The ".alte" command, for example, uses multiple words in
            # the received message. So if there is only the command
            # in the message (list index equals 0) then we need to set
            # the variables to blanks.
            artist, album = '', []
            try: # If there more than just the command line.
                if str(message_received[1]).capitalize() in music.artists:
                    artist = message_received[1] # set the artist var to the second word.
                    album = message_received[2:len(message_received)] # set album to the rest of the list length.
            except: # If it is just the command line,
                pass # pass and leave it blank.
    # SECTION M3 //////////////////////////////////////////////////////////////////////
            COMMAND_FUNCTIONS = [
                commands.hello(),
                commands.uinfo(message), commands.sinfo(message),
                commands.alte(artist, album), commands.rs(artist), commands.ra(artist),
                commands.soap()
            ]
            try:
                command = COMMAND_FUNCTIONS[command_index]
                if type(command) == discord.embeds.Embed:
                    await message.channel.send(embed=command)
                    out(f'"{message_received[0]}" Embed was returned for {message.author.name}#{message.author.discriminator} in {message.guild.name}', 'r')
                elif type(command) == str:
                    await message.channel.send(command)
                    out(f'"{message_received[0]}" Message was returned for {message.author.name}#{message.author.discriminator} in {message.guild.name}', 'r')
            except IndexError: out(f'(SECTION M3) Index out of range w/ "command" in "messages.py". {len(message_received)} <- Ignore if "0"', 'e')
            except NameError as NE: out(f'(SECTION M3) Incorrect name in "messages.py". Change to "command". {NE}', 'e')
            except KeyError: pass
            except: out(f'(SECTION M3) Something went wrong.\n  vars below:\n\tcommand = {command}\n\tMessageRecieved = {message_received}', 'e')
    except: pass

#out(f'(SECTION M3) command_index = {command_index}, command = {command} -> type({type(command)})', 'r')