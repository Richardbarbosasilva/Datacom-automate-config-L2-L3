#!/usr/bin/python3
# -*- coding: utf-8 -*-
from netmiko import ConnectHandler
import logging
logging.basicConfig(filename = "dm.log", level = logging.WARNING, format = "%(asctime)s | %(message)s")
dm = {"device_type": "cisco_ios", "host": "dm", "username": "admin", "password": "admin"}


connect = ConnectHandler(**dm)


cmd1 = connect.send_command('config', expect_string=r'#')
cmd2 = connect.send_command('load factory-config', expect_string=r'#')
cmd3 = connect.send_command('commit', expect_string=r'#')
cmd4 = connect.send_command('hostname SW-XYZ', expect_string=r'#')
cmd5 = connect.send_command('banner login "Os acessos sao monitorados, somente para pessoas autorizadas!!!\\n"', expect_string=r'#')
cmd6 = connect.send_command('clock timezone BRA -4', expect_string=r'#')
cmd7 = connect.send_command('sntp client', expect_string=r'#')
cmd8 = connect.send_command('sntp server 143.137.92.139', expect_string=r'#')
#SNMP
cmd9 = connect.send_command('no snmp community public', expect_string=r'#')
cmd10 = connect.send_command('no snmp vacm group public', expect_string=r'#')
cmd11 = connect.send_command('no snmp notify std_v1_trap', expect_string=r'#')
cmd12 = connect.send_command('no snmp notify std_v3_inform', expect_string=r'#')
cmd13 = connect.send_command('no snmp notify std_v3_trap', expect_string=r'#')
cmd14 = connect.send_command('no snmp agent version v3', expect_string=r'#')
cmd15 = connect.send_command('no snmp traps config-commit', expect_string=r'#')
cmd16 = connect.send_command('no snmp traps link-status', expect_string=r'#')
cmd17 = connect.send_command('no snmp traps login-fail', expect_string=r'#')
cmd18 = connect.send_command('no snmp traps login-success', expect_string=r'#')
cmd19 = connect.send_command('snmp agent enabled', expect_string=r'#')
cmd20 = connect.send_command('snmp system contact noc@clickip.com.br', expect_string=r'#')
cmd21 = connect.send_command('snmp system location *Manaus-AM*', expect_string=r'#')
cmd22 = connect.send_command('snmp community ClickIP sec-name ClickIP', expect_string=r'#')
cmd23 = connect.send_command('snmp vacm group ClickIP member ClickIP sec-model v2c', expect_string=r'#')
cmd24 = connect.send_command('top', expect_string=r'#')


cmdx = connect.send_command('commit', expect_string=r'#')
print(cmdx)


connect.disconnect()


#except:
#logging.warning("Erro de conexão para: " + str(dm["dm"]))