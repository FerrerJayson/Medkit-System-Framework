from pySerialTransfer import pySerialTransfer as txfer

#comport
comPort="COM6"
link = txfer.SerialTransfer('COM6', 9600) #chang port number accordingly
link.open()

#Bay Light analogWrite(pin,150)
BayOne=2
BayTwo=3
BayThree=4
BayFour=5
BayFive=6
BaySix=7
BaySeven=8
BayEight=9
BayNine=10

#Bay IR sensor
BayOne_sensor="A0"
BayTwo_sensor="A1"
BayThree_sensor="A2"
BayFour_sensor="A3"
BayFive_sensor="A4"
BaySix_sensor="A5"
BaySeven_sensor="A6"
BayEight_sensor="A7"
BayNine_sensor="A8"

#time
dosep=""
time1="" 
time2=""
time3="" 
time4=""
time5="" 

#login variables
login = "admin"
pin = "1234"