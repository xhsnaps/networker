from paramiko import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("99.1.15.194", port=22, username='root',password='Cmb@2015', timeout=5, banner_timeout=0.3)
stdin,stdout,stderr=client.exec_command("cat /config/bigip_gtm.conf")

'''
connect(hostname, port=22, username=None, password=None, pkey=None, key_filename=None, 
        timeout=None, allow_agent=True, look_for_keys=True, compress=False, sock=None, 
        gss_auth=False, gss_kex=False, gss_deleg_creds=True, gss_host=None, banner_timeout=None)
Parameters:	
		hostname (str) – the server to connect to
		port (int) – the server port to connect to
		username (str) – the username to authenticate as (defaults to the current local username)
		password (str) – a password to use for authentication or for unlocking a private key
		pkey (PKey) – an optional private key to use for authentication
		key_filename (str) – the filename, or list of filenames, of optional private key(s) to try for authentication
		timeout (float) – an optional timeout (in seconds) for the TCP connect
		allow_agent (bool) – set to False to disable connecting to the SSH agent
		look_for_keys (bool) – set to False to disable searching for discoverable private key files in ~/.ssh/
		compress (bool) – set to True to turn on compression
		!!!sock (socket) – an open socket or socket-like object (such as a Channel) to use for communication to the target host
		gss_auth (bool) – True if you want to use GSS-API authentication
		gss_kex (bool) – Perform GSS-API Key Exchange and user authentication
		gss_deleg_creds (bool) – Delegate GSS-API client credentials or not
		gss_host (str) – The targets name in the kerberos database. default: hostname
		banner_timeout (float) – an optional timeout (in seconds) to wait for the SSH banner to be presented.
'''