from interfaces import ScaleInterface  # why this error tho? :(
import serial
import time


class Scale(ScaleInterface):
    def __init__(self) -> None:
        self.serial_port = 57600

    def measure(self) -> float:
        # set up the serial line
        ser = serial.Serial('COM4', self.serial_port)
        time.sleep(2)

        # read and record the data
        data = []
        for i in range(50):
            b = ser.readline()  # read a byte string
            string_n = b.decode()  # decode byte string into Unicode
            string = string_n.rstrip()  # remove \n and \r
            flt = float(string)
            print(flt)
            data.append(flt)  # add to the end of data list
            time.sleep(0.1)  # wait
        ser.close()

        # show the data
        for line in data:
            print(line)


if __name__ == '__main__':
    scale = Scale()
    weight = scale.measure()
    print(weight)
