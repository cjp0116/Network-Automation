import regex
from cli import cli as cmd

myconfig = cmd('show run')
vlan_config = cmd('configure terminal; vlan 99; name MGMT; vlan 20; name HR; end')
myinterfaces = cmd('show ip int bri')

# regex compilation

gigEthernet = re.compile(/ (\w+\d+(\ / \d+\ / \d+\:\d+\.\d+ | \ / \d+\ / \d+\ / \d+ | \ / \d+\ / \d+\.\d+ | \ / \d+\.\d+ | \ / \d+\ / \d+ | \ / \d+)? | \w +\-\w +) /)
fastEthernet = re.compile(\D+)(\d +)(?:\ /)?(\d+)?(?:\.)?(\d+)?)
potential_mac = re.compile([0 - 9A - Fa - f]{2}[:-]){5}([0 - 9A - Fa - f]{2})$)


with open('/flash/upinterfaces.txt', 'w+') as f:
    for line in myinterfaces.split('\n'):
        if 'administratively' in line:
            continue
        f.write(line)

def shutdown_int():
    print(myinterfaces.split('\n'))
    x = input('Enter which interface you would like to shudown')
    cmd('configure terminal; interface '+ x,'; shutdown')

def disable_BPDU_guard():
    question = input('Do you know the interface that needs to be configured? (y or n)')
    if question == 'y':
        print(myinterfaces.split('\n'))
        interface = input('Which interface needs to be configured? ')
        cmd('interface', +interface'; spanning-tree bpdugaurd disable')

    elif question == 'n':

        ip = input("Enter the remote host IP address on the residing port that needs it's BPDU guard disabled")
        ping = cmd('ping' + ip)
        if '0% success' in ping.split('\n'):
            print('The destination host is unreachable')
        elif arp_table = cmd('show ip arp' + ip):
            if potential_mac.match(arp_table.split('\n')):
                mac_table = cmd('show mac address-table address' + potential_mac).split('\n')
                print(mac_table.split('\n'))
                if potential_mac > 1:
                print('This is a trunk port')
                elif potential_mac.match(fastEthernet):
                    cmd('interface' +fastEthernet'; spanning-tree bpduguard disable')
                elif potential_mac.match(gigEthernet):
                    cmd('interface' + gigEthernet'; spanning-tree bpduguard disable')
                else:
                    print('The interface already has BPDU guard disabled')


def ospf_enable():
    ospf_states = { 1 : 'DOWN',
            2 : 'ATTEMPT',
            3 : 'INIT',
            4 : '2WAY',
            5 : 'EXSTART',
            6 : 'EXCHANGE',
            7 : 'LOADING',
            8 : 'FULL',

    }

    print(myinterfaces.split('\n'))
    interface = input('Enter the interface you wish to configure')
    process_id = input('Enter the OSPF process ID')
    area = input('Enter the area number')
    try:
        cmd('configure terminal; interface'+interface'; ip ospf' +str(process_id),'area ',+ str(area),';')
    except:
        print('There was something wrong, exiting now')
        exit(23)

def main():
    print('Select from the choices from below, what would you like to do?')
    print('-' * 99)
    print('1. Shut down an interface')
    print('2. Disable BPDU guard on a interface')
    print('3. Enable ospf on a interface')
    print('4. Exit program')
    choice = input('Enter your choice:')
    if choice == '1':
        shutdown_int()
    elif choice == '2':
        disable_BPDU_guard()
    elif choice == '3':
        ospf_enable()
    else:
        end(99)

if __name__ == '__main__':
    main()

