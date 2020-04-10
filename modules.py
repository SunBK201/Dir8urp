try:
    from simhash import Simhash
except:
    print("[!] LACK OF Simhash,try 'pip install Simhash'")
try:
    import requests
except:
    print("[!] LACK OF requests,try 'pip install requests'")
try:
    from Dicts import header
except:
    print("[!] LACK OF 'Dicts.py',try to download the project again")
from colorama import Fore,Back,Style,init   #THE COLORAMA USED FOR DISPLAY COLORED NOTES
init(autoreset=True)                        #-- AUTO RESET THE COLOR OF OUTPUTS --#
from Dicts import header,Dicts_of_404_Pages_Path
from time import sleep as WAIT
import re

#-- =======================RAW DATA AERA=================================== --#
#--* Below are some raw data for extended modules to call with *--#
#-- used to USERS_SELECT --#
AVAILABLE_USER_SELECT={
    'HELP':1,
    'DB':2,
    'FUZZ':3
}
header={"headers":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
          (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
#-- $ServerReplyStatus is used for external function to call with in order to display the error reply of the Server --#
ServerReplyStatus={
    '200':'[+] 200 OK',
    '204':'[+] Server Returned status 204',
    '302':'[!] Server Returned status 302 redirect',
    '403':'[-] 403-Forbidden',
    '404':'[-] 404 Not Found',
    '405':'[-] 405 ERROR',
    '408':'[-] Request Time out',
    '500':'[-] Server ERROR 500',
    '503':'[-] Server Error 503',
    '502':'[-] Server Error 502 ',
    '400':'[-] Server returned 400'

}
LOGO={
    1:r'    ____      _           ____                        ',
    2:r'   / __ \\   (_)  ____   ( __ )   __  __   _____   ____',
    3:r'  / / / /  / /  / ___/  / __  |  / / / /  / ___/  / __ \\',
    4:r' / /_/ /  / /  / /     / /_/ /  / /_/ /  / /     / /_/ /',
    5:r'/_____/  /_/  /_/      \____/   \__,_/  /_/     / .___/ ',
    6:r'                                               /_/      '+'\n'
}

#-- =======================RAW DATA AERA=================================== --#
'''---------------------------RAW DATA AERA ENDS RIGHT HERE-----------------'''


'''#-- =====================================================================================FUNCTION AERA============================================================= --#'''


"""==================--WRITTEN BY LapterGrsd--====================-"""


#------------------COLOR_PRIMARY_DEFINE----------------------------------#
#-- THE FUNCTION TO CHANGE THE OUTPUT COLOR --#
#-- USAGE: print (Display_Color.LOGO(PRIMARY_COLOR_DEFINE,"stes")) --#
class Display_Color(object):
    def WRONG(self,s):
        return Fore.LIGHTRED_EX + s +Fore.RESET
    def SUCCESS(self,s):
        return Fore.GREEN + s +Fore.RESET
    def WARNING(self,s):
        return Fore.YELLOW + s +Fore.RESET 
    def LOGO(self,s):#-- COLOR 
        return Fore.MAGENTA+s+Fore.RESET
    def BLUE(self,s):
        return Fore.CYAN + s +Fore.RESET
    def RED(self,s):
        return Fore.LIGHTRED_EX+s+Fore.RESET
PRIMARY_COLOR_DEFINE =Display_Color()#-- THE CLASS FOR COLORED OUT PUTS --#


#---------------------main_LOGO-----------------------------------------#
#-- FUNCTION TO DISPLAY LOGO --#
def main_LOGO():
    for i in range(1,7):
        print(Display_Color.LOGO(PRIMARY_COLOR_DEFINE,LOGO[i]))

def main_LOGO_style_Green():
    for i in range(1,7):
        print(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,LOGO[i]))

def main_LOGO_style_Red():
    for i in range(1,7):
        print(Display_Color.WARNING(PRIMARY_COLOR_DEFINE,LOGO[i]))

def main_LOGO_style_Blue():
    for i in range(1,7):
        print(Display_Color.BLUE(PRIMARY_COLOR_DEFINE,LOGO[i]))

def main_LOGO_style_LightRed():
    for i in range(1,7):
        print(Display_Color.RED(PRIMARY_COLOR_DEFINE,LOGO[i]))

#--------------------get_Reply_StatusNumber-------------------------------#
#-- Function to get a returned status code and convert it to str --#
#-- ! NOTICE: FUNCTION OUT OF STYLE, MAY CAUSE ERRORS ! --#
def get_Reply_StatusNumber(replys):
    return replys[11:-2]


#-----------------------Display_Reply_Status-------------------------------#
#-- Function to Display the Returned Results --#
#-- Function takes two param,P1 as the ERROR list dict,P2 as the Reply_status of the server. --#
def Display_Reply_Status(ERROR_LIST,ReplyStatusNumber):
    try:
        print(ERROR_LIST[ReplyStatusNumber]) 
    except:#-- The Function needed to be rewrite, in order to deal the unknown error as more s possible --#
        print('Unknown error')


#------------------------------- ! MAIN IDENTIFY FUNCTION ! ----------------------------#
#-- ! MAIN FUNCTION TO CHECK EXISTING ! --#
#-- !  FUN TAKES ONE PARMA , OUT PUT FALSE OR TRUE ! --#
#-- ! TRUE = EXISTING || FALSE = 404 ! --#
def Check_Alive(url):
        try:
            print(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,"Trying to test the connection to the target "+url+"   ..."))
            result=requests.get(url,headers=header)
        except ConnectionError:
            print("ERROR! "+Display_Color.WRONG(PRIMARY_COLOR_DEFINE,ServerReplyStatus[str(result.status_code)]))
            exit(0)
        print(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,"Success!\n"))

