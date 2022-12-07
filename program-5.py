import subprocess
import optparse

def get_argument():
    
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar direccion MAC")
    parser.add_option("-m", "--mac", dest = "new_mac", help="Nueva direccion MAC")
    
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Por favor indicar una interfaz, usa --help para mas informacion")
    elif not options.new_mac :
        parser.error("[-] Por favor indicar una MAC, usa --help para mas informacion") 
    return options


def change_mac (interface, new_mac):
    
    print("[+] Cambiando direccion mac para " + interface + " a " + new_mac) 

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



options = get_argument()

change_mac(options.interface,options.new_mac)

