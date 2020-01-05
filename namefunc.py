def nameMaker(screen, font):
    nameAsciiValue = [65,65,65]#sets defaulf ascii to 'A'
    nameAsciiIndex = 0
    #screen.blit(font.render("Name:", 200, (255, 255, 255)), (450, 0))
    while True:
        pygame.display.update()
        rectangl = (200+nameAsciiIndex*300, 150, 400, 400)
        pygame.draw.rect(screen, (0,0,0), rectangl)
        screen.blit(font.render("{0}".format(chr(nameAsciiValue[nameAsciiIndex])), 200, (255, 255, 255)), (200+nameAsciiIndex*300, 150))
        print(nameAsciiValue)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    nameAsciiValue[nameAsciiIndex]+= 1
                    if nameAsciiValue[nameAsciiIndex] > 90: nameAsciiValue[nameAsciiIndex] = 65
                elif event.key == pygame.K_DOWN:
                    nameAsciiValue[nameAsciiIndex] -= 1
                    if nameAsciiValue[nameAsciiIndex] < 65: nameAsciiValue[nameAsciiIndex] = 90
                elif event.key == pygame.K_RETURN and nameAsciiIndex<2:
                    nameAsciiIndex +=1
                elif event.key == pygame.K_RETURN and nameAsciiIndex == 2:
                    playerName = ''.join(chr(x) for x in nameAsciiValue)
                    print(playerName)
                    #quit() #REMEMBER TO REMOVE QUIT
                    return playerName
            elif event.type == pygame.QUIT:
                quit()