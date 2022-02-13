from interfaces import ScaleInterface  # why this error tho? :(
import serial
import time


class Scale(ScaleInterface):
    def __init__(self) -> None:
        baudrate = 57600
        self.ser = serial.Serial('COM6', baudrate)
        time.sleep(2)

    def measure(self) -> float:  # read and record data
        data = []
        for i in range(50):
            b = self.ser.readline()  # read a byte string
            string = b.decode().rstrip()  # decode byte string into Unicode, remove \n and \r
            if string == 'Send \'t\' from serial monitor to set the tare offset.':
                print('Remove all weight from the scale, measurement in 3 seconds!')
                time.sleep(3)
                self.ser.write(b't')
            elif string == 'Then send the weight of this mass (i.e. 100.0) from serial monitor.':
                print('Place a weight of 164g to calibrate. Measurement in 5 seconds!')
                time.sleep(5)
                self.ser.write(b'164.0')
            elif string == 'Save this value to EEPROM adress 0? y/n!':
                self.ser.write(b'y')
                time.sleep(1)
            else:
                try:
                    flt = float(string)
                    print(flt)
                    data.append(flt)  # add to the end of data list
                except ValueError:
                    print('Not a float', string)
                time.sleep(0.1)  # wait
        self.ser.close()

        # show the data
        for line in data:
            print(line)


if __name__ == '__main__':
    scale = Scale()
    weight = scale.measure()
    print(weight)
