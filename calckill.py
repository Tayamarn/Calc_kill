import subprocess

def IsProcessRunning(processName):
	ps = subprocess.Popen(r'tasklist.exe /NH /FI "IMAGENAME eq %s"' % (processName), shell=True, stdout=subprocess.PIPE)
	output = ps.stdout.read()
	ps.stdout.close()
	ps.wait()
	#print(output)
	if processName in output:
		return True
	return False
	
def KillProcess(processName):
	ps = subprocess.Popen(r'taskkill /fi "IMAGENAME eq %s"' % (processName), shell=True, stdout=subprocess.PIPE)
	output = ps.stdout.read()
	ps.stdout.close()
	ps.wait()

	
if IsProcessRunning('calc.exe'):
	KillProcess('calc.exe')
