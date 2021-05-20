import pygame
pygame.init()
pygame.mixer.init()

##letterkeys = ['K_a','K_b','K_c','K_d','K_e','K_f','K_g','K_h','K_i','K_j','K_k','K_l','K_m','K_n','K_o','K_p','K_q','K_r','K_s','K_t','K_u','K_v','K_w','K_x','K_y','K_z']
errorSFX = pygame.mixer.Sound('../resources/sounds/interface/error.wav')
switchSFX = pygame.mixer.Sound('../resources/sounds/interface/switch.wav')
inputSFX = pygame.mixer.Sound('../resources/sounds/interface/input.wav')
emptyBar = pygame.image.load('../resources/bars/empty.png')
bodyBar = pygame.image.load('../resources/bars/body.png')
controlBar = pygame.image.load('../resources/bars/control.png')
mindBar = pygame.image.load('../resources/bars/mind.png')
spiritBar = pygame.image.load('../resources/bars/spirit.png')
presenceBar = pygame.image.load('../resources/bars/presence.png')
bodyIcon = pygame.image.load('../resources/icons/bodyicon.png')
bodyIcon = pygame.transform.scale(bodyIcon,(32,32))
bodyIconSelected = pygame.image.load('../resources/icons/bodyiconselect.png')
bodyIconSelected = pygame.transform.scale(bodyIconSelected,(32,32))
controlIcon = pygame.image.load('../resources/icons/controlicon.png')
controlIcon = pygame.transform.scale(controlIcon,(32,32))
controlIconSelected = pygame.image.load('../resources/icons/controliconselect.png')
controlIconSelected = pygame.transform.scale(controlIconSelected,(32,32))
mindIcon = pygame.image.load('../resources/icons/mindicon.png')
mindIcon = pygame.transform.scale(mindIcon,(32,32))
mindIconSelected = pygame.image.load('../resources/icons/mindiconselect.png')
mindIconSelected = pygame.transform.scale(mindIconSelected,(32,32))
spiritIcon = pygame.image.load('../resources/icons/spiriticon.png')
spiritIcon = pygame.transform.scale(spiritIcon,(32,32))
spiritIconSelected = pygame.image.load('../resources/icons/spiriticonselect.png')
spiritIconSelected = pygame.transform.scale(spiritIconSelected,(32,32))
presenceIcon = pygame.image.load('../resources/icons/presenceicon.png')
presenceIcon = pygame.transform.scale(presenceIcon,(32,32))
presenceIconSelected = pygame.image.load('../resources/icons/presenceiconselect.png')
presenceIconSelected = pygame.transform.scale(presenceIconSelected,(32,32))

bodyCount = 1
controlCount = 1
mindCount = 1
spiritCount = 1
presenceCount = 1
letterkeys = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,59]
arrowkeys = [273, 274, 275, 276]

disciplines = ['none','Warrior','Scout','Rogue','Healer','Fighter','Alchemist','Mage','Evoker','Mystic','Marksman','Enchanter','Vanguard']

(width, height) = (800, 600)
menuSelection = 0
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font("../resources/font/m5x7.ttf", 20)
clock = pygame.time.Clock()

