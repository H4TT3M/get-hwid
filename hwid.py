import os
import subprocess
import time

banner = r"""


      o                                o            o  
     <|>                             _<|>_         <|> 
     / >                                           < \ 
     \o__ __o     o              o     o      o__ __o/ 
      |     v\   <|>   by: HRTZ   <|>   <|>    /v     |  
     / \     <\  < >            < >   / \   />     / \ 
     \o/     o/   \o    o/\o    o/    \o/   \      \o/ 
      |     <|     v\  /v  v\  /v      |     o      |  
     / \    / \     <\/>    <\/>      / \    <\__  / \ 
                                                   

"""

def main():
    print(banner)
    if not os.name == "nt":
        print("This program only works on Windows.")
        time.sleep(3)
        exit()
    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    print(f"Your hwid is {hwid}.")
    print("Copied to your clipboard ;)")
    os.system('echo ' + hwid + '| clip')
    print(' ')
    os.system("pause")

if __name__ == "__main__":
    main()
