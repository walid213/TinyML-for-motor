# Proprocess data from Serial

this code is used to preprocess data from serial port.

you should install the following packages:

```bash
pip install -r requirements.txt
```

after that, you should transfet the SimpleAccelerometer.ino to your arduino nano ble 33 sense.

then, you can run the code:

```bash
python serial_processing.py
```

after 60 seconds, the code will stop and save the data to a csv file.
