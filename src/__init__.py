from paramiko_shell import paramiko_shell
from pexpect_shell import pexpect_shell

class networkers:
	def __init__(self):
		# 

	def __init__(self, ip=ipaddr):
		# 连接数据库查询对应IP的设备类型
		if network_type == paramiko_:
			self._shell = paramiko_shell(ip=ipaddr)
		elif network_type == pexpect_shell:
			self._shell = pexpect_shell(ip=ipaddr)

	def __init__(self, ip1=ipaddr1, ip2=ipaddr2):
		# 连接数据库查询

	def run(self, command='whoami'):
		return self._shell.run(command)
		