class IDENTIFY_MAIN(object):
    def Add_Hash_Library(self,now_url):
        Check_Alive(now_url)
        P404_LIBRARY=[]
        for PATHNOW in Dicts_of_404_Pages_Path:
            TEMP_URL=str(now_url+PATHNOW)
            TEMP_PAGE=requests.get(TEMP_URL,headers=header)
            #print(TEMP_PAGE.content)
            TEMP_PAGE_TEXT=str(TEMP_PAGE.content)
            TEMP_PAGE_HASH=Simhash(TEMP_PAGE_TEXT)
            #print(TEMP_PAGE_HASH.value)
            P404_LIBRARY.append((str(TEMP_PAGE_HASH.value))[0:6])
            WAIT(0.1)
        return P404_LIBRARY
        
    def IDENTIFY_FUNCTION(self,LIST,url):
        pre_check_page=requests.get(url,headers=header)
        if pre_check_page.status_code in [404,400,403,302,301,500,502,203]:
            return pre_check_page.status_code
        else:
            PAGE_TEST=requests.get(url,headers=header)
            #print(PAGE_TEST.content)
            PAGE_HASH=Simhash(str(PAGE_TEST.content))
            PAGE_HASH_VALUE=PAGE_HASH.value
      #print(PAGE_HASH.value)
      #print(PAGE_HASH.value)
        if (str(PAGE_HASH_VALUE))[0:6] in LIST:
            return 404
        else:
            return 200
    def DISPLAY_MAIN(self,urli,boolin):
        if boolin == 200:
            print("%-90s%-50s"%(Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,urli),Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,ServerReplyStatus['200'])))
        else:
            print("%-90s%-50s"%(Display_Color.WARNING(PRIMARY_COLOR_DEFINE,urli),Display_Color.WRONG(PRIMARY_COLOR_DEFINE,ServerReplyStatus[str(boolin) ])))


def URL_DEAL_NEXT(URLINPUTS):
  return URLINPUTS[0:(URLINPUTS.rfind('/'))]#-- NOTICE STANDARD URL INPUT IS :http://admin.com or http://admin.com/1.php




#这时确定服务器有自定义404页面，所以进入identify404函数进行下一步simhash特征值的判断


'''#-=============================--- WRITTEN BY NOTHING_H -==================================-#'''
#-- main Function to convert url to standard url --#
#-- FUNCTION receive one str param,returns a standard url like "http://example.com/admin" --#
def Standard_URL_Convert(URLstr):
    if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', URLstr) != None:
        return URLstr
    elif re.match(
        '^(?=^.{3,255}$)[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$',
            URLstr) != None:
        return "http://" + URLstr
    else:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, URLstr + " is invalid !"))
        raise Exception("Invalid URL!")


#print(Standard_URL_Convert('http://jggz.jinan.cn/col/col1863/'))

