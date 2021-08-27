from bb_cwl import BB_CWL_retrieve_data
import threading
import os

# set the user's number
user_number=1
threading_array=[]
linux_clear_process_cmd = "ps -ef|grep firefox | grep -v grep | awk '{print $2}' | xargs kill -9"
# create the thread and store
for i in range(user_number):
    son_thread=threading.Thread(target=BB_CWL_retrieve_data,args=('_'+str(i),))
    threading_array.append(son_thread)

# run the multi-thread
while(True):
    if __name__=='__main__':
        for i in range(user_number):
            threading_array[i].start()
            
        for son_thread in threading_array:
            son_thread.join()
    print("======end of the main programme=======")
    # restart the programme and clear the firefox process not quitting
    print("======restart the thread===========")
    os.system(linux_clear_process_cmd)