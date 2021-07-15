import os
import time

class Path:
	def __init__(self, file_path):
		self._cache_stamp 	= 0
		self.filename 		= file_path

class Watcher(Path):
	def __init__(self, file_path):
		super().__init__(file_path)

	def watch_file(self):
		stamp = os.stat(self.filename).st_mtime
		if stamp != self._cache_stamp:
			self._cache_stamp = stamp
			print('File changed at {}'.format(time.localtime()))
			