#-------------------------------Standard_URL_Convert-------------------------#
'''#-=-----------------=Nothing_H !S AREA ENDS RIGHT HERE===--------------------------------==-#'''





'''#-- =============================================================== FUNCTION AERA END RIGHT HERE ============================================================= --#'''
'''
def identify_404(domain, nowdomain):
    try:
      page4041 = requests.get(domain + '/dgasgdfsdf.txt', headers=header)
    except requests.exceptions.ConnectionError:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "A connection error occured.\n Please try again later.\n"))
    except requests.exceptions.ChunkedEncodingError:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "There is something wrong! \n ChunkedEncodingError!\n"))
    except:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "Unknown Error\n Maybe you can try to install the Request Library to solve the problem.\n"))
    try:
      page4042 = requests.get(domain + '/dfag04ggg00dfw32a.xpd', headers=header)
    except requests.exceptions.ConnectionError:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "A connection error occured.\n Please try again later.\n"))
    except:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Unknown Error\n Maybe you can try to install the Request Library to solve the problem.\n"))
    try:
      pagenow = requests.get(nowdomain, headers=header)
    except requests.exceptions.ConnectionError:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "A connection error occured.\n Please try again later.\n"))
    except:
      print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE, "Unknown Error\n Maybe you can try to install the Request Library to solve the problem.\n"))
    debugcode = [403, 405, 500, 503, 302, 301]
    if pagenow.status_code == 404:
        return False
    if pagenow.status_code in debugcode:
        print(Display_Color.WARNING(PRIMARY_COLOR_DEFINE,ServerReplyStatus[str(pagenow.status_code)]))
    try:
        hash_page4041 = Simhash(str(page4041.content))
    except:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Unknown Error\n Maybe you can try to install the Simhash Library to solve the problem.\n"))
    try:
        hash_page4042 = Simhash(str(page4042.content))
    except:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Unknown Error\n Maybe you can try to install the Simhash Library to solve the problem.\n"))
    try:
        hash_pagenow = Simhash(str(pagenow.content))
    except:
        print(Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"Unknown Error\n Maybe you can try to install the Simhash Library to solve the problem.\n"))
    if hash_page4041.distance(hash_page4042) != 0:  # Check whether 404 has different echos
        print(Display_Color.WARNING(PRIMARY_COLOR_DEFINE,"[!] Maybe different returns,check yourself: " + nowdomain))
    else:
        if hash_pagenow.distance(hash_page4041) < 3:
            return False
        else:
            return True
print(identify_404("https://www.csdn.net/1111111111","https://www.csdn.net"))

    '''

"""----------------sECOND EDITED BY alazymechnaic------------------------------"""
"""-----------------LAPTER GRSD!S AEERA ENDS RIGHT HERE------------------"""





#-- BELOW ARE FUNCTIONS UNUSED --#
"""
def precheck(inputs):
    if inputs[0:5] == "http:":
        if inputs[:-1]!='/':
            return inputs
        else:
            inputs[:-1]=''
            return inputs
    else:
        return "http://"+inputs
"""

"""
test1=requests.get('http://www.baidu.com/dgagasgf.txt')
test2=requests.get('http://www.baidu.com/')
print(test1.content)
a=Simhash(str(test1.content))
b=Simhash(str(test2.content))
print(a.distance(b))
"""
"""
class id_404:
    def __init__(self,domain):
        self._page404=[]
        self._url404=[]
        self._path404=["gawrgfsdfwagrsdfgwwwasdfvv"]
        self._rcode404=[200,302,301]
        for 404path in self._path404:
            for 404path in self._path404:
                if domain[-1]=='/':
                    url=domain+404path
                else:
                    url=domain+'/'+ 404path
                response=requests.get(url)
                if response.status_code in self._rcode404:
                    self.check_next(response.content,url)
    
    def check_next(self, _page404, _url404):
        if _page404 not in self._page404:
            self._page404.append(_page404)
        if _url404 not in self._url404:
            self._url404.append(_url404)
    
    def judegesim(self, page_1,page_2):
        page_1_hash=Simhash(page_1)
        page_2_hash=Simhash(page_2)
        sim=page_1_hash.distance(page_2_hash)
        if sim > 3:
            return True
        else:
            return False
    def is404(self,url):
        if url in self
"""
