# Description: This script reads data from the serial port and saves it to a CSV file.

# import python libraries
import csv
import time

# import third-party libraries
import serial
import matplotlib.pyplot as plt
import pandas as pd


# open serial port
ser = serial.Serial('/dev/cu.usbmodem114101', 9600)  # Remplacer 'COM3' par le bon port série
print('Serial port opened!')


def plot_csv_file(csv_file):
    """
    Display a graph from a CSV file
    :param csv_file: CSV file path
    :return: None
    """
    # read the CSV file
    data = pd.read_csv(csv_file)

    # plot the data
    data.plot()
    plt.show()

def save_data_from_serial_every_min():
    """open a serial port and save data to a CSV file
    every minute (60 seconds)
    :return: None
    """

    # opening the csv file
    with open('data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        print('CSV file opened!')

        # write the header of the CSV file
        csv_writer.writerow(['X', 'Y', 'Z'])

        # start time of the loop
        begin_time = time.time()

        print("saving data")
        # loop until 60 seconds
        while True:
            # end time of the loop
            end_time = time.time()
            print(end_time - begin_time)
            line = ser.readline().decode('utf-8').strip()  # read a line from the serial port and decode it
            if "Acceleration in g's" in line:  # if the header is read then ignore it
                continue
            values = line.split('\t')  # Split the line into a list of values
            if len(values) == 3:  # if the list contains 3 values then write it to the CSV file
                csv_writer.writerow(values)  # write the values to the CSV file

            # if 60 seconds have passed then break the loop
            if end_time - begin_time > 60:
                break

    # close the serial port
    ser.close()
    print('Serial port closed!')


if __name__ == '__main__':

    save_data_from_serial_every_min()
    plot_csv_file('data.csv')
