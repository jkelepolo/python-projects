from UI import *

import pyautogui as ghost
import _thread as thread

import time
import datetime

import pyperclip

macro_running = False

isLooping = True

conditions = ["IF", "TestClip", "Repeat"]

Actions = {
    
    "KeyPress": "KeyPress KEY",
    
    "KeyDown": "KeyDown KEY",
    
    "KeyUp": "KeyUp KEY",
    
    "Type": "Type STRING INTERVAL",
    
    "MousePress": "MousePress X Y",
    
    "MouseDown": "MouseDown",
    
    "MouseUp": "MouseUp",
    
    "MouseMove": "MouseMove X Y Seconds",
    
    
    
    "SetClip": "SetClip VALUE",
    
    "PasteClip": "PasteClip",
    
    "TypeClip": "TypeClip INTERVAL",
    
    "TestClip": "TestClip IS/NOT VALUE",
    
    
    
    "Wait": "Wait Seconds",
    
    "Repeat": "Repeat NUMBER (Set to 0 for endless)",
    
    "Break": "Break",
    
    
    
    "Eval": "Eval VALUE_1 OPERATION VALUE_2",
    
    "IF": "IF VALUE_1 IS/NOT VALUE_2",
    
    "END": "END INDEX",
    
    "Var": "Var NAME INT/FLOAT/STRING VALUE",
    
    
    }





def writeInstructions(Action):
    
    if Action == "Clear":
        ui.textEdit.clear()
        return
    

    if Action in conditions:
        ui.textEdit.textCursor().insertText("\n"+Actions[Action]+" "+ str(len(ui.textEdit.toPlainText().split('\n'))))
    else:
        ui.textEdit.textCursor().insertText("\n" + Actions[Action])
    ui.textEdit.textCursor().insertText("\n")



def Run(block=[], nested = False):
    
    
    global macro_running
    script = []
    
    if nested:
        script = block
    else:
        script = ui.textEdit.toPlainText().split('\n')
    
    waitTime = 0
    
    lastSuccesfulArg = ""
    currentArg = ""
    
    ignore_list = []
    
    # Remove empty spaces in script
    for item in script:
        if item == '':
            script.remove(item)
            
    
    # Run Macro
    
    for item in range(len(script)):
        
        if macro_running == False:
            break
        
        
        arg = script[item].split(' ')
        print(arg)
        currentArg = arg
        
    # try:
            
        if arg[0] == "Wait":
            waitTime = time.time() + float(arg[1])
            
            while time.time() < waitTime:
                if macro_running == False:
                    break
        
        elif arg[0] == "KeyPress":
            ghost.press(arg[1])
            
        elif arg[0] == "KeyDown":
            ghost.keyDown(arg[1])
            
        elif arg[0] == "KeyUp":
            ghost.keyUp(arg[1])
        
        elif arg[0] == "Type":
            ghost.write(arg[1], interval=float(arg[2]))
        
        elif arg[0] == "MousePress":
            ghost.click(int(arg[1]), int(arg[2]))
            
        elif arg[0] == "MouseDown":
            ghost.mouseDown()
        
        elif arg[0] == "MouseUp":
            ghost.mouseUp()
        
        elif arg[0] == "MouseMove":
            ghost.moveTo(int(arg[1]), int(arg[2]), float(arg[3]))
        
        elif arg[0] == "SetClip":
            pyperclip.copy(str(arg[1]))
        
        elif arg[0] == "PasteClip":
            ghost.hotkey('ctrl', 'v')
        
        elif arg[0] == "TypeClip":
            ghost.write(str(pyperclip.paste()), interval=float(arg[1]))
        
        elif arg[0] == "TestClip":
            
            
            if arg[1] == "IS":
              
                if evaluate(arg[2], str(pyperclip.paste())):
                    print("IS")
                    print(returnNextBlock(script, item))
                
            elif arg[1] == "NOT":
                if not evaluate(arg[2], str(pyperclip.paste())):
                    print("NOT")
                    print(returnNextBlock(script, item))
        
        
        
        
        lastSuccesfulArg = str(arg)
        
    # except:
    #     print("FAIL")
    #     print("Last successful argument: " + lastSuccesfulArg)
    #     print("Failed argument: " + str(currentArg))
    #     print("Correct Syntax: " + Actions[currentArg[0]])
    #     break
    
    stop_macro()
    return
        
def start_macro():
    global macro_running
    ui.Run.setEnabled(False)
    ui.Clear.setEnabled(False)
    ui.textEdit.setEnabled(False)
    macro_running = True
    thread.start_new_thread(Run,())


def stop_macro():
    global macro_running
    ui.Run.setEnabled(True)
    ui.Clear.setEnabled(True)
    ui.textEdit.setEnabled(True)
    macro_running = False

def stop_all():
    global isLooping
    isLooping = False
    stop_macro()
    
def MainLoop():
    return



def Initialize():
    thread.start_new_thread(MainLoop, ())


def evaluate(a,b):
    if a == b:
        return True
    else:
        return False

def returnNextBlock(script, current_index):
    block = []
    ends = 0
    for item in range(current_index, len(script)):
        arg = script[item].split(' ')
        
        if arg[0] == "END":
            ends -= 1
        
        if arg[0] in conditions:
            ends += 1
        
        elif arg[0] == "END" and ends <= 0:
            print("Returned")
            return block
        
        block.append(script[item])
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.setWindowTitle('Ghost Macro')
    
    Initialize()
    
    # Connections
    
    MainWindow.destroyed.connect(stop_all)
    
    
    
    # Buttons #
    
    # Editor Buttons
    ui.Clear.pressed.connect(lambda: writeInstructions("Clear"))
    ui.Run.pressed.connect(start_macro)
    ui.Stop.pressed.connect(stop_macro)
    
    # Input Buttons
    ui.KeyPress.pressed.connect(lambda: writeInstructions("KeyPress"))
    ui.KeyDown.pressed.connect(lambda: writeInstructions("KeyDown"))
    ui.KeyUp.pressed.connect(lambda: writeInstructions("KeyUp"))
    ui.TypeEvent.pressed.connect(lambda: writeInstructions("Type"))
    ui.MousePress.pressed.connect(lambda: writeInstructions("MousePress"))
    ui.MouseDown.pressed.connect(lambda: writeInstructions("MouseDown"))
    ui.MouseUp.pressed.connect(lambda: writeInstructions("MouseUp"))
    ui.MouseMove.pressed.connect(lambda: writeInstructions("MouseMove"))
    
    # ClipBoard Buttons
    ui.SetClipBoard.pressed.connect(lambda: writeInstructions("SetClip"))
    ui.PasteClipBoard.pressed.connect(lambda: writeInstructions("PasteClip"))
    ui.TypeClipBoard.pressed.connect(lambda: writeInstructions("TypeClip"))
    ui.TestClipBoard.pressed.connect(lambda: writeInstructions("TestClip"))
    
    # Special
    ui.Wait.pressed.connect(lambda: writeInstructions("Wait"))
    ui.Repeat.pressed.connect(lambda: writeInstructions("Repeat"))
    ui.Break.pressed.connect(lambda: writeInstructions("Break"))
    
    # Conditionals
    ui.Evaluate.pressed.connect(lambda: writeInstructions("Eval"))
    ui.IF.pressed.connect(lambda: writeInstructions("IF"))
    ui.END.pressed.connect(lambda: writeInstructions("END"))
    ui.Var.pressed.connect(lambda: writeInstructions("Var"))
    
    MainWindow.show()
    sys.exit(app.exec_())

