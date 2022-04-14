import os
import subprocess


def snmp_writer(oid: str = '.'):
    filename = '{0}.txt'.format(oid)
    os.system(f'touch {filename}')
    result = subprocess.getoutput('snmpwalk -v 2c -c sirius 192.168.254.18 {0}'.format(oid))
    with open(filename, 'w') as file:
        file.writelines(result)
    return 'ok'


snmp_writer()
