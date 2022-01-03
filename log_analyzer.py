import os
class LogAnalyzer():
	def __init__(self, path, file):
		self._path = path
		self.file = file
		self.serv_data= []
	@staticmethod
	def get_ping_status(serv_ip):
		response = os.system("ping -c 1 " +serv_ip)
		return 'Reachable' if response == 0 else 'Not Reachable'

	def log_analysis(self):
		filename = self.file#'debuglog.log'
		file_path = self._path
		file = os.path.join(file_path, filename)
		with open(file) as log_data:
			data = log_data.readlines()
			serv_data= [(i.split(':')[0], i.split(':')[1].split(' ')[0]) for i in data]
		self.serv_data = serv_data
		return self.serv_data


if __name__ == '__main__':
	a = LogAnalyzer('.', 'debuglog.log')
	serv_data= list(a.log_analysis())
	unique_servers = list(set(serv_data))
	print('Unique Servers: \n')
	for (name, ip) in unique_servers:
		l_count = serv_data.count((name, ip))
		print(name+': '+ip+' (repeated '+str(l_count)+') is '+ a.get_ping_status(ip))
