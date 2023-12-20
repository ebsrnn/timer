
import time 
  

def countdown(zaman): 
    
    while zaman: 
        mins, secs = divmod(zaman, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        zaman -= 1
      
    print('süre bitti') 
  
  

zaman = input("saniye gir: ") 
  

countdown(int(zaman)) 