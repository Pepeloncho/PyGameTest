skills = {
##Body Based skills
    'climb':        {
                        'name':'Climb',
                        'main_stats':['vigor'],
                        'untrained': True,
                        'requisites': {
                                       'vigor': 7
                                        },
                        'maxrank':3,
                        'pointscale':[1,3,5],
                        'tooltips':['tooltip_1','tooltip_2','tooltip_3']
    },
    'swim':         {
                        'name':'Swim',
                        'main_stats':['vigor','agility'],
                        'untrained': True,
                        'requisites': {
                                        'vigor' : 5,
                                        'agility' : 5
                                    },
                        'maxrank': 2,
                        'pointscale':[1,3],
                        'tooltips':['tooltip_1','tooltip_2']
    },
    'fight':        {
                        'name':'Fight',
                        'main_stats':['vigor'],
                        'untrained': True
                        'requisites': {
                                        'vigor':8,
                                        'dex':2
                        },
                        'maxrank':3,
                        'pointscale':[1,3,5],
                        'tooltips':['tooltip_1','tooltip_2','tooltip_3']

    },
    'grapple':      {
                        'name':'Grapple',
                        'main_stats':['vigor'],
                        'untrained': True
    },

    'rush':         {
                        'name':'Rush down',
                        'main_stats':['vigor'],
                        'untrained': True
    },
    'push':         {
                        'name':'Push',
                        'main_stats':['vigor'],
                        'untrained': True
    },
##Control Based skills

    'stealth':      {
                      'name':'Stealth',
                      'main_stats':['dexterity'],
                      'untrained': True
                    },
    'balance':      {
                        'name':'Balance',
                        'main_stats':['dexterity'],
                        'untrained': True

                    },

    'roll':         {
                        'name':'Roll',
                        'main_stats':['dexterity','agility'],
                        'untrained': False
                    },
    'jump':         {
                        'name':'Jumping and falling',
                        'main_stats':['agility'],
                        'untrained': True
                    },
    'sprint':       {
                        'name':'Sprint',
                        'main_stats':['agility'],
                        'untrained': True
                    },
    'strafe':       {
                        'name':'Strafe',
                        'main_stats':['agility'],
                        'untrained': True
                    },
    'dive':         {
                        'name':'Dive',
                        'main_stats':['agility'],
                        'untrained': True
                    },

    'disarm':       {
                        'name':'Disarm Device',
                        'main_stats':['dexterity'],
                        'untrained': True
                    },
    'openlock':      {
                        'name':'Open Lock',
                        'main_stats':['dexterity'],
                        'untrained': False
                    },
    'escape':        {
                        'name':'Escape',
                        'main_stats':['dexterity'],
                        'untrained': True
                    },
    'ride':          {
                        'name':'Ride',
                        'main_stats':['dexterity'],
                        'untrained': True
                        },
    'throw':          {
                        'name':'Throw',
                        'main_stats':['dexterity'],
                        'untrained': True
    },
    'throwS':       {
                        'name':'Throw (small)',
                        'main_stats':['dexterity','vigor'],
                        'untrained': True
    },
    'throwM':       {
                        'name':'Throw (medium)',
                        'main_stats':['dexterity','vigor','vigor'],
                        'untrained': True
    },
    'throwL':       {
                        'name':'Throw (large)',
                        'main_stats':['dexterity','vigor','vigor','vigor'],
                        'untrained': True
    },

##Mind based skills
    'vigilance':    {
                        'name':'Vigilance',
                        'main_stats':['awareness'],
                        'untrained': True
    },

    'sense':   {
                        'name':'Sense',
                        'main_stats':['awareness'],
                        'untrained': True
    },
    'observe':  {
                        'name':'Observe',
                        'main_stats':['awareness'],
                        'untrained': True
    },
    'hunch':  {
                        'name':'Hunch',
                        'main_stats':['awareness'],
                        'untrained': True
    },
    '/': {

    }
}