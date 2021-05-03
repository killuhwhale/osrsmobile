import os
import subprocess


"""
KEYEVENTS
    adb shell input keyevent 82
Longpress
    adb shell input swipe x y x y duration
SCREENSHOT
    Save locally
        adb shell screencap -p /sdcard/screencap.png
    Save Externally
        adb exec-out screencap -p > screen.png
SWIPE
    adb shell input swipe x1 y1 x2 y2
TEXT
    adb shell input text "insert%syour%stext%shere"
TAP
    adb shell input tap 500 1450
    To find the exact X,Y position you want to Tap go to:
        Settings > Developer Options > Check the option POINTER SLOCATION
"""

def sendKeyEvent(event):
    return f"adb shell input keyevent {event}"

def longPress(x, y):
    return f"adb shell input swipe {x} {y} {x} {y} 250"

def pressEnter():
    return sendKeyEvent(66)

def screenshot(name):
    return f"adb exec-out screencap -p > {name}.png"

def swipe(x, y, x1, y1):
    return f"adb shell input swipe {x} {y} {x1} {y1} 250"

def sendEvent(ev):
    return f"adb -t 3 shell sendevent /dev/input/event3 {ev[0]} {ev[1]} {ev[2]}"

def sendText(msg):
    return f"""adb shell input text "{msg.replace(' ', '%s')}" """

def tap(x, y):
    return f"adb shell input tap {x} {y}"

def runCmd(cmd):
    try:
        subprocess.run(cmd.split(), check=True, encoding='utf-8',
                        capture_output=True).stdout
    except subprocess.CalledProcessError as e:
        print(e)


if __name__ == "__main__":
    # runCmd(sendText("Whats mobile"))
    # runCmd(pressEnter())

    # 1536 x 864
    # print(1536*1.2, 864*1.2)
    # _MAX_X = 1920
    # _MAX_Y = 1200
    # _CENTER_X = _MAX_X / 2
    # _CENTER_Y = _MAX_Y / 2
    # runCmd(tap(_CENTER_X, _CENTER_Y))

    '''
        BS_MT_POSITION_X     : value 0, min 0, max 1439, fuzz 0, flat 0, resolution 0
        ABS_MT_POSITION_Y     : value 0, min 0, max 2879, fuzz 0, flat 0, resolution 0

        EV_KEY       BTN_TOUCH            DOWN
        EV_KEY       BTN_TOOL_FINGER      DOWN
        # Where it was down at
        EV_ABS       ABS_MT_POSITION_X    00000356
        EV_ABS       ABS_MT_POSITION_Y    0000094e

        # Swipe input point
        EV_ABS       ABS_MT_POSITION_X    000004f3
        EV_ABS       ABS_MT_POSITION_Y    0000095a
        EV_ABS       ABS_MT_ORIENTATION   fakeData[ranNum]

        EV_KEY       BTN_TOUCH            UP
        EV_KEY       BTN_TOOL_FINGER      UP

    '''

    with open('pan_right.txt', "r") as f:
        for line in f:
            line = line.strip("\n")
            runCmd(sendEvent(line.split()))