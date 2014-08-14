#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#The MIT License (MIT)
#
#Copyright (c) 2014 Bart Grzybicki <bart@lowcaburz.tk>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import SOAPpy

api_key = 'klucz można uzyskać na stronie http://burze.dzis.net'
wsdl_file = 'https://burze.dzis.net/soap.php?WSDL'
city = 'Przywidz'

server = SOAPpy.SOAPProxy(wsdl_file)
auth = server.KeyAPI(api_key)

print('*** SzukajBurzy 0.1 Prototyp ***\n')
print('auth=' + str(auth))
hd = SOAPpy.Types.headerType()
hd.KeyAPI = {'KeyAPI': api_key}
server = server._hd(hd)
miejscowosc = server.miejscowosc(city)

coords_y = str(miejscowosc['y'])
coords_x = str(miejscowosc['x'])

print(u'współrzędne miasta ' + city + ': ' + str(coords_y) + ', ' + str(coords_x))

ostrzezenia = server.ostrzezenia_pogodowe(coords_y, coords_x)
mroz = str(ostrzezenia['mroz'])
upal = str(ostrzezenia['upal'])
wiatr = str(ostrzezenia['wiatr'])
opad = str(ostrzezenia['opad'])
burza = str(ostrzezenia['burza'])
tornado = str(ostrzezenia['traba'])

print(u'\nostrzeżenia pogodowe:')
print(u'mróz=' + mroz)
print(u'upał=' + upal)
print(u'wiatr=' + wiatr)
print(u'burza=' + opad)
print(u'mróz=' + burza)
print(u'tornado=' + tornado)

burza = server.szukaj_burzy(coords_y, coords_x)
print burza
