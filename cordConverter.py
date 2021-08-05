
# 여기서 하고 싶은 것은
# 정리가 안된 좌표들(cord)을 dxfHander에서 처리할 수 있게 변환하는 것이다
# 정리가 안된 좌표들을 순서에 맞게 재배열하고
# 벽, 기둥, 창문, 문 등 각각의 layer에 맞게 분류하는 것이다

# 아직 dictionary가 정해진 것이 없기 때문에 리스트나 다중리스트로 구현할 예정
# 나중에 사용할 때에도 리스트로 변환만 하면 사용할 수 있도록 개발하도록 하자    

        

def rectangle2cords(leftBot: tuple, rightTop: tuple) -> list:
    leftTop = (leftBot[0], rightTop[1])
    rightBot = (rightTop[0], leftBot[1])
    cords = [leftBot, leftTop, rightTop, rightBot, leftBot]
    return cords

def isPointBetween(start: tuple, end: tuple, target: tuple) -> bool:
    # 세 점이 연속성을 가지기 위해서는 
    # (t-s)(e-t)가 음수값이 나오면 안됨
    if (target[0]-start[0])*(end[0]-target[0]) < 0: return False
    if (target[1]-start[1])*(end[1]-target[1]) < 0: return False
    return True

def isPointOnStraight(start: tuple, end: tuple, target: tuple) -> bool:
    # 직선의 방정식, le가 0이어야만 같은 직선 안에 있는 것
    le = (start[1]-end[1])*target[0] + (end[0]-start[0])*target[1] + start[0]*end[1] - start[1]*end[0]
    if le == 0: return True
    return False

def isPointOnLine(start: tuple, end: tuple, target: tuple) -> bool:
    # 직선 위에 점이 없으면 False 값 return
    if isPointOnStraight(start, end, target) == False: return False
    # start와 end 사이에 target이 있어야 선분 위에 점이 있는 것
    return isPointBetween(start, end, target)

def getDistance(pointA: tuple, pointB: tuple) -> float:
    return getDistanceByPoints(pointA[0], pointA[1], pointB[0], pointB[1] )

def getDistanceByPoints(X1, Y1, X2, Y2) -> float:
    return ((X1-X2)**2 + (Y1-Y2)**2)**0.5

def getClosePoint(standard: tuple, pointA: tuple, pointB: tuple) -> tuple:
    if getDistance(standard, pointA) < getDistance(standard, pointB):
        return pointA
    return pointB

def getContainedPoint(cordsList: list, point: tuple) -> tuple:
    # cordsList가 가지고 있는 선분들 중에서 point 좌표를 포함하는 좌표를 찾는다
    # 좌표의 인덱스 값을 튜플로 리턴한다
    for cords in cordsList:
        for i in range(0, len(cords)-1):
            if isPointOnLine(cords[i], cords[i+1], point):
                return (cordsList.index(cords), i)
    return None

def swap(a: list):
    temp = a[0]
    a[0] = a[1]
    a[1] = temp




def severCords(cordsList: list, blankCords: list) -> list:
    # 좌하단부터 반시계방향으로 0(좌하)-1(우하)-2(우상)-3(좌상)
    # 1. 일단 blankCords 0이 속한 선분부터 찾아
    # 2. 선분에 속한 점이 1인지 3인지 찾아
    # 3. 만약에 속한 점이 1이면, (0->3, 2->1)
    # 4. 3가 속하는 선분을 찾아서 3에서의 거리가 3에서의 거리보다 짧은 친구를 방향으로 점을 추가하면서 가
    # 5. 0이 나올 때까지 or 2이 나올 때까지 반복


    resultList = []
    # cordsList는 이중 리스트 -> [[(),(),()],[(),()]]
    # blankCords는 [(0),(1),(2),(3),(0)]
    
    # blankCords[0] 이 속하는 선분을 찾아
    LBidx = getContainedPoint(cordsList, blankCords[0])
    RTidx = getContainedPoint(cordsList, blankCords[2])

    lineLB = [cordsList[LBidx[0]][LBidx[1]], cordsList[LBidx[0]][LBidx[1]+1]]
    lineRT = [cordsList[RTidx[0]][RTidx[1]], cordsList[RTidx[0]][RTidx[1]+1]]

    if isPointOnLine(cordsList[LBidx[0]][LBidx[1]],cordsList[LBidx[0]][LBidx[1]+1], blankCords[1]):
        # 0->3 , 2->1 케이스
        if getClosePoint(lineLB[0], blankCords[0], blankCords[3]) == blankCords[3]:
            swap(lineLB)
        if getClosePoint(lineRT[0], blankCords[2], blankCords[1]) == blankCords[1]:
            swap(lineRT)
            
        LBto = blankCords[3]
        RTto = blankCords[1]
    else:
        # 0->1, 2->3 케이스
        if getClosePoint(lineLB[0], blankCords[0], blankCords[1]) == blankCords[1]:
            swap(lineLB)
        if getClosePoint(lineRT[0], blankCords[2], blankCords[3]) == blankCords[3]:
            swap(lineRT)
            
        LBto = blankCords[1]
        RTto = blankCords[3]


    resultList.append([lineLB[0], blankCords[0], LBto, lineRT[1]])
    resultList.append([lineRT[0], blankCords[2], RTto, lineLB[1]])

    if lineRT[0] == cordsList[RTidx[0]][RTidx[1]]: 
        dir = 1
        idx = RTidx[1] + 2
    else: 
        dir = -1
        idx = RTidx[1] - 1
    m = len(cordsList[RTidx[0]])-1
    while True:
        # 리스트의 마지막이 처음과 같거나 대척점과 같다면 루프문 탈출
        if resultList[0][len(resultList[0])-1] == resultList[0][0]: break
        if resultList[0][len(resultList[0])-1] == blankCords[2]: break

        resultList[0].append(cordsList[RTidx[0]][idx%m])
        idx = idx + dir

    if lineLB[0] == cordsList[LBidx[0]][LBidx[1]]: 
        dir = 1
        idx = LBidx[1] + 2
    else: 
        dir = -1
        idx = LBidx[1] - 1
    m = len(cordsList[LBidx[0]])-1
    while True:
        # 리스트의 마지막이 처음과 같거나 대척점과 같다면 루프문 탈출
        if resultList[1][len(resultList[1])-1] == resultList[1][0]: break
        if resultList[1][len(resultList[1])-1] == blankCords[0]: break

        resultList[1].append(cordsList[LBidx[0]][idx%m])
        idx = idx + dir

    if resultList[0][len(resultList[0])-1] == resultList[1][0]:
        resultList[0].pop()
        resultList[0].append(resultList[1])
        resultList.pop()
    
    return resultList


# ------ for test ------------------------------------------------------------
def printError(errorCode: int):
    print("Error: {0}" .format(errorCode))

def testFunctions():
    # if isPointBetween((0,0), (10,10), (5,5)) == False:
    #     print("Error 1")
    
    if isPointOnLine((0,0), (10,10), (5,5)) == False:
        printError(1)

    if isPointOnLine((0,0), (10,10), (4,5)) == True:
        printError(2)

    if getDistance((0,0), (10,0)) != 10:
        printError(3)



# ------ end function definitions ------------------------------------------------------------
room = [[(0,0), (1000,0), (1000,1000), (800,1000), (800,200), (0,200), (0,0)]]
blank = [(200,0), (400,0), (400, 200), (200, 200), (200,0)]

result = severCords(room, blank)
print(result)