class Character:
    """
    This class stores characters stats and attributes that are semistatic (they only change after a scenario)
    It also contains another object to track dynamic in-game attributes such as status and damage applied.

    The involved stats and attributes of each character  are as follows.

    Name -- Duh.
    Race -- Species of the character.
    Discipline -- This describes the role or class of the character.
    Life Pool -- This is health points.
    Action Pool -- This is the base value of a character's action points. Which are spent on every combat action.
    Focus Pool -- This is mana.
    Will Pool -- This measures a character's ability to stay sane and focused. Can be spent on Hellbent combat actions.
    Transcendence Pool -- Can be invested on lifesaving combat rerolls, on bonus rolls or to automatically pass a non-combat challenge. At the end of a scenario, they can be used on different ways to leave a mark on history, to erase some scars or to gain virtues.

    Main Stats
        *Body -- Physical Prowess.
        *Control -- Coordination and swiftness.
        *Mind -- Alertness & Mental Prowess.
        *Spirit -- Will and mental fortitude.
        *Presence -- Appearance, "shadow-casting" and destiny in the eyes of the gods.

    Each main stat has substats. A utility stat and a pool stat.
    Body stats
        *Vigor -- Strength and power.
        *Constitution -- Physical fortitude. Determines Life Pool.
    Control stats
        *Dexterity -- Precision, coordination, equilibrium. Ability to perform skillfully difficult tasks with hands.
        *Agility -- Swiftness and acrobatics. Determines action pool.
    Mind stats
        *Awareness -- Wariness of surroundings, vigilance and ability to capture subtle details.
        *Wit -- Inventive thought and quick understanding. Ability to focus and keen intelligence. Determines Focus Pool.
    Spirit stats
        *Soul -- Mind over matter ability. The force and power of the non-physical self. How the body digest magic. Calculates sturdiness against spells.
        *Willpower -- Sheer will. Ability to stay sane and calm in the face of peril and to fight the urges of the body. Determines Will Pool.
    Presence stats
        *Charisma -- How the mortals see the character. Social prowess. Calculates appearance and "shadow-casting".
        *Providence -- How the gods see the character. Determines Transcendence pool.

    Next are skill stats, those determine the variety of skills on each branch the character can learn. And the ranks they can assign to them.
    Skill stats
        *Combat -- The way of the steel.
        *Stealth -- Stay in the shadows.
        *Knowledge -- Harness reality.
        *Magic -- Master the spellcraft.
        *Social -- Silver tongue.




    Also this class stores:
        *A class to track inventory and carrying.
        *A dictionary to store skills.
        *A dictionary to store abilities.
        *A dictionary to store scars and virtues.
        *A dictionary to store historical data.
        *A dictionary to store traits and feats.



"""

    def __init__(self, name, race, discipline):
        """

        :param name: Character's identity
        :param race: Species of the character.
        :param discipline: Class of the character.
        """
        self.__name = name
        self.__race = race
        self.__discipline = discipline
        self.__stats = {}
    
    def setBody(self, body):
        self.__stats['body'] = body

    def setControl(self, control):
        self.__stats['control'] = control

    def setMind(self, mind):
        self.__stats['mind'] = mind

    def setSpirit(self, spirit):
        self.__stats['spirit'] = spirit

    def setPresence(self, presence):
        self.__stats['presence'] = presence

    def getBody(self):
        return self.__stats.get("body")

    def getControl(self):
        return self.__stats.get("control")

    def getMind(self):
        return self.__stats.get("mind")

    def getSpirit(self):
        return self.__stats.get("spirit")

    def getName(self):
        return self.__name

    def getRace(self):
        return self.__race

    def getDiscipline(self):
        return self.__discipline

    def setVigor(self, vigor):
        self.__stats['vigor'] = vigor

    def setConstitution(self, constitution):
        self.__stats['constitution'] = constitution

    def setAgility(self, agility):
        self.__stats['agility'] = agility

    def setDexterity(self, dexterity):
        self.__stats['dexterity'] = dexterity

    def setAwareness(self, awareness):
        self.__stats['awareness'] = awareness

    def setWit(self, wit):
        self.__stats['wit'] = wit

    def setSoul(self, soul):
        self.__stats['soul'] = soul

    def setWillpower(self, willpower):
        self.__stats['willpower'] = willpower

    def setCharisma(self, charisma):
        self.__stats['charisma'] = charisma

    def setProvidence(self, providence):
        self.__stats['providence'] = providence

    def setLifePool(self, lifepool):
        self.__lifepool = lifepool

    def setActionPool(self, actionpool):
        self.__actionpool = actionpool

    def setFocusPool(self, focuspool):
        self.__focuspool = focuspool

    def setWillPool(self, willpool):
        self.__willpool = willpool

    def setTranscendencePool(self, transcendencepool):
        self.__transcendencepool = transcendencepool

    def getVigor(self):
        return self.__stats['vigor']

    def getConstitution(self):
        return self.__stats['constitution']

    def getDexterity(self):
        return self.__stats['dexterity']

    def getAgility(self):
        return self.__stats['agility']

    def getAwareness(self):
        return self.__stats['awareness']

    def getWit(self):
        return self.__stats['wit']

    def getSoul(self):
        return self.__stats['soul']

    def getWillpower(self):
        return self.__stats['willpower']

    def getCharisma(self):
        return self.__stats['charisma']

    def getProvidence(self):
        return self.__stats['providence']

    def getLifePool(self):
        return self.__lifepool

    def getActionPool(self):
        return self.__actionpool

    def getFocusPool(self):
        return self.__focuspool

    def getWillPool(self):
        return self.__willpool

    def getTranscendence(self):
        return self.__transcendencepool

    def setMainStats(self, body, control, mind, spirit, presence):
        self.setBody(body)
        self.setControl(control)
        self.setMind(mind)
        self.setSpirit(spirit)
        self.setPresence(presence)

    def setSubStats(self,vigor,constitution,dexterity,agility,awareness,wit,soul,willpower,charisma,providence):
        self.setVigor(vigor)
        self.setConstitution(constitution)
        self.setDexterity(dexterity)
        self.setAgility(agility)
        self.setAwareness(awareness)
        self.setWit(wit)
        self.setSoul(soul)
        self.setWillpower(willpower)
        self.setCharisma(charisma)
        self.setProvidence(providence)

    def getStats(self):
        return self.__stats

    def setCombat(self, combat):
        self.__stats['combat'] = combat

    def setStealth(self, stealth):
        self.__stats['stealth'] = stealth

    def setKnowledge(self, knowledge):
        self.__stats['knowledge'] = knowledge

    def setMagic(self, magic):
        self.__stats['magic'] = magic

    def setSocial(self, social):
        self.__stats['social'] = social

    def getCombat(self):
        return self.__stats['combat']

    def getStealth(self):
        return self.__stats['stealth']

    def getKnowledge(self):
        return self.__stats['knowledge']

    def getMagic(self):
        return self.__stats['magic']

    def getSocial(self):
        return self.__stats['social']

    def setSkillstats(self, combat, stealth, knowledge, magic, social):
        self.setCombat(combat)
        self.setStealth(stealth)
        self.setKnowledge(knowledge)
        self.setMagic(magic)
        self.setSocial(social)








