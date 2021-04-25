import pyautogui as py
import time

count = 5


def capturer():
    global count
    count += 1

    py.hotkey('ctrl', 'alt', 't')
    time.sleep(2)
    py.write('cd PycharmProjects')
    py.press('enter')
    py.write('cd OpenCV_Studies')
    py.press('enter')
    py.write('cd Images')
    py.press('enter')
    py.write(f'mkdir {count}')
    py.press('enter')


capturer()
