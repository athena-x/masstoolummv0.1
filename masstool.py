import os
import re
import requests
import sys
import time
class color:
    HEADER = '\033[95m'
    onemli = '\33[35m'
    NOTICE = '\033[33m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    WARNING = '\033[93m'
    kırmızı = '\033[91m'
    END = '\033[0m'
    altıcızık = '\033[4m'
    LOGGING = '\33[34m'
banner = """
                       ___________           .__   
  /     \ _____    ______ ______ \__    ___/___   ____ |  |  
 /  \ /  \\__  \  /  ___//  ___/   |    | /  _ \ /  _ \|  |  
/    Y    \/ __ \_\___ \ \___ \    |    |(  <_> |  <_> )  |__
\____|__  (____  /____  >____  >   |____| \____/ \____/|____/
        \/     \/     \/     \/                              
"""
print(banner)
if sys.platform == 'win32':
    print('Windowsta çalışmaz !!'+color.mavi)
    exit()
sozlesme = input(" Lütfen yasal yönde kullanın tamam mı ? "+color.kırmızı)
if sozlesme == "tamam":
    print('Güzel seçim !'+color.onemli)
    tool = input("""Ne tür bi saldırı yapmak istersin

{1} Bilgi Toplamak
{2} Açık Aramak
{3} Exploit aramak

""")
    if tool == "1":
        bilgi = input("""
{1} Nmap
""")
        if bilgi == "1":
            os.system("clear")
            hedef = input(' Hedef ip at canım'+color.altıcızık)
            os.system('nmap -sS -sV'+hedef)
            if hedef == "batalyonteam.1otl.net":
                print('Ayıp değil mi yaptığın ? '+color.mavi)
        

    
