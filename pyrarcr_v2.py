import time,os,sys,shutil,itertools
import threading

THREAD_COUNT = 2

name=os.path.basename(__file__)

for which in ["unrar","p7zip"]:
    if not shutil.which(which):
        print("ERROR:",which,"isn't installed.\nExiting...")
        sys.exit(-1)

# *.rar
def try_pass_unrar(file, key):
    kf=os.popen("unrar t -y -p%s %s 2>&1|grep 'All OK'"%(key, file))
    for rkf in kf.readlines():
        if rkf=="All OK\n":
            return 1
    return 0

# *.zip or *.7z
def try_pass_7za(file, key):
    kf=os.popen("7za t -p%s %s 2>&1|grep 'Everything is Ok'"%(key, file))
    for rkf in kf.readlines():
        if rkf=="Everything is Ok\n":
            return 1
    return 0

def thread_body(id, file, regex_format):
    for i in range():
        password = run_regex(regex_format, i)
        r = try_pass_unrar(file, password)
        if r:
            break
    print("ID:", id, ": DONE!")

def thread_scheduler(file, regex_format):
    threadsList = []
    
    for i in range(THREAD_COUNT):
        thread = threading.Thread(target=thread_body, args=(i, file, regex_format))
        thread.daemon = True
        thread.start()

        threadsList.append(thread)

    # threadleri kontrol et biri bitince diğerlerini 
    # öldür.

#checking if the file exists/running the function
thread_scheduler("example.rar", "CNN")

"""
if len(sys.argv)==2:
    file_name = sys.argv[1]
    if os.path.exists(file_name):
        thread_scheduler(file_name)
    else:
         print("ERROR: File doesn't exist.\nExiting...")
else:
    print("Usage:",name,"[rar file]")
    print("Example:",name,"foobar.rar")
"""
