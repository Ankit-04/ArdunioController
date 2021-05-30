from serial import Serial
from pynput.keyboard import Key, Controller

keyboard = Controller()
ard = Serial('COM3',9600)

while True:
    data = ard.readline()
    data = data.decode()
    print(data)
    if data[0] == '0':
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif data[1] == '0':
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    elif data[2] == '0':
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    elif data[3] == '0':
        keyboard.press(Key.right)
        keyboard.release(Key.right)
