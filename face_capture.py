import pyautogui as py
import time


def capturer():
    name = input('Enter the name of the person here ')

    py.hotkey('ctrl', 'alt', 't')
    time.sleep(2)
    py.write('cd PycharmProjects')
    py.press('enter')
    py.write('cd OpenCV_Studies')
    py.press('enter')
    py.write('cd Images')
    py.press('enter')
    py.write(f'mkdir {name}')
    py.press('enter')


capturer()
