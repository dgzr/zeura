# Jangan Anggap Serius , Cuman Tuul Ampas Buat ngisi Kegabutan
# Mulai : Kamis, Apr 09 2020,- 16:14:44 WIB
# python3
import requests,re
from os import system

m = '\033[1;31m'
h = '\033[1;32m'
p = '\033[1;37m'
ab = '\033[1;35m'

class BuSyet:
	def __init__(self):
		self.url = 'https://www.phpencode.org/'
		self.url_2 = 'http://decode.tools/decode-zeura'
		self.menu()
	def menu(self):
		system('clear')
		print(f'          {p}[{h}   Coder : Ezz-Kun  {p}]')
		print(f'        [  {h}Zeura Encode & Decode {p} ]')
		print(f'\n{p}--{m}Main{p} --')
		print(f'{p}[{h}01{p}] ~ Encode \n[{h}02{p}] ~ Decode')
		inp = int(input(f'\n{p}[{h}*{p}] Chose : '))
		if inp == 1:
			self.enkode()
		elif inp == 2:
			self.dekode()
	def enkode(self):
		file = input(f'{p}[{h}?{p}] File For Encode : ')
		out = input(f'[{h}?{p}] File To Save : ')
		data = {"ascii":open(file).read(),"token":"submit"}
		r = requests.post(self.url,data=data).text
		result = re.search(r"<textarea.*php.*?(.*)</textarea>",r).group(1).replace('&quot;','"')
		with open(out,'w') as i:
			i.write('<?php'+result)
			i.close()
#		system('clear')
		print('_'*35)
		system(f'cat {out}')
		print('\n'+'_'*35)
		print(f'{p}[{h}*{p}] Okay Encode File {file}')
		print(f'[{h}*{p}] Output Saved As {out}')
	def dekode(self):
		file = input(f'[{h}?{p}] File To Decode : ')
		out = input(f'[{h}?{p}] File To Save : ')
		data = {"input":open(file).read(),"decode":"submit"}
		r = requests.post(self.url_2,data=data).text
		done = re.search(r'<textarea\ rows\=\"15\" cols\=\"100\">\n(.*?)<\/textarea\>',r).group(1)
		with open(out,'w') as i:
			i.write('<?php\n'+done+'\n?>')
			i.close()
#		system('clear')
		print('_'*35)
		system(f'cat {out}')
		print('\n'+'_'*35)
		print(f'{p}[{h}*{p}] Okay Decode File {file}')
		print(f'[{h}*{p}] Output Saved As {out}')

try:
	BuSyet()
except (EOFError,KeyboardInterrupt):
	pass
except ValueError:
	exit(f'{p}[{m}!{p}] Wrong :{m} Your Choice Must Be Integer')
except IOError:
	exit(f'{p}[{m}!{p}] Wrong : {m}File Not Found')
except requests.exceptions.ConnectionError:
	exit(f'{p}[{m}!{p}] Wrong :{m} No Internet Connection')
