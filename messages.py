import discord
import commands
import data.albums as music
from misc import out


async def message(message):
    # To enter multiple things into a command, I first need
    # to break the message down into multiple strings in a
    # list for the bot to understand the full sentence, also
    # for convienence sake. I don't know any other way of doing this.
    message_received = message.content.lower() # Lower the sentence in case a user capitalizes a word.
    message_received = message_received.split() # Then split the words into a list.
    COMMAND_NAMES = ['.hello', '.uinfo', '.sinfo', '.alte', '.rs', '.ra', '.soap', '.shank'] # \\ Commands will need to be added to this as well as 'COMMAND_FUNCTIONS.'
    try: # This is just because 'COMMAND_FUNCTIONS' will run through all the functions and errors will rise in commands that aren't being used.
        if message_received[0] in COMMAND_NAMES:
            command_index = -1 # Command index tells me where the command is in both 'COMMAND_NAMES' and 'COMMAND_FUNCTIONS'
            for names in COMMAND_NAMES: # Needs to check through each
                command_index += 1 # Add one to the command index
                if message_received[0] == names:
                    break
            # The ".alte" command, for example, uses multiple words in
            # the received message. So if there is only the command
            # in the message (list index equals 0) then I need to set
            # the variables to blanks.
            artist, album = '', []
            try: # If there more than just the command line.
                if str(message_received[1]).capitalize() in music.artists:
                    artist = message_received[1] # set the artist var to the second word.
                    album = message_received[2:len(message_received)] # set album to the rest of the list length.
            except: # If it is just the command line,
                pass # pass and leave it blank.
            COMMAND_FUNCTIONS = [
                commands.hello(),
                commands.Info.uinfo(message), commands.Info.sinfo(message),
                commands.alte(artist, album),
                commands.Random.rs(artist), commands.Random.ra(artist),
                commands.soap(),
                commands.shank(message)
            ]
            try: # Sometimes
                command = COMMAND_FUNCTIONS[command_index] # This will run the command chosen.
                # Since the functions return either an embed or a message,
                # I need to identify which one it is and send it as an embed
                # or as a message.
                if type(command) == discord.embeds.Embed:
                    await message.channel.send(embed=command)
                    out(f'"{message_received[0]}" Embed was returned for {message.author.name}#{message.author.discriminator} in {message.guild.name}', 'r') # This might get annoying
                elif type(command) == str: # Message
                    await message.channel.send(command)
                    out(f'"{message_received[0]}" Message was returned for {message.author.name}#{message.author.discriminator} in {message.guild.name}', 'r') # This also might get annoying
            except IndexError: out(f'(SECTION M3) Index out of range w/ "command" in "messages.py". {len(message_received)} <- Ignore if "0"', 'e')
            except KeyError: pass # I forgot why this is a pass, but I most likely have a good reason for it.
            except Exception as e: out(f'(SECTION M3) Something went wrong. {e}.\n  vars below:\n\tcommand = {command}\n\tMessageRecieved = {message_received}', 'e')
        elif message_received[0] == '.commands':
            commands_list_str = ''
            for i in COMMAND_NAMES:
                commands_list_str += f'  {i}\n'
            await message.channel.send(f'Command List:\n{commands_list_str}')
    except Exception as E: out(f'{E}', 'e')