import pyautogui as ghost
import time

while True:
    time.sleep(5)
    for i in range(100):
        
        ghost.keyUp('Space')
        ghost.keyDown('Space')
        
        time.sleep(1)
        
        for k in range(2):
            ghost.keyDown('Left')
            time.sleep(0.03)
            ghost.keyUp('Left')
            time.sleep(0.03)

        
        
    # for i in range(100):
    #     print(i)
    #     ghost.mouseDown(574, 715)
    #     ghost.mouseUp()
        
    #     ghost.mouseDown(787, 248)
    #     ghost.mouseUp()
        
    #     ghost.mouseDown(420, 717)
    #     ghost.mouseUp()
        
    #     for i in range(4):
    #         ghost.mouseDown(787, 248)
    #         ghost.mouseUp()
        
    #     # time.sleep(1)
    #     time.sleep(0.5)
    #     ghost.keyDown('W')
    #     time.sleep(0.03)
    #     ghost.keyUp('W')
    #     time.sleep(0.5)