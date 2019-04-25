# spawn()
# ㄴ Starts the interaction/automation of a 'child' process
#
# expect()
# ㄴ Used to tell Python/Pexpect what the remote node is going to 'say' to us
#
# sendline()
# ㄴ Allows us to send commands to the remote node
#
# interact()
# ㄴ  Allows us to 'interact' with the remote node just like we are on the command line!
#

__version__ = 1.0

import pexpect
from os import system

def main():
    """
    This is the main() function that will invoke the other functions when this module is run
    as a script. If not being run as a script, the main() function will never be called.
    """
    system(' ')
    print()
    network = input('Please enter the prefix on which you would like information from:')
    child = pexpect.spawn(network, timeout = 300)

    child.sendline('\n')
    child.expect(['Username:', pexpect.TIMEOUT])
    child.sendline('rviews')
    child.expect(['route-views>'])
    child.sendline('term length 0')
    child.expect(['route-views>'])
    child.sendline('sh ip bgp' + network)
    child.expect(['route-views>'])

    bgpoutput = child.before.decode('utf-8')
    print(bgpoutput)

    child.sendline('sh version')
    child.expect(['route-veiws>'])

    version = child.before.decode('utf-8')
    print(version)


if __name__ == '__main__':
    print('Attemping to connect...')
    main()
