import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar direccion MAC")

parser.add_option("-m", "--mac", dest = "new_mac", help="Nueva direccion MAC")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Cambiando direccion mac para " + interface + " a " + new_mac) 


subprocess.call(["ifconfig", interface, "down"])

subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

subprocess.call(["ifconfig", interface, "up"])

