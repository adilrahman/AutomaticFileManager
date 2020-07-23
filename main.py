import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os

extentions = {"pictures" : ["jpg", "mkv","png","gif"] , "documents" : ["pdf", "docx", "ppt"],
"executable" : ["exe" , "sh", "cpp" , "py"]}

def on_create(event):
	count = 0
	flag = 0
 
	path = event.src_path
	file_name = path.split("/")[-1]
	ext = file_name.split(".")[-1]
	if ext not in extentions.values():
		print(f"extention : {ext}")
		for i in list(extentions.values()):
			if ext in i:
				flag = 1
				break
			count += 1
		if flag:
			dest = "/home/bitbyte/python-master/wt/" + str(list(extentions.keys())[count])
			print(f" file : {dest} ")
			os.system(f"mv {path} {dest}")



'''

def on_delete(event):
	print(f"{event.src_path} deleted")

def on_modified(event):
	print(f"{event.src_path} modified")

def on_moved(event):
	print(f"{event.src_path} moved to {event.dest_path}")


'''
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns,ignore_directories,case_sensitive)

    my_event_handler.on_created = on_create
    #my_event_handler.on_deleted = on_delete
    #my_event_handler.on_modified = on_modified
    #my_event_handler.on_moved = on_moved

    path = "/home/bitbyte/python-master/wt"
    go_recv = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler,path,recursive=go_recv)

    my_observer.start()
    try:
    	while True:
    		time.sleep(10)
    except 	KeyboardInterrupt:
    	my_observer.stop()
    	my_observer.join()



