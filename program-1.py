import subprocess

#ifconfig (direccion ip de la maquina)
subprocess.call("ifconfig eth0 down", shell=True)
#cambiar la mac de la maquina
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
#se realiza el cambio
subprocess.call("ifconfig eth0 up", shell=True)





