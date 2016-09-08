#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TopsecConnection:
	def __init__(self, ipaddr, user, passwd, port=22, prompt="%"):

	def __enter__(self):
        try:
            self.child = pexpect.spawn('ssh -p %s %s@%s' % (self.port, self.user, self.manageIP), timeout=login_timeout)
            self.child.expect('password:')
            self.child.sendline(self.passwd)
            self.child.expect(self.prompt)
            self.screenLog += self.child.before + self.child.after
            return True
        except:
            return False

	def __exit__(self, exc_ty, exc_val, tb):
		pass





class TopsecShell:
	def __init__(self, address):
		self._conn = topsecConnection(address=address)

	def run(self, command=command):
		with self._conn as conn:
			pass


			