def sheetCreatorMenu():
    global screen
    global letterkeys
    global disciplines
    global emptyBar,bodyBar,controlBar,mindBar,spiritBar,presenceBar
    global bodyCount,controlCount,mindCount,spiritCount,presenceCount
    global bodyIcon,controlIcon,mindIcon,spiritIcon,presenceIcon
    global bodyIconSelected,controlIconSelected,mindIconSelected,spiritIconSelected,presenceIconSelected
    global errorSFX,switchSFX,inputSFX
    option = 1
    discipline = 0
    attravailable = 45
    nametext = ""

    while True:
        if option != 3:
            bodyLabel  = setText("Body ("+ str(bodyCount) +")", True, (255,0,0))
        else:
            bodyLabel = setText("[[Body]] (" + str(bodyCount) + ")", True, (255, 0, 0))
        if option != 4:
            controlLabel = setText("Control ("+ str(controlCount)+")", True, (0,128,64))
        else:
            controlLabel = setText("[[Control]] (" + str(controlCount) + ")", True, (0, 128, 64))
        if option != 5:
            mindLabel = setText("Mind ("+ str(mindCount)+")", True, (63,72,204))
        else:
            mindLabel = setText("[[Mind]] (" + str(mindCount) + ")", True, (63, 72, 204))
        if option != 6:
            spiritLabel = setText("Spirit ("+ str(spiritCount)+")", True, (163,73,164))
        else:
            spiritLabel = setText("[[Spirit]] (" + str(spiritCount) + ")", True, (163, 73, 164))
        if option != 7:
            presenceLabel = setText("Presence ("+ str(presenceCount)+")",True,(255,242,0))
        else:
            presenceLabel = setText("[[Presence]] (" + str(presenceCount) + ")", True, (255, 242, 0))
        if option == 1:
            namelabel = setText("[[Name:]]", True, (255, 0, 0))
        else:
            namelabel = setText("Name:", True, (255, 0, 0))
        if option == 2:
            classlabel = setText("[[Discipline:]]", True, (255, 0, 0))
        else:
            classlabel = setText("Discipline:", True, (255, 0, 0))
        if 2 < option < 8:
            attributeslabel = setText("[[Attributes:]]", True, (255, 0, 0))
        else:
            attributeslabel = setText("Attributes:", True, (255, 0, 0))


        namebox = setText(nametext, True, (255, 255, 255))
        disciplinebox = setText(disciplines[discipline], True, (255,255,255))
        attravailablebox = setText('('+str(attravailable)+' points available)', True, (255,255,255))
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return

            if e.type == pygame.KEYDOWN:
                print(e.key)
                if e.key == 273 and option == 1:
                    errorSFX.play()
                if e.key == 274 and option == 9:
                    errorSFX.play()
                if e.key in letterkeys and option == 1 and len(nametext) < 10:
                   nametext += e.unicode
                   inputSFX.play()
                if e.key == 8 and option == 1 and nametext != '':
                    nametext = nametext[:-1]
                    inputSFX.play()
                if e.key == 273 and option > 1:
                    option = option - 1
                    switchSFX.play()

                if e.key == 274 and option < 9:
                    option = option + 1
                    switchSFX.play()
                if e.key == 275 and option == 2 and discipline < len(disciplines)-1:
                    discipline += 1
                    inputSFX.play()
                if e.key == 276 and option == 2 and discipline > 1:
                    discipline -= 1
                    inputSFX.play()
                if e.key == 275 and 2 < option < 8:
                    if option == 3 and (bodyCount == 20 or attravailable == 0):
                        errorSFX.play()
                    if option == 3 and bodyCount < 20 and attravailable > 0:
                        bodyCount += 1
                        attravailable -= 1
                        inputSFX.play()
                    if option == 4 and (controlCount == 20 or attravailable == 0):
                        errorSFX.play()
                    if option == 4 and controlCount < 20 and attravailable > 0:
                        controlCount += 1
                        attravailable -= 1
                        inputSFX.play()
                    if option == 5 and (mindCount == 20 or attravailable == 0):
                        errorSFX.play()
                    if option == 5 and mindCount < 20 and attravailable > 0:
                        mindCount += 1
                        attravailable -= 1
                        inputSFX.play()
                    if option == 6 and (spiritCount == 20 or attravailable == 0):
                        errorSFX.play()
                    if option == 6 and spiritCount < 20 and attravailable > 0:
                        spiritCount += 1
                        attravailable -= 1
                        inputSFX.play()
                    if option == 7 and (presenceCount == 20 or attravailable == 0):
                        errorSFX.play()
                    if option == 7 and presenceCount < 20 and attravailable > 0:
                        presenceCount += 1
                        attravailable -= 1
                        inputSFX.play()
                if e.key == 276 and 2 < option < 8:
                    if option == 3 and bodyCount == 1:
                        errorSFX.play()
                    if option == 3 and bodyCount > 1:
                        bodyCount -= 1
                        attravailable += 1
                        inputSFX.play()
                    if option == 4 and controlCount == 1:
                        errorSFX.play()
                    if option == 4 and controlCount > 1:
                        controlCount -= 1
                        attravailable += 1
                        inputSFX.play()
                    if option == 5 and mindCount == 1:
                        errorSFX.play()
                    if option == 5 and mindCount > 1:
                        mindCount -= 1
                        attravailable += 1
                        inputSFX.play()
                    if option == 6 and spiritCount == 1:
                        errorSFX.play()
                    if option == 6 and spiritCount > 1:
                        spiritCount -= 1
                        attravailable += 1
                        inputSFX.play()
                    if option == 7 and presenceCount == 1:
                        errorSFX.play()
                    if option == 7 and presenceCount > 1:
                        presenceCount -= 1
                        attravailable += 1
                        inputSFX.play()

        inCreator = True
        screen.fill((0, 0, 0))
        screen.blit(namelabel, (40 - namelabel.get_width() // 2, 60 - namelabel.get_height() // 2))
        screen.blit(namebox, (40 // 2, 80 - namebox.get_height() // 2))
        screen.blit(classlabel, (40// 2, 100 - classlabel.get_height() // 2))
        screen.blit(disciplinebox, (40 //2 , 120 - disciplinebox.get_height() // 2))
        screen.blit(attributeslabel, (40//2, 140 - attributeslabel.get_height() // 2))
        screen.blit(attravailablebox, (220//2, 140 - attributeslabel.get_height() // 2))
        if option == 3:
            screen.blit(bodyIconSelected, (5, 160))
        else:
            screen.blit(bodyIcon, (5,160))
        if option == 4:
            screen.blit(controlIconSelected, (5,200))
        else:
            screen.blit(controlIcon, (5,200))
        if option == 5:
            screen.blit(mindIconSelected, (5,240))
        else:
            screen.blit(mindIcon,(5,240))
        if option == 6:
            screen.blit(spiritIconSelected,(5,280))
        else:
            screen.blit(spiritIcon,(5,280))
        if option == 7:
            screen.blit(presenceIconSelected,(5,320))
        else:
            screen.blit(presenceIcon,(5,320))

        screen.blit(bodyLabel, (40, 160))
        screen.blit(controlLabel,(40, 200))
        screen.blit(mindLabel,(40,240))
        screen.blit(spiritLabel,(40,280))
        screen.blit(presenceLabel,(40,320))
        for i in range(20):
            if i < bodyCount:
                screen.blit(bodyBar,(160+(i*5),160))
            else:
                screen.blit(emptyBar,(160+(i*5),160))
            if i < controlCount:
                screen.blit(controlBar,(160+(i*5),200))
            else:
                screen.blit(emptyBar,(160+(i*5),200))
            if i < mindCount:
                screen.blit(mindBar,(160+(i*5),240))
            else:
                screen.blit(emptyBar,(160+(i*5),240))
            if i < spiritCount:
                screen.blit(spiritBar,(160+(i*5),280))
            else:
                screen.blit(emptyBar,(160+(i*5),280))
            if i < presenceCount:
                screen.blit(presenceBar,(160+(i*5),320))
            else:
                screen.blit(emptyBar,(160+(i*5),320))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


def setText(text, antialias, color):
    global font
    return font.render(text, antialias, color,(0,0,0))


def drawText(text, x, y, screen):
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


sheetCreatorMenu()
