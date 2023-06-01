# AYDEN ARNAULT-LAFOND #

from misc import timeToSeconds, time_to_seconds

PANTERA = {
    "Cowboys from Hell": [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1105997220869849178/220px-CowboysFromHell.png', 'July 24th', 1990, 0x756542, 'Studio Album'],
        ['Cowboys from Hell', 'Primal Concrete Sledge', 'Psycho Holiday', 'Heresy', 'Cemetery Gates', 'Domination', 'Shattered', 'Clash with Reality', 'Medicine Man', 'Message In Blood', 'The Sleep', 'The Art of Shredding'],
        [246, 133, 319, 287, 422, 304, 202, 316, 315, 314, 347, 258]
    ],
    'Vulgar Display of Power': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1105998662145945600/PanteraVulgarDisplayofPower.png', 'Feburary 25th', 1992, 0x404040, 'Studio Album'],
        ['Mouth for War', 'A New Level', 'Walk', 'Fucking Hostile', 'This Love', 'Rise', 'No Good (Attack the Radical)', 'Live in a Hole', 'Regular People (Conceit)', 'By Demons Be Driven', 'Hollow'],
        [237, 237, 314, 168, 392, 276, 289, 300, 327, 280, 348]
    ],
    'Far Beyond Driven': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1106001068132933692/81iabVrElHL.png', 'March 22nd', 1994, 0x4e85ad, 'Studio Album'],
        ['Strength Beyond Strength', 'Becoming', '5 Minutes Alone', 'I\'m Broken', 'Good Friends and a Bottle of Pills', 'Hard Lines, Sunken Cheeks', 'Slaughtered', '25 Years', 'Shedding Skin', 'Use My Third Arm', 'Throes of Rejection', 'Planet Caravan'],
        [218, 185, 347, 264, 172, 421, 236, 365, 336, 291, 301, 243]
    ],
    'The Great Southern Trendkill': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1106003111174209576/Pantera_The_Great_Southern_Trendkill.png', 'May 7th', 1996, 0xd27025, 'Studio Album'],
        ['The Great Southern Trendkill', 'War Nerve', 'Drag the Waters', '10\'s', '13 Steps to Nowhere', 'Suicide Note Pt. 1', 'Suicide Note Pt. 2', 'Living Through Me (Hell\'s Wrath)', 'Floods', 'The Underground In America', '(Reprise) Sandblasted Skin'],
        [227, 293, 295, 289, 217, 284, 259, 290, 419, 273, 339]
    ],
    'Reinventing the Steel': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1106005278631137280/Pantera_Reinventing_the_Steel.png', 'March 21st', 2000, 0xecca33, 'Studio Album'],
        ['Hellbound', 'Goddamn Electric', 'Yesterday Don\'t Mean Shit', 'You\'ve Got to Belong to It', 'Revolution Is My Name', 'Death Rattle', 'We\'ll Grind That Axe for a Long Time', 'Uplift', 'It Makes Them Disappear', 'I\'ll Cast a Shadow'],
        [161, 296, 259, 253, 315, 197, 224, 225, 381, 322]
    ]
}

