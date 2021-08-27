from bb_cwl import BB_CWL_retrieve_data
import threading
import os
import time

# set the user's number
user_number=1
threading_array=[]
linux_clear_process_cmd = "ps -ef|grep firefox | grep -v grep | awk '{print $2}' | xargs kill -9"

# create the thread and store these threads
for i in range(user_number):
    son_thread=threading.Thread(target=BB_CWL_retrieve_data,args=('_'+str(i),))
    threading_array.append(son_thread)

# run the multi-thread
if __name__=='__main__':
    for i in range(user_number):
        threading_array[i].start()
    
    # check and restart the threads if required.
    while(True):
        for i in range(user_number):
            if not threading_array[i].is_alive():
                print("======restart the thread_"+str(i)+"===========")
                threading_array[i] = threading.Thread(target=BB_CWL_retrieve_data,args=('_'+str(i),))
                threading_array[i].start()
        
        # check every half an hour
        time.sleep(1800)
    
    print("======end of the main programme=======")
    #clear the firefox process not quitting
    os.system(linux_clear_process_cmd)