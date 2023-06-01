import discord
import misc


def hello():
    return 'Hello!'

def uinfo(message):
    if message.mentions == []: 
        user = message.author
    else:
        for mention in message.mentions:
            user = mention
    nickname_text = ''
    if user.nick == None: pass # if there is no a nickname attached to that account pass
    else: # but if there is set it to that var
        nickname_text = '"' + user.nick + '"'

    TIME_CREATED = misc.cst(user.created_at.strftime('%H'), user.created_at.strftime('%p'), user.created_at.strftime('%d'), user.created_at.strftime('%m'), user.created_at.strftime('%Y'))
    TIME_JOINED = misc.cst(user.joined_at.strftime('%H'), user.joined_at.strftime('%p'), user.joined_at.strftime('%d'), user.joined_at.strftime('%m'), user.joined_at.strftime('%Y'))
    EMBED = discord.Embed(title=f'{user.name}#{user.discriminator}', description=f'{nickname_text}')
    EMBED.add_field(name='Overview', value=f'ID: `{user.id}`')
    EMBED.add_field(name='Created/Joined', value=f'Created: {user.created_at.strftime(f"`{TIME_CREATED[3]} {TIME_CREATED[2]} {TIME_CREATED[1]} @ {TIME_CREATED[0]}:%M:%S CST`")}\nJoined: {user.joined_at.strftime(f"`{TIME_JOINED[3]} {TIME_JOINED[2]} {TIME_JOINED[1]} @ {TIME_JOINED[0]}:%M:%S CST`")}', inline=False)
    EMBED.set_thumbnail(url=user.avatar)
    return EMBED

def rs(artist):
    import data.albums
    from random import randint
    from misc import release_catagory, seconds_converter, rand_dict
    if artist == '':
        return 'You have to pick a band'
    else:
        artist = artist.capitalize()
    try:
        album = rand_dict(data.albums.artists[artist])
        album = data.albums.artists[artist][album][1]
        if type(album) == list:
            rand_disc = randint(0, len(data.albums.artists[artist][album][1]))
            rand_song = randint(0, len(data.albums.artists[artist][album][1][rand_disc]))
            song = data.albums.artists[artist][album][1][rand_disc][rand_song]
            length = data.albums.artists[artist][album][2][rand_disc][rand_song]
        else:
            rand_disc = 0
            rand_song = randint(0, len(data.albums.artists[artist][album][1]))
            song = data.albums.artists[artist][album][1][rand_song]
            length = data.albums.artists[artist][album][2][rand_song]            
    except KeyError:
        misc.out(f'{artist} not in artists data', 'e')
        return f'{artist} is not in the bots database.'
    try:
        EMBED = discord.Embed(title=f'"{song}" ({seconds_converter(length)})')
        EMBED.add_field(name='', value=f'From the {release_catagory(data.albums.artists[artist][album][2])} "{album}" - {artist}')
        EMBED.add_field(name=f'{rand_disc}', value=f'{rand_song}')
        return EMBED
    except TypeError: 
        misc.out('TypeError in ".rs" embed', 'e')
    except: pass

def ra(artist):
    import data.albums
    from misc import release_catagory, seconds_converter, set_list, rand_dict
    if artist == '':
        return 'You have to pick a band'
    else:
        artist = artist.capitalize()
    try:
        album = rand_dict(data.albums.artists[artist])
    except KeyError:
        misc.out(f'{artist} not in artists data', 'e')
        return f'{artist} is not in the bots database.'
    try:
        EMBED = discord.Embed(title=f'"{album}" - {artist}', description=f'{release_catagory(data.albums.artists[artist][album][2])} · {data.albums.artists[artist][album][0][0]}, {data.albums.artists[artist][album][0][1]}')
        EMBED.add_field(name='', value=set_list(data.albums.artists[artist][album][1], force=True)[1])
        EMBED.set_footer(text=f'{set_list(data.albums.artists[artist][album][1])[0]} songs, {seconds_converter(sum(data.albums.artists[artist][album][2]))}')
        return EMBED
    except TypeError: 
        misc.out('TypeError in ".ra" embed', 'e')
    except: pass