METALLICA = {
    'Kill \'Em All': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1108214467709386822/Metallica_-_Kill_27Em_All_cover.png', 'July 25th', 1983, 0xeb1c23, 'Studio Album'],
        ['Hit The Lights', 'The Four Horsemen', 'Motorbreath', '(Anesthesia) - Pulling Teeth', 'Whiplash', 'Phantom Lord', 'No Resmorse', 'Seek & Destory', 'Metal Militia'],
        timeToSeconds(['4:17', '7:13', '3:08', '4:42', '4:15', '4:09', '5:02', '6:27', '6:56', '5:11'])
    ],
    'Ride The Lightning': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1108214155049193482/2Q.png', 'July 27th', 1984, 0x233f7b, 'Studio Album'],
        ['Fight Fire With Fire', 'Ride The Lightning', 'For Whom The Bell Tolls', 'Fade To Black', 'Trapped Under Ice', 'Escape', 'Creeping Death', 'The Call Of Ktulu'],
        timeToSeconds(['4:44', '6:37', '5:11', '6:55', '4:04', '4:24', '6:36', '8:55'])
    ],
    'Master of Puppets': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1108214582603960341/Metallica_-_Master_of_Puppets_cover.png', 'March 3rd', 1986, 0xda7541, 'Studio Album'],
        ['Battery', 'Master of Puppets', 'The Thing That Should Not Be', 'Welcome Home (Sanitarium)', 'Disposable Heroes', 'Leper Messiah', 'Orion', 'Damage Inc.  🅴'],
        timeToSeconds(['5:13', '8:36', '6:36', '6:27', '8:17', '5:40', '8:27', '5:32'])
    ],
    '...And Justice for All': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1108214969331355731/image.png', 'Semptember 7th', 1989, 0xbbd48f, 'Studio Album'],
        ['Blackened', '...And Justice for All', 'Eye Of The Beholder', 'One', 'The Shortest Straw', 'Harvester Of Sorrow', 'The Frayed Ends of Sanity', 'To Live Is to Die', 'Dyers Eve  🅴'],
        timeToSeconds(['6:42', '9:46', '6:25', '7:26', '6:35', '5:45', '7:43', '9:49', '5:14'])
    ],
    'Metallica': [
        ['https://cdn.discordapp.com/attachments/812562361399115820/1108214051907063839/9k.png', 'August 12th', 1991, 0x090e10, 'Studio Album'],
        ['Enter Sandman', 'Sad but True', 'Holier Than Thou', 'Wherever I May Roam', 'Don\'t Tread On Me', 'Through The Never', 'Nothing Else Matters', 'Of Wolf And Man', 'The God That Failed', 'My Friend of Misery', 'The Struggle Within'],
        timeToSeconds(['5:31', '5:24', '3:47', '6:27', '6:44', '4:00', '4:04', '6:28', '4:16', '5:08', '6:49', '3:53'])
    ],
    'Load': [
        [],
        [],
        [],
    ],
    'Reload': [],
    'Death Magnetic': [],
    'Hardwired... to Self-Destruct': [
        ['', '', 2016, 0x111111, '1:23:00'],
        ['Hardwired `🅴`', 'Atlas, Rise!', 'Now That We\'re Dead', 'Moth Into Flame', 'Dream No More', 'Halo On Fire', 'Confusion', 'ManUNkind', 'Here Comes Revenge', 'Am I Savage?', 'Murder One', 'Spit Out the Bone']
    ],
    '72 Seasons': []
}

