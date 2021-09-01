import pyautogui

pyautogui.sleep(2)
ssll=pyautogui.locateOnScreen('ssll.png')
pyautogui.moveTo(ssll)
pyautogui.doubleClick(duration = 0.25)
id=pyautogui.locateOnScreen('id.png')
pyautogui.sleep(0)
id = None
pas = None
kkll = None
running = True
while running:
    try:
        on = pyautogui.getWindowsWithTitle('새')[0]
        print(on)
        on.moveTo(0, 0)
        running = False
    except IndexError:
        continue

pyautogui.sleep(1)
while id == None:
    id = pyautogui.locateOnScreen('id.png')
    pyautogui.moveTo(id)
    pyautogui.click(duration = 0.25)
    pyautogui.write('sys8364')

pyautogui.sleep(1)
while pas == None:
    pas = pyautogui.locateOnScreen('pas.png')
    pyautogui.moveTo(pas)
    pyautogui.click(duration = 0.25)
    pyautogui.write('dudtjd!121')
pyautogui.press('enter')

pyautogui.sleep(3)

while kkll == None:
    kkll = pyautogui.locateOnScreen('kkll.png')
    pyautogui.moveTo(kkll)
    pyautogui.click(duration = 0.25)

on = pyautogui.getWindowsWithTitle('새')[0]
on.activate()
on.maximize()

on = pyautogui.getWindowsWithTitle('온')[0]
on.activate()
on.maximize()

# 새올행정시스템 - Internet Explorer
# 온-나라 문서1.0/송영성/교육체육과 - Internet Explorer