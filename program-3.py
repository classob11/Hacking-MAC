import subprocess

interface = input ("interface > ")
new_mac = input("nuevo MAC ")

print("[+] Cambiando direccion mac para " + interface + " a " + new_mac) 


##############  Forma 1  ##############  

#subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up", shell=True)

##############  Forma 2 ##############  

subprocess.call(["ifconfig", interface, "down"])

subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

subprocess.call(["ifconfig", interface, "up"])