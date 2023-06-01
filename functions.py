import discord
import random
import misc


def rndSong(data):
    album_list = []
    for i in data:
        album_list.append(i)

    RANDOM_ALBUM = random.randint(0, len(album_list)-1)                                        # Picks a number in range of the input list.
    ALBUM_CHOSEN = album_list[RANDOM_ALBUM]   
    RANDOM_SONG = random.randint(0, len(data[ALBUM_CHOSEN][1])-1)

    ALBUM_INFO = data[ALBUM_CHOSEN][0]
    ALBUM_SONGS = data[ALBUM_CHOSEN][1]
    ALBUM_SONG_LENGTH = data[ALBUM_CHOSEN][2]
    
    EMBED = discord.Embed(title=f'"{ALBUM_SONGS[RANDOM_SONG]}"', description=f'From {ALBUM_CHOSEN} *({ALBUM_INFO[2]})*\nLength: {ALBUM_SONG_LENGTH[RANDOM_SONG]}', color=ALBUM_INFO[3])
    #EMBED.set_footer(text=f'{ALBUM_CHOSEN} • {ALBUM_YEAR}')
    EMBED.set_thumbnail(url=ALBUM_INFO[0])
    return EMBED

def rndAlbum(data):
    album_list = [albums for albums in data]
    RANDOM_ALBUM = random.randint(0, len(album_list)-1)                                        # Picks a number in range of the input list.
    ALBUM_CHOSEN = album_list[RANDOM_ALBUM]                                             # It then chooses the album from the album list.

    ALBUM_INFO = data[ALBUM_CHOSEN][0]
    ALBUM_SONGS = data[ALBUM_CHOSEN][1]

    album_set_info = [0, 0, 0, ''] # TOTAL, INDEX, DISC, SET LIST
    for each_disc in ALBUM_SONGS:
        if type(each_disc) == list:
            album_set_info[2] += 1
            album_set_info[3] += f'Disc {album_set_info[2]}\n'
            for each_song in each_disc:
                album_set_info[1] += 1
                if len(str(album_set_info[1])) == 1:
                    album_set_info[1] = str(album_set_info[1]) + ' '
                if '~~' not in each_song:
                    album_set_info[3] += f'{album_set_info[1]} {each_song}\n'
                album_set_info[1] = int(album_set_info[1])
            album_set_info[0] += album_set_info[1]
            album_set_info[1] = 0
        else:
            album_set_info[1] += 1
            if len(str(album_set_info[1])) == 1:
                album_set_info[1] = str(album_set_info[1]) + ' '
            if '~~' not in each_disc:
                album_set_info[3] += f'`{album_set_info[1]}` {each_disc}\n'
            album_set_info[1] = int(album_set_info[1])
    album_set_info[0] += album_set_info[1]                                        # 

    EMBED = discord.Embed(title=f'{ALBUM_CHOSEN}', description=f'{ALBUM_INFO[1]}, {ALBUM_INFO[2]} • {ALBUM_INFO[4]}', color=ALBUM_INFO[3])
    EMBED.add_field(name='',value=album_set_info[3])
    EMBED.set_footer(text=f'{misc.secondsTo(sum(data[ALBUM_CHOSEN][2]))}')
    EMBED.set_thumbnail(url=ALBUM_INFO[0])
    return EMBED