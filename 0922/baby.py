for tc in range(1, int(input())+1):
    lst = list(map(int, input().split()))

    player1 = [0]*10
    player2 = [0]*10

    ocnt = 0
    tcnt = 0

    win = 0

    for i in range(0, 12, 2):

        if i <= 3:
            player1[lst[i]] += 1
            player2[lst[i+1]] += 1

        else:
            if win != 0: break

            else:
                player1[lst[i]] += 1
                for o in range(10):
                    if player1[o] == 3:
                        win = 1
                        break
                if win != 0: break

                for o in range(10):
                    if ocnt == 3:
                        win = 1
                        break
                    else:
                        if player1[o] != 0:
                            ocnt += 1
                        else:
                            ocnt = 0

                if win == 0:
                    player2[lst[i+1]] += 1

                    for t in range(10):
                        if player2[t] == 3:
                            win = 2
                            break
                    if win != 0 : break

                    for t in range(10):
                        if tcnt == 3:
                            win = 2
                            break
                        else:
                            if player2[t] != 0:
                                tcnt += 1
                            else:
                                tcnt = 0

                else: break
    print(f'#{tc} {win}')
