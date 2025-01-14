#!/usr/bin/env python3
#-*-coding:utf8;-*-
#qpy:console
'''
simple http server for file sharing.
because i intend on using this with
qpython on my android, i've decided
to take input rather than parse sys-
tem arguments. other design choices
may apply.
authored by brianc2788@gmail.com
http://brianc2788.github.io/
'''
__author__ = 'brianc2788@gmail.com, http://brianc2788.github.io'
__copyright__ = 'Copyright (c) 2022, Brian Chiodo'
__license__ = 'Apache License, Version 2.0'

from sys import exit
from os import path, chdir, getcwd
import http.server
import socketserver

# Android doesn't allow binding to port numbers below 1024.
port = 8000
rhandler = http.server.SimpleHTTPRequestHandler

server = socketserver.TCPServer(
         ("", port),
         rhandler
         )

""" Get a target dir from the user. Check for valid target. """
'''
I don't much like this setup, but I really
wanted to use a python while loop. thanks.
'''
rdir = getcwd()
tdir = ''
fdir = ''

while not path.exists(fdir):
    tdir = input('Enter dir: {}'.format(rdir))
    fdir = rdir + tdir

try:
    chdir(fdir)
except BaseException:
    print('Encountered a problem. You may lack user priviledges.\nExiting...')
    exit()

""" Run the server until the user quits. """
try:
    print('Listening for HTTP requests on port {}'.format(port))
    server.serve_forever()
except BaseException:
    if KeyboardInterrupt:
        print('\nShutdown requested by user...')
        server.server_close()
        print('Server closed. Exiting...')
        exit(0)
    else:
        print('an error has occurred. exiting...')
        exit()
