
import subprocess

print('WELCOME TO MAC CHANGER V 1.0.0 FROM BETA LABS..')
print('')

interface=input('Enter the interface (eth0,wlan0,wlan1.....):  ')
print('')
fake_MAC=input('Enter fake MAC id that you want to assign(XX:XX:XX:XX:XX:XX): ')

print('current MAC id is : ')
subprocess.call("ifconfig "+interface,shell=True)
print('')

subprocess.call("ifconfig "+interface+" down",shell=True)

subprocess.call("ifconfig "+interface+" hw ether "+fake_MAC,shell=True)

subprocess.call("ifconfig "+interface+" up",shell=True)

print('NEW MAC ADDRESS is '+fake_MAC)

print('')
subprocess.call("ifconfig "+interface,shell=True)