artists = { # In Order of A-Z
    'Avatar': { # In Order of Year #
        'Black Waltz': [
            ['January 12th', 2012],
            ['~~Let Us Die~~', 'Torn Apart', '~~Ready For the Ride~~', 'Napalm', '~~Black Waltz~~', '~~Blod~~', 'Let It Burn', '~~One Touch~~', '~~Paint Me Red~~', 'Smells Like a Freak Show', '~~Use Your Tongue~~'],
            time_to_seconds(['4:12', '6:29', '3:14', '5:32', '5:58', '3:34', '3:32', '4:17', '4:27', '4:53', '9:33'])
        ],
        'Feathers & Flesh': [
            ['May 13th', 2016],
            ['~~Regret~~', '~~House of Eternal Hunt~~', 'The Eagle Has Landed', '~~New Land~~', '~~Tooth, Beak & Claw~~', 'For the Swarm', '~~Fiddler\'s Farewell~~', '~~One More Hill~~', '~~Black Waters~~', 'Night Never Ending', '~~Pray the Sun Away~~', '~~When the Snow Lies Red~~', '~~Raven Wine~~', '~~Sky Burial~~'],
            time_to_seconds(['2:01', '4:58', '5:01', '4:31', '4:25', '1:54', '4:57', '4:13', '5:38', '3:33', '5:30', '5:16', '4:36', '6:54'])
        ],
        'Avatar Country': [
            ['January 12th', 2018],
            ['~~Glory to Our King~~', '~~Legend of the King~~', 'The King Welcomes You to Avatar Country', '~~King\'s Harvest~~', 'The King Wants You', '~~The King Speaks~~', 'A Statue of the King', '~~King After King~~', '~~Silent Songs of the King Pt. 1: Winter Comes When the King Dreams of Snow~~', '~~Silent Songs of the King Pt. 2: The King\'s Palace~~'],
            time_to_seconds(['0:51', '8:17', '5:36', '3:55', '4:20', '3:17', '3:44', '5:07', '3:34'])
        ],
        'Hunter Gatherer': [
            ['August 7th', 2020],
            ['~~Silence in the Age of Apes~~', 'Colossus', 'A Secret Door', '~~God of Sick Dreams~~', '~~Scream Until You Wake~~', '~~Child~~', '~~Justice~~', '~~Gun~~', '~~When All but Force Has Failed~~', '~~Wormhole~~'],
            time_to_seconds(['4:21', '4:01', '6:06', '3:57', '4:10', '5:33', '4:41', '4:31', '2:48', '5:20'])
        ],
        'So Sang the Hollow': [
            ['October 29th', 2021],
            ['So Sang the Hollow'],
            time_to_seconds(['4:51'])
        ],
        'Construction of Souls': [
            ['November 26th', 2021],
            ['Construction of Souls'],
            time_to_seconds(['0:01'])
        ]
    },
    'Bring Me The Horizon': {
        'Post Human: Survival Horror': [
            ['October 30th', 2020],
            ['Dear Diary, 🅴', 'Parasite Eve 🅴', 'Teardrops 🅴', 'Obey (with YUNGBLUD) 🅴', 'Itch for the Cure (When Will We Be Free?)', 'Kingslayer (feat. BABYMETAL) 🅴', '1x1 (feat. Nova Twins) 🅴', 'Ludens', 'One Day the Only Butterflies Left Will Be In Your Chest as You March Towards Your Death (featuring Amy Lee) 🅴'],
            time_to_seconds(['2:44', '4:51', '3:35', '3:40', '1:26', '3:38', '3:29', '4:40', '4:03'])
        ]
    },
    'Metallica': {
        'Kill \'Em All': [
            ['July 25th', 1983, 0xeb1c23],
            ['Hit The Lights', 'The Four Horsemen', 'Motorbreath', '(Anesthesia) - Pulling Teeth', 'Whiplash', 'Phantom Lord', 'No Resmorse', 'Seek & Destory', 'Metal Militia'],
            timeToSeconds(['4:17', '7:13', '3:08', '4:42', '4:15', '4:09', '5:02', '6:27', '6:56', '5:11'])
        ],
        'Ride The Lightning': [
            ['July 27th', 1984, 0x233f7b],
            ['Fight Fire With Fire', 'Ride The Lightning', 'For Whom The Bell Tolls', 'Fade To Black', 'Trapped Under Ice', 'Escape', 'Creeping Death', 'The Call Of Ktulu'],
            timeToSeconds(['4:44', '6:37', '5:11', '6:55', '4:04', '4:24', '6:36', '8:55'])
        ],
        'Master of Puppets': [
            ['March 3rd', 1986, 0xda7541],
            ['Battery', 'Master of Puppets', 'The Thing That Should Not Be', 'Welcome Home (Sanitarium)', 'Disposable Heroes', 'Leper Messiah', 'Orion', 'Damage Inc.  🅴'],
            timeToSeconds(['5:13', '8:36', '6:36', '6:27', '8:17', '5:40', '8:27', '5:32'])
        ],
        '...And Justice for All': [
            ['Semptember 7th', 1989, 0xbbd48f],
            ['Blackened', '...And Justice for All', 'Eye Of The Beholder', 'One', 'The Shortest Straw', 'Harvester Of Sorrow', 'The Frayed Ends of Sanity', 'To Live Is to Die', 'Dyers Eve  🅴'],
            timeToSeconds(['6:42', '9:46', '6:25', '7:26', '6:35', '5:45', '7:43', '9:49', '5:14'])
        ],
        'Metallica': [
            ['August 12th', 1991, 0x090e10],
            ['Enter Sandman', 'Sad but True', 'Holier Than Thou', 'Wherever I May Roam', 'Don\'t Tread On Me', 'Through The Never', 'Nothing Else Matters', 'Of Wolf And Man', 'The God That Failed', 'My Friend of Misery', 'The Struggle Within'],
            timeToSeconds(['5:31', '5:24', '3:47', '6:27', '6:44', '4:00', '4:04', '6:28', '4:16', '5:08', '6:49', '3:53'])
        ],
        'Death Magnetic': [
            ['September 12th', 2008],
            ['That Was Just Your Life', 'The End of the Line', 'Broken, Beat & Scarred', 'The Day That Never Comes', 'All Nightmare Long', 'Cyanide', 'The Unforgiven III', 'The Judas Kiss', 'Suicide & Redemption', 'My Apocalyse'],
            time_to_seconds(['7:08', '7:52', '6:25', '7:56', '7:58', '6:40', '7:47', '8:01', '9:58', '5:01'])
        ],
        'Hardwired... to Self-Destruct': [
            ['November 18th', 2016],
            [['Hardwired 🅴', 'Atlas, Rise!', 'Now That We\'re Dead', 'Moth Into Flame', 'Dream No More', 'Halo On Fire'], ['Confusion', 'ManUNkind', 'Here Comes Revenge', 'Am I Savage?', 'Murder One', 'Spit Out the Bone']],
            time_to_seconds(['3:09', '6:28', '6:59', '5:50', '6:29', '8:15', '6:43', '6:55', '7:17', '6:30', '5:45', '7:09'])
        ]
    },
    'My Chemical Romance': {
        'I Brought You My Bullets, You Brought Me Your Love': [
            ['July 23rd', 2002],
            ['~~Romance~~', 'Honey, This Mirror Isn\'t Big Enough for the Two of Us 🅴', 'Vampires Will Never Hurt You', '~~Drowning Lessons~~', '~~Our Lady Sorrows 🅴~~', 'Headfirst for Halos', '~~Skylines and Turnstiles~~', 'Early Sunsets over Monroeville', '~~This Is the Best Day Ever~~', '~~Cubicles~~', '~~Demolition Lovers~~'],
            time_to_seconds(['30:01'])
        ],
        'Number Three': [
            ['November 18th', 2012],
            ['~~The World Is Ugly~~', 'The Light Behind Your Eyes'],
            time_to_seconds(['4:54', '5:12'])
        ]
    },
    'Pantera': {
        "Cowboys from Hell": [
            ['July 24th', 1990, 0x756542],
            ['Cowboys from Hell', 'Primal Concrete Sledge', 'Psycho Holiday', 'Heresy', 'Cemetery Gates', 'Domination', 'Shattered', 'Clash with Reality', 'Medicine Man', 'Message In Blood', 'The Sleep', 'The Art of Shredding'],
            [246, 133, 319, 287, 422, 304, 202, 316, 315, 314, 347, 258]
        ],
        'Vulgar Display of Power': [
            ['Feburary 25th', 1992, 0x404040],
            ['Mouth for War', 'A New Level', 'Walk', 'Fucking Hostile', 'This Love', 'Rise', 'No Good (Attack the Radical)', 'Live in a Hole', 'Regular People (Conceit)', 'By Demons Be Driven', 'Hollow'],
            [237, 237, 314, 168, 392, 276, 289, 300, 327, 280, 348]
        ],
        'Far Beyond Driven': [
            ['March 22nd', 1994, 0x4e85ad],
            ['Strength Beyond Strength', 'Becoming', '5 Minutes Alone', 'I\'m Broken', 'Good Friends and a Bottle of Pills', 'Hard Lines, Sunken Cheeks', 'Slaughtered', '25 Years', 'Shedding Skin', 'Use My Third Arm', 'Throes of Rejection', 'Planet Caravan'],
            [218, 185, 347, 264, 172, 421, 236, 365, 336, 291, 301, 243]
        ],
        'The Great Southern Trendkill': [
            ['May 7th', 1996, 0xd27025],
            ['The Great Southern Trendkill', 'War Nerve', 'Drag the Waters', '10\'s', '13 Steps to Nowhere', 'Suicide Note Pt. 1', 'Suicide Note Pt. 2', 'Living Through Me (Hell\'s Wrath)', 'Floods', 'The Underground In America', '(Reprise) Sandblasted Skin'],
            [227, 293, 295, 289, 217, 284, 259, 290, 419, 273, 339]
        ],
        'Reinventing the Steel': [
            ['March 21st', 2000, 0xecca33],
            ['Hellbound', 'Goddamn Electric', 'Yesterday Don\'t Mean Shit', 'You\'ve Got to Belong to It', 'Revolution Is My Name', 'Death Rattle', 'We\'ll Grind That Axe for a Long Time', 'Uplift', 'It Makes Them Disappear', 'I\'ll Cast a Shadow'],
            [161, 296, 259, 253, 315, 197, 224, 225, 381, 322]
        ],
        'Piss': [
            ['April 12th', 2012],
            ['Piss'],
            time_to_seconds(['4:22'])
        ]
    }
    #'Gojira': {
    #    'From Mars to Sirius': [
    #        ['1'],
    #        []
    #    ]
    #}
}