from random import randint
import time
import discord

def out(text='Hello', event='r'):
    events = {
        'b': '\033[1;35m'+'client'+'\033[0m',
        'i': '\033[1;34m'+'information'+'\033[0m',
        'r': '\033[1;34m'+'report'+'\033[0m',
        'w': '\033[1;33m'+'warning'+'\033[0m',
        'e': '\033[1;31m'+'error'+'\033[0m'
    }
    if event in events:
        event_text = events[event]
    current_time = time.strftime('%y/%m/%d @ %H:%M:%S')
    print(f'co ({current_time}) {event_text}  \t{text}')

def rand_dict(dictionary=dict):
    keys = []
    for key in dictionary:
        keys.append(key)
    rnd = randint(0, len(keys)-1)
    return keys[rnd]

def secondsTo(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if len(str(seconds)) == 1:
        seconds = '0' + str(seconds)
    if hours == 0:
        hours = ''
        minutes = str(minutes) + ':'
    else:
        hours = str(hours) + ':'
        minutes = '0' + str(minutes) + ':'
    return f'{hours}{minutes}{seconds}'

def timeToSeconds(seconds=str):
    end_list = []
    if type(seconds) == list:
        for each in seconds:
            end_result = int(each[0]) * 60 + int(each[2:4])
            end_list.append(end_result)
    else:
        return (int(seconds[0]) * 60 + int(seconds[2:4]))
    return end_list

def albumInfo(data, album, artist='YAY'):
    just_a_number = 1
    album_list = [albums for albums in data]
    album_name = ''
    for i in album:
        if len(album) == 1 or just_a_number == len(album):
            album_name += i
        else:
            just_a_number += 1
            album_name += i + ' '
    for i in range(0, len(album_list)):
        if album_name.lower() in album_list[i].lower():
            album_name = album_list[i]
        #print(album_name, album_list[i])
    ALBUM_INFO = data[album_name][0]
    ALBUM_SONGS = data[album_name][1]

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
                    album_set_info[3] += f'`{album_set_info[1]}` {each_song}\n'
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
    album_set_info[0] += album_set_info[1]

    EMBED = discord.Embed(title=f'{album_name}', description=f'{ALBUM_INFO[4]} by {artist}', color=ALBUM_INFO[3])
    EMBED.add_field(name='',value=album_set_info[3])
    EMBED.set_footer(text=f'{ALBUM_INFO[1]}, {ALBUM_INFO[2]} • {secondsTo(sum(data[album_name][2]))}')
    EMBED.set_thumbnail(url=ALBUM_INFO[0])
    return EMBED

def release_catagory(track_list):
    over_thirty = False # Check to see if the release is over 30 minutes or not.
    song_under_10 = False # Check to see if each song is under or not.
    track_count = 0 # Track count
    for each_song in track_list:
        track_count += 1
        if each_song < 600: # If each song is under 10 minutes.
            song_under_10 = True # Set the check to True.
    if sum(track_list) > 1800: # If the release is over 30 minutes
        over_thirty = True # Set the check to True.
    # A release is considered an album when it is over 39 minutes long and has over 7 tracks
    if over_thirty == True or track_count >= 7:
        return 'Album'
    # EPs are usually less than 30 minutes and has a track range of 4-6 tracks or 1-3 tracks if one track is over 10 minutes.
    elif (over_thirty == False and track_count in range(4, 7)) or (over_thirty == False and song_under_10 == False and track_count in range(1,4)):
        return 'EP'
    # There tends to be one song in a single but there can be up to 3 songs.
    elif track_count in range(1,4) and over_thirty == False and song_under_10 == True:
        return 'Single'
    else: # If all else fails the catagory will be undetermined.
        return 'Undetermined'

def time_to_seconds(seconds=[0]):
    end_list = [] # End result.
    if type(seconds) == list: # If there are multiple
        for each in seconds: # Multiply first half and add the last half of each
            if len(each) == 4: # [0] = First digit | [2:4] = Last two digits.
                end_result = int(each[0]) * 60 + int(each[2:4])
            else: # [0:2] = First two digits | [4:5] = Last two digits.
                end_result = int(each[0:2]) * 60 + int(each[3:5])
            end_list.append(end_result)
    else: # If there is only one/string
        if len(seconds) == 4: # Multiply
            return (int(seconds[0]) * 60 + int(seconds[2:4]))
        else:
            return (int(seconds[0:2]) * 60 + int(seconds[3:5]))
    return end_list

def seconds_converter(seconds=0):
    # Floor divide the seconds by 3600 to get the hour.
    hours = seconds // 3600 # 3600 is one hour in seconds.
    seconds %= 3600 # Remainder of amount of hours.
    # Floor divide the seconds by 60 to get the hour.
    minutes = seconds // 60
    seconds %= 60 # Remainder of minutes
    # FORMATING THE HOURS AND MINUTES #
    if len(str(seconds)) == 1: # If the seconds are a length of one
        seconds = '0' + str(seconds) # Add a zero in front of the second.
    minutes = str(minutes) + ':'
    if len(str(minutes)) == 1 and hours != 0:
            minutes = '0' + str(minutes) + ':'
    if hours != 0: # If there are no hours in the input seconds.
        hours = str(hours) + ':'
    else:
        hours = '' # Set the hour as nothing.
    return f'{hours}{minutes}{seconds}'

def set_list(album=[], force=False):
    album_set_info = [0, 0, 0, ''] # // TOTAL, INDEX, DISC, SET LIST
    padding = '' # This is for when the album is more than 10 tracks or not.
    if len(album) > 9:
        padding = ' '
    for each_disc in album: # For each song in the release.
        if type(each_disc) == list: # If the album is multi-disc.
            album_set_info[2] += 1 # Add one for each disc to the variable.
            album_set_info[3] += f'Disc {album_set_info[2]}\n' # Add the disc number into the set list.
            for each_song in each_disc:
                album_set_info[1] += 1 # For every song add one to the song index.
                # This is to even it out for when it gets to the double digits.
                if len(str(album_set_info[1])) == 1:
                    album_set_info[1] = str(album_set_info[1]) + ' '
                # This is for when i dont like that song.
                if force == False:
                    if '~~' not in each_song:
                        album_set_info[3] += f'`{album_set_info[1]}`{padding}{each_song}\n'
                else:
                    album_set_info[3] += f'`{album_set_info[1]} `{padding}{each_song}\n'
                album_set_info[1] = int(album_set_info[1]) # The index is set back to an integer.
            album_set_info[0] += album_set_info[1] # the index is added to the total.
            album_set_info[1] = 0 # Reset the index for the next disc.
        else: # If it is not a multi-disc.
            # Same routine.
            album_set_info[1] += 1
            if len(str(album_set_info[1])) == 1:
                album_set_info[1] = str(album_set_info[1]) + ' '
            if force == False:
                if '~~' not in each_disc:
                    album_set_info[3] += f'`{album_set_info[1]}{padding}` {each_disc}\n'
            else:
                album_set_info[3] += f'`{album_set_info[1]}{padding}` {each_disc}\n'
            album_set_info[1] = int(album_set_info[1])
    album_set_info[0] += album_set_info[1] # Add index to the total.
    return album_set_info[0], album_set_info[3] # TOTAL AND SET LIST

def cst(hour=0, time='AM', day=0, month=1, year=2023):
    hour, day, month, year = int(hour), int(day), int(month), int(year)
    months_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    if time == 'AM' and hour < 5:
        day -= 1
        if day == 0:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                day = 31
            elif month == 4 or month == 6 or month == 9 or month == 11:
                day = 30
            elif month == 2 and (year % 4) == 0: # LEAP YEAR
                day = 29
            elif month == 2 and (year % 4) != 0: # NOT LEAP YEAR
                day = 28
            month -= 1
            if month == 0:
                month = 12
                year -= 1
    hour = hour - 5
    if hour < 0:
        hour = 24 + hour
    elif hour == 0:
        hour = '00'
    month = months_names[month-1]

    return hour, day, month, year