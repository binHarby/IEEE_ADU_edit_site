#!/bin/python
from bs4 import BeautifulSoup as bs
import re
with open('test.html','r+') as html_file:
	content = html_file.read()
	print(content)
	soup=bs(content,'lxml')
	print('this is another print of the file: \n')
	print(soup.prettify())

old_text=soup.find('p', {'id':'para'})

print(old_text)
new_text=old_text.find(text=True).replace_with('Abdulla  yes this is me')
old_image=soup.find('img',{'id':'img1'})
print()
print()
print(old_image)
new_image=old_image['src']='hahaha'

print(soup.prettify())
with open('test.html', 'wb') as f_output:

   f_output.write(soup.prettify('utf-8'))
