from bb_cwl import BB_CWL_retrieve_data
import threading
# assume there are 16 people
user_number=2
threading_array=[]
if __name__=='__main__':
    # create the thread and make it as protect process
    for i in range(user_number):
        son_thread=threading.Thread(target=BB_CWL_retrieve_data,args=('_'+str(i),))
        threading_array.append(son_thread)
        threading_array[i].start()
    for son_thread in threading_array:
        son_thread.join()
print("======end of the main programme=======")