import sys  # 파이썬 인터프리터가 제공하는 변수/함수 제어 모듈(내장)
import pygame  # 게임 제작 지원 모듈(설치 필요)

pygame.init()  # 초기화

# 그래픽 구성요소
backGroundColor = (48, 48, 48)  # 배경화면 RGB 색상 값
stageClearSprite = pygame.image.load('image/stageClear.png')  # 스테이지 클리어 대화창
wallSprite = pygame.image.load('image/wall.png')  # 벽
boxSprite = pygame.image.load('image/box.png')  # 상자
locationSprite = pygame.image.load('image/location.png')  # 목표위치
playerUSprite = pygame.image.load('image/playerU.png')  # 플레이어 방향 위
playerDSprite = pygame.image.load('image/playerD.png')  # 플레이어 방향 아래
playerLSprite = pygame.image.load('image/playerL.png')  # 플레이어 방향 왼쪽
playerRSprite = pygame.image.load('image/playerR.png')  # 플레이어 방향 오른쪽
playerSprite = playerLSprite  # 현재 플레이어 상태

# 연산정보 구성요소
playerPositionX = 0  # 플레이어 최초 위치 X 좌표 값
playerPositionY = 0  # 플레이어 최초 위치 Y 좌표 값
blockSizeX = 60  # 오브젝트 이동 시 X 좌표 움직이는 거리 (한 칸 당 60)
blockSizeY = 60  # 오브젝트 이동 시 Y 좌표 움직이는 거리 (한 칸 당 60)
tileSizeX = 10  # X 좌표 내 칸 수
tileSizeY = 8  # Y 좌표 내 칸 수
displaySizeX = blockSizeX * tileSizeX  # 전체 화면 X 축 크기
displaySizeY = blockSizeY * tileSizeY  # 전체 화면 Y 축 크기
locationEmpty = None  # 채워지지 않은 목표위치가 있는지 여부
moveCount = 0  # 이동횟수
stageNumber = 0  # 스테이지 번호
stageMap = []  # 스테이지 정보

stageInformation = [  # 스테이지 정보 모음(다차원 배열) (0 = 공백, 1 = 벽, 2 = 목표위치, 3 = 상자, 4 = 플레이어)
    #  stageInformation[0]
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # stageInformation[0][0]
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],  # stageInformation[0][0]
        [0, 1, 1, 1, 2, 1, 1, 0, 0, 0],  # stageInformation[0][0]
        [0, 1, 2, 3, 3, 0, 1, 1, 1, 0],  # stageInformation[0][0]
        [0, 1, 1, 1, 4, 3, 3, 2, 1, 0],  # stageInformation[0][0]
        [0, 0, 0, 1, 1, 2, 1, 1, 1, 0],  # stageInformation[0][0]
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],  # stageInformation[0][0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # stageInformation[0][0]
    ],
    [
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 3, 0, 3, 2, 1, 0],
        [0, 1, 2, 0, 3, 4, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 3, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 0, 0, 0, 3, 2, 2, 1],
        [1, 2, 3, 0, 1, 1, 1, 3, 1, 1],
        [1, 3, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 4, 0, 1, 3, 1],
        [1, 1, 3, 1, 1, 1, 0, 3, 2, 1],
        [1, 2, 2, 3, 0, 0, 0, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
]


# 스테이지 연산정보 불러오기
def map_load():
    # 전역변수 함수 내에서 사용하기 위한 global 선언
    global stageMap

    # 반복문을 통해 한 줄 씩 스테이지 정보로 추가한다
    for num in range(tileSizeY):
        # 스테이지 정보 모음(stageInformation)에서 필요한 스테이지의 정보를 불러온다
        stageMap.append(stageInformation[stageNumber][num][:])


# 스테이지 제목 지정
def set_caption(caption):
    # pygame.display set_caption() 윈도우 창의 제목 변경
    pygame.display.set_caption(caption)


# 화면 그리기
def draw():
    # 전역변수 함수 내에서 사용하기 위한 global 선언
    global playerPositionX
    global playerPositionY
    global locationEmpty

    # pygame.surface fill() 지정된 RGB 값으로 화면 채우기
    displaySurface.fill(backGroundColor)

    # 해당 함수가 수행될 때에 게임의 승리조건(= 목표위치가 전부 상자로 채워짐)이 달성된 것을 기본 값으로 간주한다
    locationEmpty = True

    # 스테이지 정보에 따라 화면을 그린다
    # pygame.surface blit() 지정된 좌표에 매개변수의 이미지를 그림
    for searchX in range(tileSizeX):
        for searchY in range(tileSizeY):
            # 벽
            if 1 == stageMap[searchY][searchX]:
                displaySurface.blit(wallSprite, (searchX * blockSizeX, searchY * blockSizeY))
            # 목표위치
            elif 2 == stageMap[searchY][searchX]:
                displaySurface.blit(locationSprite, (searchX * blockSizeX, searchY * blockSizeY))
            # 상자
            elif 3 == stageMap[searchY][searchX]:
                displaySurface.blit(boxSprite, (searchX * blockSizeX, searchY * blockSizeY))
                # 이 상자를 그릴 때 현재 플레이중인 스테이지 정보(stageMap)의 상자 위치와
                # 원본인 스테이지 정보 모음(stageInformation)의 목표위치가 같지 않을 경우
                # 승리조건 미달성인 것으로 변경된다
                if 2 != stageInformation[stageNumber][searchY][searchX]:
                    locationEmpty = False
            # 플레이어 케릭터
            elif 4 == stageMap[searchY][searchX]:
                playerPositionX = searchX
                playerPositionY = searchY
                displaySurface.blit(playerSprite, (searchX * blockSizeX, searchY * blockSizeY))