def sinfo(message):
    TIME_CREATED = misc.cst( message.guild.created_at.strftime('%H'), message.guild.created_at.strftime('%p'), message.guild.created_at.strftime('%d'), message.guild.created_at.strftime('%m'), message.guild.created_at.strftime('%Y'))
    embed = discord.Embed(title=f'{message.guild.name}', color=0x4287f5)
    embed.add_field(name='Overview', value=f'Owner: <@{message.guild.owner_id}>\nServer ID: `{message.guild.id}`\nMembers: `{message.guild.member_count}`', inline=True)
    embed.add_field(name='Counts', value=f'Text Channels: `{len([x for x in message.guild.channels if type(x) == discord.channel.TextChannel])}`\nVoice Channels: `{len([x for x in message.guild.channels if type(x) == discord.channel.VoiceChannel])}`\nRoles: `{len([x for x in message.guild.roles])}`', inline=True)
    embed.add_field(name='Created On', value=f'{message.guild.created_at.strftime(f"`{TIME_CREATED[3]} {TIME_CREATED[2]} {TIME_CREATED[1]} @ {TIME_CREATED[0]}:%M:%S CST`")}', inline=False)
    embed.set_thumbnail(url=message.guild.icon)
    return embed

def alte(artist='', album=[]):
    import data.albums
    from misc import release_catagory, seconds_converter, set_list, rand_dict
    # If album is not in list form the rest of the function
    # will break as it expects the variable to be a list.
    if type(album) != list: # If the album var is not a list
        misc.out('variable "album" is not a list, converting it to a list. This may cause problems.', 'w')
        album = list(album) # Make it into a list reguardless.
    for i in data.albums.artists:
        if artist.lower() in i.lower():
            artist = i
    try:
        album_list = [albums for albums in data.albums.artists[artist]]
    except KeyError: misc.out(f'{artist} not in artists data', 'e')
    except: pass
    album_name = ''
    if artist == 'Avatar':
        artist = rand_dict(data.albums.artists)
    else: pass
    if len(album) == 0:
        try:
            album = rand_dict(data.albums.artists[artist])
        except: pass
    else:
        number_test = 1
        for i in album:
            if len(album) == 1 or number_test == len(album):
                album_name += i
            else:
                number_test += 1
                album_name += i + ' '
        for i in range(0, len(album_list)):
            if album_name.lower() in album_list[i].lower():
                album_name = album_list[i]
        album = album_name
    try:
        EMBED = discord.Embed(title=f'"{album}" - {artist}', description=f'{release_catagory(data.albums.artists[artist][album][2])} · {data.albums.artists[artist][album][0][0]}, {data.albums.artists[artist][album][0][1]}')
        EMBED.add_field(name='', value=set_list(data.albums.artists[artist][album][1], force=True)[1])
        EMBED.set_footer(text=f'{set_list(data.albums.artists[artist][album][1])[0]} songs, {seconds_converter(sum(data.albums.artists[artist][album][2]))}')
        return EMBED
    except TypeError: 
        misc.out('TypeError in ".alte" embed', 'e')
    except: pass

def soap():
    EMBED = discord.Embed(title='For Steven') #description='We know you dont wash ur hands, we thought this would help')
    EMBED.add_field(
        name='https://www.amazon.ca/Dove-Men-Care-Refreshed-Moisturizing/dp/B0876WWXVH/ref=sr_1_9?keywords=dove+man+soap&qid=1683690407&sr=8-9',
        value='This will not only help with hands, but face and shaving ur beard too.'
    )
    EMBED.add_field(
        name='https://www.amazon.ca/Old-Spice-Soap-Extra-Clean/dp/B0BT55LL7Q/ref=sr_1_3?keywords=old+spice+soap&qid=1683691021&sr=8-3',
        value='This one comes with 4 soaps so you\'ll never run out'
    )
    return EMBED