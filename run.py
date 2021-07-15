from core import watcher

def exec():
	watcher.watch_file()

if __name__ == '__main__':
	while True:
		exec()