pygame.init()  # 초기화
set_caption("Sokoban")  # 스테이지 제목 지정

# pygame.display set_mode() 윈도우 창 크기 및 그래픽 처리 설정
displaySurface = pygame.display.set_mode((displaySizeX, displaySizeY), 0, 32)

map_load()  # 스테이지 연산정보 불러오기

while True:  # 메인 루프
    draw()  # 화면 그리기

    # pygame.display update() 화면을 갱신
    # (해당 함수가 없을 경우 연산은 수행하나 사용자는 화면 갱신이 되지 않아 최초화면만 보게 됨)
    pygame.display.update()

    # 승리조건 달성 (locationEmpty == True 값으로 루프 진행중일 때)
    if locationEmpty:

        # 스테이지 성공 스프라이트 그린 후 갱신
        displaySurface.blit(stageClearSprite, (120, 60))
        pygame.display.update()

        # 키 조작 여부 확인용 변수
        eventInput = False

        # 키 조작 여부 확인
        while True:
            # pygame.event get() 이벤트 큐에서 이벤트를 가져옴
            for event in pygame.event.get():
                # 가져온 이벤트 종류가 키 누름(KEYDOWN)일 경우
                if event.type == pygame.KEYDOWN:
                    # 키 조작 여부 값을 참으로 변경
                    eventInput = True
            # 키 조작 여부가 참일 경우
            if eventInput:
                # 루프 중지
                break

        # 스테이지 성공에 따른 연산정보 수정
        stageNumber = stageNumber + 1
        stageMap = []
        map_load()
        moveCount = 0
        set_caption("Sokoban [Stage : %d][move : %d]" % (stageNumber + 1, moveCount))

    # pygame.event get() 이벤트 큐에서 이벤트를 가져옴
    for event in pygame.event.get():
        # 가져온 이벤트 종류가 키 누름(KEYDOWN)일 경우
        if event.type == pygame.KEYDOWN:
            # 플레이어의 현재 좌표 저장
            tempX = playerPositionX
            tempY = playerPositionY
            # 화살표 위
            if event.key == pygame.K_UP:
                # 플레이어 스프라이트 변경(위로 보고 있는 상태)
                playerSprite = playerUSprite
                # 플레이어 좌표 수정
                playerPositionY = playerPositionY - 1
            # 화살표 아래
            elif event.key == pygame.K_DOWN:
                playerSprite = playerDSprite
                playerPositionY = playerPositionY + 1
            # 화살표 왼쪽
            elif event.key == pygame.K_LEFT:
                playerSprite = playerLSprite
                playerPositionX = playerPositionX - 1
            # 화살표 오른쪽
            elif event.key == pygame.K_RIGHT:
                playerSprite = playerRSprite
                playerPositionX = playerPositionX + 1
            # R (재시도)
            elif event.key == pygame.K_r:
                moveCount = 0
                set_caption("Sokoban [Stage : %d][move : %d]" % (stageNumber + 1, moveCount))
                stageMap = []
                map_load()
                break
            # 이외 버튼일 경우 이하 코드 건너뜀
            else:
                continue

            # 충돌 판정
            # 수정된 좌표가 벽이 아닐 경우
            if 1 != stageMap[playerPositionY][playerPositionX]:
                # 수정된 좌표가 상자일 경우
                if 3 == stageMap[playerPositionY][playerPositionX]:
                    # 수정된 좌표 전진 방향의 한 칸 앞이 공백이거나 목표위치일 경우
                    if 0 == stageMap[2 * playerPositionY - tempY][2 * playerPositionX - tempX] \
                            or 2 == stageMap[2 * playerPositionY - tempY][2 * playerPositionX - tempX]:
                        # 해당 위치에 상자 생성(진행방향으로 상자를 밂 구현)
                        stageMap[2 * playerPositionY - tempY][2 * playerPositionX - tempX] = 3
                    # 수정된 좌표 전진 방향의 한 칸 앞이 공백이거나 목표위치가 아닐 경우
                    # 수정 전 저장했던 좌표로 플레이어 위치 복구
                    else:
                        playerPositionX = tempX
                        playerPositionY = tempY
                        # 이하 코드 건너뜀
                        continue
                # 수정 전 좌표가 목표위치일 경우 목표위치 생성
                if 2 == stageInformation[stageNumber][tempY][tempX]:
                    stageMap[tempY][tempX] = 2
                # 수정 전 좌표가 목표위치가 아닐 경우 공백 생성
                else:
                    stageMap[tempY][tempX] = 0

                # 모든 충돌변수 확인 후 플레이어 좌표 수정을 포함한 연산정보 수정
                stageMap[playerPositionY][playerPositionX] = 4
                moveCount = moveCount + 1
                set_caption("Sokoban [Stage : %d][move : %d]" % (stageNumber + 1, moveCount))
            # 수정된 좌표가 벽일 경우
            # 수정 전 저장했던 좌표로 플레이어 위치 복구
            else:
                playerPositionX = tempX
                playerPositionY = tempY
        # 가져온 이벤트 종류가 창 닫기(X 단추 누름)일 경우
        # 게임 종료
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
