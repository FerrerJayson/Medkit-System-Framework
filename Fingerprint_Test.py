from pySerialTransfer import pySerialTransfer as txfer
import time
link = txfer.SerialTransfer('COM6', 9600) 

link.open()
print("green on")
link.send(link.tx_obj(1))
time.sleep(2)
print("fingerprint led on")
link.send(link.tx_obj(6))
time.sleep(3)
link.send(link.tx_obj(8))
while not link.available():rc=0
arr = link.rx_obj(obj_type='i')
print(arr)
while 1:
    if 
        arr = link.rx_obj(olink.available():bj_type=str,start_pos=0,obj_byte_size=5)
        print(arr)
    else:
        print("Waiting")
while not link.available():rc=0
id = link.rx_obj(obj_type='i')
print(id)
link.close()
link.open()
time.sleep(3)