#!/usr/bin/python3

from os import name, system, path
from requests import get
from titles import english

def action(titles,inputs):
    from Yikebox import clear, home_page, choose_lang,info_gathering, vulner_analysis, passwd_attack, web_apps, wireless_attack, exploit_tools, sniff_spoof, malware_bypass, ddos_tools, downloader_installer
    from banner import Yikebox_banner

    if inputs.upper() == "HELP":
        print(titles.help)
    elif inputs.upper() == "CHANGELOG":
        print(titles.changelog)
    elif inputs.upper() == "ABOUT":
        print(titles.about_Yikebox)
    elif inputs.upper() == "HOMEP":
        clear()
        Yikebox_banner(titles)
        home_page(titles)
    elif inputs.upper() == "LANG":
        clear()
        choose_lang(titles)
    elif inputs.upper() == "EXIT":
        print(titles.exiting)
        exit()
    elif inputs.upper() == "INFOGARTHER":
        clear()
        info_gathering(titles)
    elif inputs.upper() == "VULNER":
        clear()
        vulner_analysis(titles)
    elif inputs.upper() == "PASSWD":
        clear()
        passwd_attack(titles)
    elif inputs.upper() == "WEBAPPS":
        clear()
        web_apps(titles)
    elif inputs.upper() == "WIRELESS":
        clear()
        wireless_attack(titles)
    elif inputs.upper() == "EXPLOITER":
        clear()
        exploit_tools(titles)
    elif inputs.upper() == "SNIFFSPOOF":
        clear()
        sniff_spoof(titles)
    elif inputs.upper() == 'MALWARER':
        clear()
        malware_bypass(titles)
    elif inputs.upper() == 'DDOSER':
        clear()
        ddos_tools(titles)
    elif inputs.upper() == 'INSTALLER':
        clear()
        downloader_installer(titles)

def download(url):
    filename = url.split('/')[-1]
    with get(url, stream=True) as re:
        re.raise_for_status()
        with open(filename, 'wb') as file:
            for chunk in re.iter_content(chunk_size=8192): 
                if chunk:
                    file.write(chunk)

def the_path(titles,tool):
    try:
        paths = str(input(titles.path_folder.format(tool))).strip()
        action(titles,paths)

        if (paths.upper() == 'HELP' or paths.upper() == 'CHANGELOG' or paths.upper() == 'ABOUT'):
            the_path(titles,tool)

        elif path.exists(paths) == True:
            return paths

        else:
            print(titles.doesnt_exists)
            the_path(titles, tool)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        print(titles.invalid)
        the_path(titles,tool)


def billcipher(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python3 = str(input(titles.installed_or_not.format('Python 3.7'))).strip()
            action(titles,python3)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)
            ruby = str(input(titles.installed_or_not.format('Ruby-lang'))).strip()
            action(titles,ruby)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y' and python2[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif python3[0].upper() == 'N':
                    print(titles.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(titles.note_python3)
                    system('.\\python-3.7.3.exe')

                elif ruby[0].upper() == 'N':
                    print(titles.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(titles.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP' or python2.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    billcipher(titles)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    billcipher(titles)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT' or python2.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    billcipher(titles)

                else:
                    print(titles.invalid)
                    billcipher(titles)
   
            print("BillCipher is no longer available on github, please contact me if there is a working fork")
            
        print("BillCipher', 'NO LONGER AVAILABLE (I AM UNABLE TO FIND THE REPO OR A FORK OF IT AS IT HAS BEEN TAKEN DOWN AND NOT FORKED")

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def leaked(titles):
    print(titles.leaked_read_only)
    print(titles.readmore.format('Leaked', 'http://bit.ly/2Qy3v08'))


def devploit(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    devploit(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    devploit(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    devploit(titles)

                else:
                    print(titles.invalid)
                    devploit(titles)

            print(titles.installing.format('Devploit'))
            system("cd C:\\ && git clone https://github.com/zD4NI3LH/Devploit")
            print(titles.done.format('Devploit'))
            print(titles.note_tools.format('Devploit', 'python Devploit'))

        else:
            if path.exists('/usr/bin/pacman') == True:
                paths = the_path(titles,'Devploit')
                system("cd {} && sudo git clone https://github.com/zD4NI3LH/Devploit".format(paths))
                print(titles.done.format('Devploit'))
                print(titles.note_tools.format('Devploit', 'python2 Devploit'))

            else:
                if path.exists('/usr/bin/Devploit') == True:
                    print(titles.installed.format('Devploit'))    

                else:
                    paths = the_path(titles,'Devploit')
                    print(titles.installing.format('Devploit'))
                    system("""cd {} && sudo git clone https://github.com/zD4NI3LH/Devploit
                    cd Devploit && sudo bash install""".format(paths))
                    print(titles.done.format('Devploit'))
                    
                print(titles.note_tools2.format('Devploit','Devploit','Terminal'))

        print(titles.readmore.format('Devploit', 'http://bit.ly/2KU7BMF'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def gorecon(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
               paths = the_path(titles,'Gorecon')
               print(titles.installing.format('Gorecon'))

               if path.exists('/usr/bin/apt') == True:
                   system("sudo apt install golang-go")

               elif path.exists('/usr/bin/pacman') == True:
                   system("sudo pacman -S go")

               system("""cd {} && sudo go get "github.com/devanshbatham/gorecon"
               cd gorecon && sudo go get "github.com/gocolly/colly"
               sudo go get "github.com/fatih/color" && sudo go get "github.com/likexian/whois-go" """.format(paths))
               print(titles.done.format('Gorecon'))
               print(titles.note_tools.format('Gorecon','go run gorecon.go'))

        print(titles.readmore.format('Gorecon','http://bit.ly/2KykK2p'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def dracnmap(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Dracnmap')
                print(titles.installing.format('Dracnmap'))
                
                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install nmap")

                elif path.exists('usr/bin/pacman') == True:
                    system("sudo pacman -S nmap")

                system("cd {} && sudo git clone https://github.com/Screetsec/Dracnmap".format(paths))
                print(titles.done.format('Dracnmap'))
                print(titles.note_tools.format('Dracnmap', 'bash dracnmap-v2.2.sh'))

        print(titles.readmore.format('Dracnmap','http://bit.ly/2sTQtlS'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def nmap(titles):
    try:
        if name == 'nt':
            print(titles.installing.format('Nmap'))
            print(titles.downloading.format('nmap-7.70-setup.exe'))
            download('https://nmap.org/dist/nmap-7.70-setup.exe')
            system('.\\nmap-7.70-setup.exe')
            print(titles.done.format('Nmap'))
            print(titles.note_tools2.format('Nmap','nmap','CMD'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/nmap') == True:
                    print(titles.installed.format('Nmap'))

                else:
                    print(titles.installing.format('Nmap'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install nmap")
                        
                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S nmap")

                    print(titles.done.format('Nmap'))
                    
                print(titles.note_tools2.format('Nmap','nmap','Terminal'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sublist3r(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python3 = str(input(titles.installed_or_not.format('Python 3.7'))).strip()
            action(titles,python3)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python3[0].upper() == 'N':
                    print(titles.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(titles.note_python3)
                    system('.\\python-3.7.3.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP'):
                    sublist3r(titles)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG'):
                    sublist3r(titles)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT'):
                    sublist3r(titles)

                else:
                    print(titles.invalid)
                    sublist3r(titles)

            print(titles.installing.format("Sublist3r"))
            system("""cd C:\\ && git clone https://github.com/aboul3la/Sublist3r
            cd Sublist3r && pip install -r requirements.txt""")

        else:
            paths = the_path(titles, 'Sublist3r')
            print(titles.installing.format('Sublist3r'))
            system("""cd {} && sudo git clone https://github.com/aboul3la/Sublist3r
            cd Sublist3r && sudo pip install -r requirements.txt""".format(paths))

        print(titles.done.format('Sublist3r'))
        print(titles.note_tools.format('Sublist3r','python sublist3r.py'))
        print(titles.readmore.format('Sublist3r','http://bit.ly/2LCZ18X'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sslscan(titles):
    try:
        if name == 'nt':
            print(titles.installing.format('SSLScan'))
            print(titles.downloading.format('sslscan-win-1.11.11-rbsec.zip'))
            download('https://github.com/rbsec/sslscan/releases/download/1.11.11-rbsec/sslscan-win-1.11.11-rbsec.zip')
            print(titles.note_sslscan)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)
            
            else:
                if path.exists('/usr/bin/sslscan') == True:
                    print(titles.installed.format('SSLScan'))

                else:
                    print(titles.installing.format('SSLScan'))

                    if path.exists('/usr/bin/apt') == True:
                        system('sudo apt install sslscan')

                    elif path.exists('/usr/bin/pacman') == True:
                        system('sudo pacman -S sslscan')

                    print(titles.done.format('SSLScan'))

                print(titles.note_tools2.format('SSLScan','sslscan','Terminal'))

        print(titles.readmore.format('SSLScan', 'http://bit.ly/2MAQBNo'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def dnsmaper(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles, 'DNSMaper')
            print(titles.installing.format('DNSMaper'))
            system("""cd {} && sudo git clone https://github.com/le4f/dnsmaper
            cd dnsmaper && sudo pip2 install requests geoip2 signal""".format(paths))
            print(titles.done.format('DNSMaper'))
            print(titles.note_tools.format('DNSMaper','python2 dnsmaper.py'))

        print(titles.readmore.format('DNSMaper', 'http://bit.ly/2MoEx57'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def a2sv(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if path.exists('/usr/bin/pacman') == True:
                paths = the_path(titles,'A2SV')
                print(titles.installing.format('A2SV'))
                system("""cd {} && sudo git clone https://github.com/hahwul/a2sv
                cd a2sv && sudo pip2 install argparse netaddr""".format(paths))
                print(titles.done.format('A2SV'))
                print(titles.note_tools.format('A2SV','python2 a2sv.py'))
                
            else:
                if path.exists('/usr/bin/a2sv') == False:
                    print(titles.installed.format('A2SV'))

                else:
                    paths = the_path(titles, 'A2SV')
                    print(titles.installing.format('A2SV'))
                    system("""cd {} && sudo git clone https://github.com/hahwul/a2sv
                    cd a2sv && sudo bash install.sh""".format(paths))
                    print(titles.done.format('A2SV'))
                    
                print(titles.note_tools2.format('A2SV','a2sv','Terminal'))

        print(titles.readmore.format('A2SV','http://bit.ly/2KCDPz7'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def shodanhat(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    shodanhat(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    shodanhat(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    shodanhat(titles)

                else:
                    print(titles.invalid)
                    shodanhat(titles)

            system("""cd C:\\ && git clone https://github.com/HatBashBR/ShodanHat
            cd ShodanHat && pip uninstall nmap && pip install shodan python-nmap""")

        else:
            paths = the_path(titles,'ShodanHat')
            print(titles.installing.format('ShodanHat'))
            system("""cd {} && sudo git clone https://github.com/HatBashBR/ShodanHat"
            sudo pip2 uninstall nmap && sudo pip2 install shodan python-nmap""".format(paths))
  
        print(titles.done.format('ShodanHat'))
        print(titles.note_tools.format('ShodanHat','python2 shodanhat.py'))
        print(titles.readmore.format('ShodanHat','http://bit.ly/2KQnpDn'))
        
    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def hatcloud(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            ruby = str(input(titles.installed_or_not.format('Ruby-lang'))).strip()
            action(titles,ruby)

            if (git[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif ruby[0].upper() == 'N':
                    print(titles.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(titles.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    hatcloud(titles)

                elif (git.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    hatcloud(titles)

                elif (git.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    hatcloud(titles)

                else:
                    print(titles.invalid)
                    hatcloud(titles)

            print(titles.installing.format('HatCloud'))
            system("cd C:\\ && git clone https://github.com/HatBashBR/HatCloud")

        else:
            paths = the_path(titles,'HatCloud')
            print(titles.installing.format('HatCloud'))
            system("cd {} && sudo git clone https://github.com/HatBashBR/HatCloud".format(paths))

        print(titles.done.format('HatCloud'))
        print(titles.note_tools.format('HatCloud','ruby hatcloud.rb'))
        print(titles.readmore.format('HatCloud','http://bit.ly/2KAJC9m'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sub6(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git[0].upper() == 'HELP' or python2[0].upper() == 'HELP'):
                    sub6(titles)

                elif (git[0].upper() == 'CHANGRLOG' or python2[0].upper() == 'CHANGRLOG'):
                    sub6(titles)

                elif (git[0].upper() == 'ABOUT' or python2[0].upper() == 'ABOUT'):
                    sub6(titles)

                else:
                    print(titles.invalid)
                    sub6(titles)

            print(titles.installing.format('sub6'))
            system("cd C:\\ && git clone https://github.com/YasserGersy/sub6")

        else:
            paths = the_path(titles, 'sub6')
            print(titles.installing.format('sub6'))
            system("cd {} && sudo git clone https://github.com/YasserGersy/sub6".format(paths))

        print(titles.done.format('sub6'))
        print(titles.note_tools.format('sub6','python2 sub6.py'))
        print(titles.readmore.format('sub6','http://bit.ly/2Gh75td'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def masscan(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if path.exists('/usr/bin/masscan') == True:
                print(titles.installed.format('Masscan'))

            else:
                paths = the_path(titles,'Masscan')
                print(titles.installing.format('Masscan'))
                system("""cd {} && sudo git clone https://github.com/robertdavidgraham/masscan
                cd masscan && sudo make install""".format(paths))
                print(titles.done.format('Masscan'))

            print(titles.note_tools2.format('Masscan','masscan','Terminal'))

        print(titles.readmore.format('Masscan','http://bit.ly/2HqigzG'))
                    
    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def dnsmap(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/local/bin/dnsmap') == True or path.exists('/usr/bin/dnsmap') == True):
                print(titles.installed.format('dnsmap'))

            else:
                paths = the_path(titles,'dnsmap')
                print(titles.installing.format('dnsmap'))
                system("""cd {} && sudo git clone https://gitlab.com/kalilinux/packages/dnsmap.git
                cd dnsmap && sudo make install""".format(paths))
                print(titles.done.format('dnsmap'))

            print(titles.note_tools2.format('dnsmap','dnsmap','Terminal'))

        print(titles.readmore.format('dnsmap','http://bit.ly/2HoZiZX'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def infosploit(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    infosploit(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    infosploit(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    infosploit(titles)

                else:
                    print(titles.invalid)
                    infosploit(titles)

            print(titles.installing.format('InfoSploit'))
            system("cd C:\\ && git clone https://github.com/CybernetiX-S3C/InfoSploit")
            print(titles.done.format('InfoSploit'))
            print(titles.note_tools.format('InfoSploit','python Infosploit.py'))
 
        else:
            if path.exists('/usr/bin/Infosploit') == True:
                print(titles.installed.format('InfoSploit'))

            else:
                paths = the_path(titles,'InfoSploit')
                print(titles.installing.format('InfoSploit'))
                system("""cd {} && sudo git clone https://github.com/CybernetiX-S3C/InfoSploit
                cd InfoSploit && sudo bash install""".format(paths))
                print(titles.done.format('InfoSploit'))
                
            print(titles.note_tools2.format('InfoSploit','Infosploit','Terminal'))

        print(titles.readmore.format('InfoSploit','http://bit.ly/2LUfN4w'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def infoga(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'Infoga')
            print(titles.installing.format('Infoga'))
            system("""cd {} && sudo git clone https://github.com/m4ll0k/Infoga
            cd Infoga && sudo python2 setup.py install""".format(paths))
            print(titles.done.format('Infoga'))
            print(titles.note_tools.format('Infoga','python2 infoga.py'))

        print(titles.readmore.format('Infoga','http://bit.ly/2F6ioDW'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def httrack(titles):
    try:
        if name == 'nt':
            print(titles.installing.format('HTTrack'))
            print(titles.downloading.format('httrack-3.49.2.exe'))
            download('https://download.httrack.com/httrack-3.49.2.exe')
            system('.\\httrack-3.49.2.exe')
            print(titles.done.format('HTTrack'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/httrack') == True:
                    print(titles.installed.format('HTTrack'))
                    
                else:
                    print(titles.installing.format('HTTrack'))

                    if path.exists('/usr/bin/apt') == True:
                        system('sudo apt install httrack')

                    elif path.exists('/usr/bin/pacman') == True:
                        system('sudo pacman -S httrack')

                    print(titles.done.format('HTTrack'))
                    
                print(titles.note_tools2.format('HTTrack','httrack','Terminal'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def apt2(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'APT2')
            print(titles.installing.format('APT2'))
            system(""""cd {} && sudo git clone https://github.com/MooseDojo/apt2
            sudo pip2 install unqlite scapy""".format(paths))
            print(titles.done.format('APT2'))
            print(titles.note_tools.format('APT2','python2 apt2.py'))

        print(titles.readmore.format('APT2', 'http://bit.ly/2WVHP0z'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def inspy(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'InSpy')
            print(titles.installing.format('InSpy'))
            system("""cd {} && sudo git clone https://github.com/leapsecurity/InSpy
            cd InSpy && sudo pip2 install -r requirements.txt""".format(paths))
            print(titles.done.format('InSpy'))
            print(titles.note_tools.format('InSpy','python2 InSpy.py'))

        print(titles.readmore.format('InSpy','http://bit.ly/2n8P9J1'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def setoolkit(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'SEToolkit')
                print(titles.installing.format('SEToolkit'))
                metasploit(titles)
                system("""cd {} && sudo git clone https://github.com/trustedsec/social-engineer-toolkit set
                cd set && sudo pip2 install -r requirements.txt""".format(paths))
                print(titles.done.format('SEToolkit'))
                print(titles.note_tools.format('SEToolkit','sudo python2 setoolkit'))

        print(titles.readmore.format('SEToolkit','http://bit.ly/2EkvcHi'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def phishx(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'PhishX')
                print(titles.installing.format('PhishX'))

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S python-setuptools sendemail php xterm")

                system("""cd {} && sudo git clone https://github.com/rezaaksa/PhishX
                cd PhishX && sudo bash installer.sh""".format(paths))
                print(titles.done.format('PhishX'))
                print(titles.note_tools.format('PhishX','python3 PhishX.py'))

        print(titles.readmore.format('PhishX','http://bit.ly/2N7IM01'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def phisherman(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'PhisherMan')
            print(titles.installing.format('PhisherMan'))
            system("cd {} && sudo git clone https://github.com/FDX100/Phisher-man".format(paths))
            print(titles.done.format('PhisherMan'))
            print(titles.note_tools.format('PhisherMan','sudo python2 phisherman.py'))

        print(titles.readmore.format('PhisherMan','http://bit.ly/2QLy5DL'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def aron(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/aron') == True:
                    print(titles.installed.format('Aron'))

                else:
                    paths = the_path(titles, 'Aron')
                    print(titles.installing.format('Aron'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install golang-go")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S go")

                    system("""cd {} && sudo git clone https://github.com/m4ll0k/Aron
                    cd Aron && sudo go get github.com/m4ll0k/printer"
                    sudo go env | grep -i gopath && sudo export GOPATH=$HOME/go
                    sudo go build aron.go && sudo cp aron /usr/bin/""".format(paths))
                    print(titles.done.format('Aron'))

                print(titles.note_tools2.format('Aron','aron','Terminal'))

        print(titles.readmore.format('Aron','http://bit.ly/2MkbKyj'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def evilginx2(titles):
    try:
        if name == 'nt':
            print(titles.installing.format('Evilginx'))
            print(titles.downloading.format('evilginx_windows_x86_2.3.0.zip'))
            download('https://github.com/kgretzky/evilginx2/releases/download/2.3.0/evilginx_windows_x86_2.3.0.zip')
            print(titles.note_evilginx2)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/apt') == True:
                    paths = the_path(titles, 'Evilginx 2')
                    print(titles.installing.format('Evilginx 2'))
                    system("""cd {} && wget https://github.com/kgretzky/evilginx2/releases/download/2.3.0/evilginx_linux_x86_2.3.0.zip
                    sudo apt install unzip && unzip evilginx_linux_x86_2.3.0.zip -d evilginx2
                    cd evilginx2 && sudo bash install.sh""".format(paths))

                elif path.exists('/usr/bin/pacman') == True:
                    print(titles.installing.format('Evilginx 2'))
                    system("sudo pacman -S go && sudo pacman -S evilginx")

                print(titles.done.format('Evilginx 2'))
                print(titles.note_tools2.format('Evilginx 2','evilginx','Terminal'))

        print(titles.readmore.format('Evilginx 2','http://bit.ly/2O8cWFS'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def infinity(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    infinity(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    infinity(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    infinity(titles)

                else:
                    print(titles.invalid)
                    infinity(titles)

            print(titles.installing.format('infinity'))
            system("""cd C:\\ && pip install mechanize
            git clone https://github.com/s0md3v/infinity""")

        else:
            paths = the_path(titles,'infinity')
            print(titles.installing.format('infinity'))
            system("""cd {} && sudo pip2 install mechanize
            sudo git clone https://github.com/s0md3v/infinity""".format(paths))

        print(titles.done.format('infinity'))
        print(titles.note_tools.format('infinity','python2 infinity.py'))
        print(titles.readmore.format('infinity','http://bit.ly/2EZriD5'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def credsniper(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'CredSniper')

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S virtualenv gnupg certbot")

                system("""cd {} && sudo git clone https://github.com/ustayready/CredSniper
                cd CredSniper && sudo bash install.sh""".format(paths))
                print(titles.done.format('CredSniper'))
                print(titles.note_tools.format('CredSniper','python3 credsniper.py'))

        print(titles.readmore.format('CredSniper','http://bit.ly/2yXXrc1'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def ghost_phisher(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Ghost Phisher')
                print(titles.installing.format('Ghost Phisher'))
                metasploit(titles)
                system("cd {} && sudo git clone https://github.com/savio-code/ghost-phisher".format(paths))
                print(titles.done.format('Ghost Phisher'))
                print(titles.note_tools2.format('Ghost Phisher','sudo python2 ghost.py','ghost-phisher/Ghost-Phisher'))

        print(titles.readmore.format('Ghost Phisher','http://bit.ly/2HeR83c'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def subdomain_analyzer(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    subdomain_analyzer(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    subdomain_analyzer(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    subdomain_analyzer(titles)

                else:
                    print(titles.invalid)
                    subdomain_analyzer(titles)

            print(titles.installing.format('SubDomain-Analyzer'))
            system("""cd C:\\ && git clone https://github.com/El3ct71k/SubDomain-Analyzer
            cd SubDomain-Analyzer && pip install -r requirements.txt""")  

        else:
            paths = the_path(titles,'SubDomain-Analyzer')
            print(titles.installing.format('SubDomain-Analyzer'))
            system("""cd {} && git clone https://github.com/El3ct71k/SubDomain-Analyzer
            cd SubDomain-Analyzer && sudo pip2 install -r requirements.txt""".format(paths))
            
        print(titles.done.format('SubDomain-Analyzer'))
        print(titles.note_tools.format('SubDomain-Analyzer','python subdomain-analyzer.py'))
        print(titles.readmore.format('SubDomain-Analyzer','http://bit.ly/2NKLU2J'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sqlmap(titles):
    try:
        if name == 'nt':
            python3 = str(input(titles.installed_or_not.format('Python 3.7'))).strip()
            action(titles,python3)

            if python3[0].upper() == 'Y':
                pass

            elif python3[0].upper() == 'N':
                print(titles.downloading.format('python-3.7.3.exe'))
                download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                print(titles.note_python3)
                system('.\\python-3.7.3.exe')

            elif (python3.upper() == 'HELP' or python3.upper() == 'CHANGELOG' or python3.upper() == 'ABOUT'):
                sqlmap(titles)

            else:
                print(titles.invalid)
                sqlmap(titles)

            print(titles.installing.format('SQLMap'))
            system("pip install sqlmap")

        else:
            print(titles.installing.format('SQLMap'))
            system("sudo pip3 install sqlmap")
            
        print(titles.done.format('SQLMap'))
        print(titles.note_tools2.format('SQLMap','sqlmap','Terminal & CMD'))
        print(titles.readmore.format('SQLMap','http://bit.ly/2zArNjX'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sqlmate(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    sqlmate(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    sqlmate(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    sqlmate(titles)

                else:
                    print(titles.invalid)
                    sqlmate(titles)

            print(titles.installing.format('SQLMate'))
            system("""cd C:\\ && git clone https://github.com/s0md3v/sqlmate
            cd sqlmate && pip install -r requirements.txt""")

        else:
            paths = the_path(titles,'SQLMate')
            print(titles.installing.format('SQLMate'))
            system("""cd {} && sudo git clone https://github.com/s0md3v/sqlmate
            cd sqlmate && sudo pip2 install -r requirements.txt""".format(paths))
            
        print(titles.done.format('SQLMate'))
        print(titles.note_tools.format('SQLMate', 'python2 sqlmate'))
        print(titles.readmore.format('SQLMate','http://bit.ly/2C0DwXW'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def searchsploit(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/searchsploit') == True:
                    print(titles.installed.format('SearchSploit'))

                else:
                    print(titles.installing.format('SearchSploit'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install go-exploitdb")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudp pacman -S exploitdb")

                    print(titles.done.format('SearchSploit'))

                print(titles.note_tools2.format('SearchSploit','searchsploit','Terminal'))

        print(titles.readmore.format('SearchSploit','http://bit.ly/2svkh4C'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def brakemen(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Brakeman')
                print(titles.installing.format('Brakeman'))

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S ruby")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install ruby")

                system("""cd {} && sudo git clone https://github.com/presidentbeef/brakeman
                cd brakeman && sudo gem build brakeman.gemspec && sudo gem install brakeman*.gem""".format(paths))
                print(titles.done.format('Brakeman'))

            print(titles.note_tools.format('Brakeman','ruby /bin/brakeman'))

        print(titles.readmore.format('Brakeman','http://bit.ly/2L8GhKi'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def whatweb(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if path.exists('/usr/bin/whatweb') == True:
                print(titles.installed.format('WhatWeb'))

            else:
                paths = the_path(titles,'WhatWeb')
                print(titles.installing.format('WhatWeb'))
                system("""cd {} && sudo git clone https://github.com/urbanadventurer/WhatWeb
                cd WhatWeb && sudo make install""".format(paths))
                print(titles.done.format('WhatWeb'))

            print(titles.note_tools2.format('WhatWeb','whatweb','Terminal'))

        print(titles.readmore.format('WhatWeb','http://bit.ly/2H8IvZK'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def vulscan(titles):
    try:
        if name == 'nt':
            print(titles.installing.format('vulscan'))
            print(titles.downloading.format('nmap-7.70-setup.exe'))
            download('https://nmap.org/dist/nmap-7.70-setup.exe')
            system('.\\nmap-7.70-setup.exe')
            
        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                print(titles.installing.format('vulscan'))

                if path.exists('/usr/bin/apt') == True:
                    system('sudo apt install nmap')

                elif path.exists('/usr/bin/pacman'):
                    system('sudo pacman install nmap')

        print(titles.downloading.format('vulscan-master.zip'))
        download('https://github.com/scipag/vulscan/archive/master.zip')
        print(titles.readmore.format('vulscan','http://bit.ly/2DQfjbc'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def takeover(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    takeover(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    takeover(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    takeover(titles)

                else:
                    print(titles.invalid)
                    takeover(titles)

            print(titles.installing.format('TakeOver'))
            system("cd C:\\ && git clone https://github.com/m4ll0k/takeover")

        else:
            paths = the_path(titles,'TakeOver')
            print(titles.installing.format('TakeOver'))
            system("cd {} && sudo git clone https://github.com/m4ll0k/takeover".format(paths))

        print(titles.done.format('TakeOver'))
        print(titles.note_tools.format('TakeOver','python2 takeover.py'))
        print(titles.readmore.format('TakeOver','http://bit.ly/2uPGGvN'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def openvas(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)
            else:
                print(titles.installing.format('OpenVAS'))

                if path.exists('/usr/bin/pacman') == True:
                    system('sudo pacman -S openvas')

                elif path.exists('/usr/bin/apt') == True:
                    system('sudo apt install openvas')

                print(titles.done.format('OpenVAS'))
                print(titles.note_tools2.format('OpenVAS','openvas-start','Terminal'))

        print(titles.readmore.format('OpenVAS','http://bit.ly/2FtrxnV'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def droid_hunter(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                    print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/dhunter') == True:
                    print(titles.installed.format('Droid-Hunter'))

                else:
                    paths = the_path(titles,'Droid-Hunter')
                    print(titles.installing.format('Droid-Hunter'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install ruby")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S ruby")

                    system("""cd {} && sudo git clone https://github.com/hahwul/droid-hunter
                    cd droid-hunter && sudo bash install.sh""".format(paths))
                    print(titles.done.format('Droid-Hunter'))

                print(titles.note_tools2.format('Droid-Hunter','dhunter','Terminal'))

        print(titles.readmore.format('Droid-Hunter','http://bit.ly/2tY1Nuj'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def patrowl(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'PatrOwl')
                print(titles.installing.format('PatrOwl'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install curl rabbitmq-server postgresql build-essential")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S curl rabbitmq postgresql base-devel")

                system("""cd {} && sudo git clone https://github.com/Patrowl/PatrowlManager && cd PatrOwlManager
                sudo pip2 install virtualenv && sudo pip2 install -r requirements.txt""".format(paths))
                print(titles.done.format('PatrOwl'))
                print(titles.note_tools.format('PatrOwl','start-server.sh'))

        print(titles.readmore.format('PatrOwl','http://bit.ly/2InjYAy'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def infection_monkey(titles):
    try:
        if name == 'nt':
            print(titles.installing.format('Infection Monkey'))
            print(titles.downloading.format('monkey-windows-32.exe'))
            download("https://github.com/guardicore/monkey/releases/download/v1.6.3/monkey-windows-32.exe")
            system(".\\monkey-windows-32.exe")

        else:
            if path.exists('/usr/bin/apt') == True:
                print(titles.installing.format('Infection Monkey'))
                system("""sudo wget https://github.com/guardicore/monkey/releases/download/v1.6.2/infection_monkey_deb.1.6.2.tgz
                sudo tar xvzf infection_monkey_deb.1.6.2.tgz && sudo dpkg -i monkey_island.deb""")
                print(titles.done.format('Infection Monkey'))

            else:
                print(titles.run_well.format('Debian & Windows'))

        print(titles.readmore.format('Infection Monkey','http://bit.ly/2sldHOf'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def vuls(titles):
    try:
        from platform import architecture

        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if architecture()[0] == "64bit":
                paths = the_path(titles,'Vuls')
                print(titles.installing.format('Vuls'))
                system("""cd {} && sudo mkdir vuls && cd vuls
                sudo wget https://github.com/future-architect/vuls/releases/download/v0.7.0/vuls_0.7.0_linux_amd64.tar.gz
                sudo tar xvzf vuls_0.7.0_linux_amd64.tar.gz && sudo chmod +x vuls""".format(paths))
                print(titles.done.format('Vuls'))
                print(titles.note_tools.format('Vuls','sudo ./vuls'))

            else:
                print(titles.only_compatible.format("64-bit OS"))

        print(titles.readmore.format('Vuls','http://bit.ly/2kxngpY'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def wpseku(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'WPSeku')
            print(titles.installing.format('WPSeku'))
            system("""cd {} && sudo git clone https://github.com/m4ll0k/WPSeku
            cd WPSeku && sudo pip3 install -r requirements.txt""".format(paths))
            print(titles.done.format('WPSeku'))
            print(titles.note_tools.format('WPSeku','python3 wpseku.py'))

        print(titles.readmore.format('WPSeku','http://bit.ly/2D8be1N'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def wpscan(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/wpscan') == True:
                    print(titles.installed.format('WPScan'))

                else:
                    if path.exists('/usr/bin/apt') == True:
                        paths = the_path(titles,'WPScan')
                        print(titles.installing.format('WPScan'))
                        system("""sudo apt install libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby ruby-bundler ruby-dev build-essential libgmp-dev zlib1g-dev
                        cd {} && sudo git clone https://github.com/wpscanteam/wpscan
                        cd wpscan && sudo bundle install && sudo rake install""".format(paths))

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S wpscan")

                    print(titles.done.format('WPScan'))
                    
                print(titles.note_tools2.format('WPScan','wpscan','Terminal'))

        print(titles.readmore.format('WPScan','https://github.com/wpscanteam/wpscan'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def routersploit(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'RouterSploit')
            print(titles.installing.format('RouterSploit'))
            system("""cd {} && sudo git clone https://github.com/threat9/routersploit
            cd routersploit && sudo python3 pip install -r requirements.txt""".format(paths))
            print(titles.done.format('RouterSploit'))
            print(titles.note_tools.format('RouterSploit','python3 rsf.py'))

        print(titles.readmore.format('RouterSploit','http://bit.ly/2s94mcV'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def xsstrike(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'XSStrike')
            print(titles.installing.format('XSStrike'))
            system("""cd {} && sudo git clone https://github.com/s0md3v/XSStrike
            cd XSStrike && sudo pip3 install -r requirements.txt""".format(paths))
            print(titles.done.format('XSStrike'))
            print(titles.note_tools.format('XSStrike','python3 xsstrike.py'))

        print(titles.readmore.formt('XSStrike','http://bit.ly/2iGBEv9'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def striker(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'Striker')
            print(titles.installing.format('Striker'))
            system("""cd {} && sudo git clone https://github.com/s0md3v/Striker
            cd Striker && sudo pip3 install -r requirements.txt""".format(paths))
            print(titles.done.format('Striker'))
            print(titles.note_tools.format('Striker','python3 striker.py'))

        print(titles.readmore.formt('Striker','http://bit.ly/2EFQG1z'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def raptor(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'Raptor')
            print(titles.installing.format('Raptor'))
            system("""cd {} && sudo git clone https://github.com/dpnishant/raptor
            cd raptor && sudo bash install.sh""".format(paths))
            print(titles.done.format('Raptor'))
            print(titles.note_tools.format('Raptor','sudo bash start.sh'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
                print(titles.wsl)
            
            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('Raptor','http://bit.ly/2sAtbBq'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def breacher(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    breacher(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    breacher(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    breacher(titles)

                else:
                    print(titles.invalid)
                    breacher(titles)

            print(titles.installing.format("Breacher"))
            system("cd C:\\ && git clone https://github.com/s0md3v/Breacher")

        else:
            paths = the_path(titles,'Breacher')
            print(titles.installing.format('Breacher'))
            system("cd {} && sudo https://github.com/s0md3v/Breacher".format(paths))

        print(titles.done.format("Breacher"))
        print(titles.note_tools.format("Breacher","python2 breacher.py"))
        print(titles.readmore.format("Breacher","http://bit.ly/2ohlBa5"))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def wascan(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'WAScan')
            print(titles.installing.format('WAScan'))
            system("cd {} && sudo git clone https://github.com/m4ll0k/WAScan".format(paths))
            print(titles.done.format('WAScan'))
            print(titles.note_tools.format('WAScan','python2 wascan.py'))

        print(titles.readmore.format('WAScan','http://bit.ly/2HL9OZG'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def xsser(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if path.exists('/usr/bin/xsser') == True:
                print(titles.installed.format('XSSer'))

            else:
                paths = the_path(titles,'XSSer')
                print(titles.installing.format('XSSer'))
                system("""cd {} && sudo git clone https://github.com/epsylon/xsser && cd xsser/xsser
                sudo pip2 install pycurl xmlbuilder geoip BeautifulSoup && sudo python2 setup.py install""".format(paths))
                print(titles.done.format('XSSer'))
                
            print(titles.note_tools2.format('XSSer','xsser','Terminal'))

        print(titles.readmore.format('XSSer','http://bit.ly/2DwhImM'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def spectre_meldown_checker(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'spectre-meltdown-checker')
            print(titles.installing.format('spectre-meltdown-checker'))
            system("cd {} && sudo git clone https://github.com/speed47/spectre-meltdown-checker".format(paths))
            print(titles.done.format('spectre-meltdown-checker'))
            print(titles.note_tools.format('spectre-meltdown-checker','sudo bash spectre-meltdown-checker.sh'))

        print(titles.readmore.format('spectre-meltdown-checker','http://bit.ly/30JWP47'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def brutedum(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'BruteDum')
                print(titles.installing.format('BruteDum'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install nmap hydra medusa ncrack")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S nmap hydra medusa ncrack")

                system("""cd {} && sudo git clone https://github.com/GitHackTools/BruteDum""".format(paths))
                print(titles.done.format('BruteDum'))
                print(titles.note_tools.format('BruteDum','python3 brutedum.py'))

        print(titles.readmore.format('BruteDum','http://bit.ly/2ISotWY'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def ftpbruter(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python3 = str(input(titles.installed_or_not.format('Python 3.7'))).strip()
            action(titles,python3)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python3[0].upper() == 'N':
                    print(titles.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(titles.note_python3)
                    system('.\\python-3.7.3.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP'):
                    ftpbruter(titles)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG'):
                    ftpbruter(titles)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT'):
                    ftpbruter(titles)

                else:
                    print(titles.invalid)
                    ftpbruter(titles)

            print(titles.installing.format('FTPBruter'))
            system("cd C:\\ && git clone https://github.com/GitHackTools/FTPBruter")

        else:
            paths = the_path(titles,"FTPBruter")
            print(titles.installing.format("FTPBruter"))
            system("cd {} && sudo git clone https://github.com/GitHackTools/FTPBruter".format(paths))

        print(titles.done.format("FTPBruter"))
        print(titles.note_tools.format("FTPBruter","python3 ftpbruter.py"))
        print(titles.readmore.format("FTPBruter","http://bit.ly/2IzrGtk"))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def hash_buster(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python3 = str(input(titles.installed_or_not.format('Python 3.7'))).strip()
            action(titles,python3)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python3[0].upper() == 'N':
                    print(titles.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(titles.note_python3)
                    system('.\\python-3.7.3.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP'):
                    hash_buster(titles)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG'):
                    hash_buster(titles)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT'):
                    hash_buster(titles)

                else:
                    print(titles.invalid)
                    hash_buster(titles)

            print(titles.installing.format('Hash-Buster'))
            system("cd C:\\ && git clone https://github.com/s0md3v/Hash-Buster")
            print(titles.done.format("Hash-Buster"))
            print(titles.note_tools.format('Hash-Huster','python hash.py'))

        else:
            if path.exists('/usr/local/bin/buster') == True:
                print(titles.installed.format('Hash-Buster'))

            else:
                paths = the_path(titles,'Hash-Buster')
                print(titles.installing.format('Hash-Buster'))
                system("""cd {} && sudo git clone https://github.com/s0md3v/Hash-Buster
                cd Hash-Buster && sudo make install""".format(paths))
                print(titles.done.format("Hash-Buster"))
                
            print(titles.note_tools2.format("Hash-Buster",'buster','Terminal'))

        print(titles.readmore.format('Hash-Buster','http://bit.ly/2GxqhPL'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def socialbox(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'SocialBox')
            print(titles.installing.format('SocialBox'))

            if path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -sS tor")

            system("""cd {} && sudo git clone https://github.com/TunisianEagles/SocialBox
            cd SocialBox && sudo bash install.sh""".format(paths))
            print(titles.done.format('SocialBox'))
            print(titles.note_tools.format('SocialBox','bash SocialBox.sh'))

        print(titles.readmore.format('SocialBox','http://bit.ly/2NJ6GnQ'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def blazy(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    blazy(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    blazy(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    blazy(titles)

                else:
                    print(titles.invalid)
                    blazy(titles)

            print(titles.installing.format('Blazy'))
            system("""cd C:\\ && git clone https://github.com/s0md3v/Blazy
            cd Blazy && pip install -r requirements.txt""")

        else:
            paths = the_path(titles,'Blazy')
            print(titles.installing.format('Blazy'))
            system("""cd {} && sudo git clone https://github.com/s0md3v/Blazy
            cd Blazy && sudo pip2 install -r requirements.txt""".format(paths))

        print(titles.done.format('Blazy'))
        print(titles.note_tools.format('Blazy', 'python2 blazy.py'))
        print(titles.readmore.format('Blazy','http://bit.ly/2owpqYx'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def ncrack(titles):
    try:
        if name == 'nt':
            print(titles.installing.format('Ncrack'))
            print(titles.downloading.format('ncrack-0.6-setup.exe'))
            download('https://nmap.org/ncrack/dist/ncrack-0.6-setup.exe')
            system(".\\ncrack-0.6-setup.exe")
            print(titles.done.format('Ncrack'))
            print(titles.note_tools2.format('Ncrack','ncrack','CMD'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/ncrack') == True:
                    print(titles.installed.format('Ncrack'))

                else:
                    print(titles.installing.format('Ncrack'))
                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt instal ncrack")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S ncrack")

                    print(titles.done.format('Ncrack'))
                    
                print(titles.note_tools2.format('Ncrack','ncrack','Terminal'))
                    
        print(titles.readmore.format('Ncrack','http://bit.ly/2BxF3Y8'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def kickthemout(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'KickTheOut')
            print(titles.instaling.format('KickThemOut'))

            if path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S tcpdump")

            elif path.exists('/usr/bin/apt') == True:
                system("sudo apt install tcpdump")

            system("""cd {} && sudo git clone https://github.com/k4m4/kickthemout
            cd kickthemout && sudo pip3 uninstall nmap && sudo pip3 install -r requirements.txt""".format(paths))
            print(titles.done.format('KickThemOut'))
            print(titles.note_tools.format('KickThemOut','sudo python3 kickthemout.py'))

        print(titles.readmore.format('KickThemOut','http://bit.ly/30SMUJC'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sniffair(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'SniffAir')
            print(titles.installing.format('SniffAir'))
            system("""cd {} && sudo git clone https://github.com/Tylous/SniffAir
            cd SniffAir && sudo bash setup.sh""".format(paths))
            print(titles.done.format('SniffAir'))
            print(titles.note_tools.format('SniffAir','python2 SniffAir.py'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('SniffAir','http://bit.ly/2U06v5S'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def wifi_pumpkin(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'WiFi-Pumpkin')
            print(titles.installing.format('WiFi-Pumpkin'))
            system("""cd {} && sudo https://github.com/P0cL4bs/WiFi-Pumpkin
            cd WiFi-Pumpkin && sudo bash installer.sh --install""".format(paths))
            print(titles.done.format('WiFi-Pumpkin'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('WiFi-Pumpkin','http://bit.ly/2MFWIjB'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def airgeddon(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/airgeddon') == True:
                    print(titles.installed.format('Airgeddon'))

                else:
                    if path.exists('/usr/bin/pacman') == True:
                        system("""sudo pacman -S bettercap bully ccze crunch dsniff ethtool ettercap hashcat sslstrip lighttpd john hostapd iptables nftables pciutils pixiewps reaver usbutils
                        sudo wget https://github.com/v1s1t0r1sh3r3/airgeddon/raw/master/binaries/arch/airgeddon-git-9.20-1-any.pkg.tar.xz
                        sudo pacman -U pacman -U airgeddon-git-9.20-1-any.pkg.tar.xz""")

                    elif path.exists('/usr/bin/apt') == True:
                        system("""sudo wget https://github.com/v1s1t0r1sh3r3/airgeddon/raw/master/binaries/kali/airgeddon_9.20-1_all.deb
                        sudo dpkg -i airgeddon_9.20-1_all.deb""")

                    print(titles.done.format('Airgeddon'))
                    
                print(titles.note_tools2.format('Airgeddon','sudo airgeddon','Terminal'))

        print(titles.readmore.format('Airgeddon','http://bit.ly/2tOQ5Dd'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def pikarma(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'PiKarma')
                print(titles.installing.format('PiKarma'))
                
                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install aircrack-ng")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S aircrack-ng")

                system("""cd {} && sudo git clone https://github.com/WiPi-Hunter/PiKarma && sudo pip2 install termcolor""".format(paths))
                print(titles.done.format('PiKarma'))
                print(titles.note_tools.format('PiKarma','python2 PiKarma.py'))

        print(titles.readmore.format('PiKarma','http://bit.ly/2slyUaC'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def wifite2(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Wifite 2')
                print(titles.installing.format('Wifite 2'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install aicrack-ng tshark reaver bully cowpatty pyrit hashcat ncxtools hcxdumptool hcxpcaptool")

                elif path.exists('/usr/bin/pacman'):
                    system("sudo pacman -S aicrack-ng tshark reaver bully cowpatty pyrit hashcat ncxtools hcxdumptool hcxpcaptool")

                system("""cd {} && sudo git clone https://github.com/derv82/wifite2
                cd wifite2 && sudo python2 setup.py install""".format(paths))
                print(titles.done.format('Wifite 2'))
                print(titles.note_tools.format('Wifite2','sudo python2 Wifite.py'))

        print(titles.readmore.format('Wifite 2','http://bit.ly/2Wvf4Lg'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def pixiewps(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if path.exists('/usr/local/bin/pixiewps') == True:
                print(titles.installed.format('PixieWPS'))

            else:
                paths = the_path(titles,'PixieWPS')
                print(titles.installing.format('PixieWPS'))
                system("""cd {} && sudo git clone https://github.com/wiire-a/pixiewps
                cd pixiewps && sudo make install""".format(paths))
                print(titles.done.format('PixieWPS'))
                
            print(titles.note_tools.format('PixieWPS','pixiewps','Terminal'))

        print(titles.readmore.format('PixieWPS','http://bit.ly/2XgsHLs'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def fluxion(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Fluxion')
                print(titles.installing.format('Fluxion'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install aircrack-ng coreutils awk iw unzip bc xterm binutils macchanger php-cgi openssl pyrit")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S aircrack-ng coreutils awk iw unzip bc xterm binutils macchanger php-cgi  pyrit")

                system("""cd {} && sudo git clone https://github.com/FluxionNetwork/fluxion
                cd fluxion && sudo git clone https://github.com/aircrack-ng/mdk4
                cd mdk4 && sudo make install
                cd {}/fluxion && sudo bash fluxion.sh -i""".format(paths,paths))
                print(titles.done.format('Fluxion'))
                print(titles.note_tools.format('Fluxion','sudo bash fluxion.sh'))

        print(titles.readmore.format('Fluxion','http://bit.ly/2JJELln'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def reaver(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/reaver') ==  True:
                    print(titles.installed.format('Reaver'))

                else:
                    print(titles.installing.format('Reaver'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install reaver build-essential libpcap-dev aircrack-ng pixiewps")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S reaver libpcap aircrack-ng pixiewps")

                    print(titles.done.format('Reaver'))
                    
                print(titles.note_tools2.format('Reaver','reaver','Terminal'))

        print(titles.readmore.format('Reaver','http://bit.ly/2GRlTMY'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def zarp(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'Zarp')
            print(titles.installing.format('Zarp'))
            system("""cd {} && sudo git clone https://github.com/hatRiot/zarp
            cd zarp && sudo pip2 install -r requirements.txt
            sudo pip2 install scapy mitmproxy config netlib paramiko odict""".format(paths))
            print(titles.done.format('Zarp'))
            print(titles.note_tools.format('Zarp','sudo python2 zarp.py'))

        print(titles.readmore.format('Zarp','http://bit.ly/2H1sJ1f'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def xerosploit(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            if path.exists('/usr/bin/xerosploit') == True:
                print(titles.installed.format('Xerosploit'))

            else:
                paths = the_path(titles,'Xerosploit')
                print(titles.installing.format('Xerosploit'))
                system("""cd {} && sudo git clone https://github.com/LionSec/xerosploit
                cd xerosploit && sudo python2 install.py""".format(paths))
                print(titles.done.format('Xerosploit'))

            print(titles.note_tools2.format('Xerosploit','sudo xerosploit','Terminal'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
                print(titles.wsl)

            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('Xerosploit','http://bit.ly/2q4qpAD'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def seth(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Seth')
                print(titles.installing.format('Seth'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install tcpdump dsniff openssl && sudo pip3 install hexdump")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S tcpdump dsniff openssl && sudo pip3 install hexdump")

                system("cd {} && sudo git clone https://github.com/SySS-Research/Seth".format(paths))
                print(titles.done.format('Seth'))
                print(titles.note_tools.format('Seth','sudo bash seth.sh'))

        print(titles.readmore.format('Seth','http://bit.ly/2DamOVy'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def wifiphisher(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            if path.exists('/usr/bin/wifiphisher'):
                print(titles.installed.format('Wifiphisher'))

            else:
                paths = the_path(titles,'Wifiphisher')
                print(titles.installing.format('Wifiphisher'))
                system("""cd {} && sudo git clone https://github.com/wifiphisher/wifiphisher
                cd wifiphisher && sudo python2 setup.py install""".format(paths))
                print(titles.done.format('Wifiphisher'))
                
            print(titles.note_tools2.format('Wifiphisher','sudo wifiphisher','Terminal'))

        print(titles.readmore.format('Wifiphisher','http://bit.ly/2W3srhs'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sharp(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_supprt_windows)

        else:
            paths = the_path(titles,'shARP')
            print(titles.installing.format('shARP'))

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install aircrack-ng espeak")

            elif path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S aircrack-ng espeak")

            system("cd {} && https://github.com/europa502/shARP".format(paths))
            print(titles.done.format('shARP'))
            print(titles.note_tools.format('shARP','sudo bash shARP.sh'))

        print(titles.readmore.format('shARP','http://bit.ly/2FxBwYk'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sharp_2(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)

        else:
            paths = the_path(titles,'shARP 2.0')
            print(titles.installing.format('shARP 2.0'))

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install aircrack-ng espeak")

            elif path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S aircrack-ng espeak")

            system("cd {} && sudo git clone https://github.com/europa502/shARP_2.0 shARP2".format(paths))
            print(titles.done.format('shARP 2.0'))
            print(titles.note_tools.format('shARP 2.0','sudo bash shARP.sh'))

        print(titles.readmore.format('shARP 2.0','http://bit.ly/2FZDMrQ'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def eviltwinframework(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'EvilTwinFramework')
            print(titles.installing.format('EvilTwinFramework'))
            system("""cd {} && sudo git clone https://github.com/Esser420/EvilTwinFramework
            cd EvilTwinFramework && sudo python2 setup.py""".format(paths))
            print(titles.done.format('EviltwinFramework'))
            print(titles.note_tools.format('EvilTwinFramework','sudo python2 etfconsole.py'))
            
        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('EvilTwinFramework','http://bit.ly/2Hw6owh'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def the_rogue_toolkit(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'The Rogue Toolkit')
            print(titles.installing.format('The Rogue Toolkit'))
            system("""cd {} && sudo git clone https://github.com/InfamousSYN/rogue
            cd rogue && sudo python2 install.py""".format(paths))
            print(titles.done.format('The Rogue Toolkit'))
            print(titles.note_tools.format('The Rogue Toolkit','sudo python2 rogue.py'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('The Rogue Toolkit','http://bit.ly/2UR5UEE'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sitebroker(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    sitebroker(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    sitebroker(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    sitebroker(titles)

                else:
                    print(titles.invalid)
                    sitebroker(titles)

            print(titles.installing.format('SiteBroker'))
            system("""cd C:\\ && git clone https://github.com/Anon-Exploiter/SiteBroker
            cd SiteBroker && pip install -r requirements.txt""")

        else:
            paths = the_path(titles,'SiteBroker')
            print(titles.installing.format('SiteBroker'))
            system("""cd {} && sudo git clone https://github.com/Anon-Exploiter/SiteBroker
            cd SiteBroker && sudo pip2 install -r requirements.txt""".format(paths))
            
        print(titles.done.format('SiteBroker'))
        print(titles.note_tools.format('SiteBroker','python2 SiteBroker.py'))
        print(titles.readmore.format('SiteBroker','http://bit.ly/2MwTdeF'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def websploit(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'WebSploit')
            print(titles.installing.format('WebSploit'))
            metasploit(titles)

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install aircrack-ng xterm")

            elif path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S aircrack-ng xterm")

            system("cd {} && sudo git clone https://github.com/websploit/websploit/blob/master/websploit".format(paths))
            print(titles.done.format('WebSploit'))
            print(titles.note_tools.format('WebSploit','python2 websploit'))

        print(titles.readmore.format('WebSploit','http://bit.ly/2MpIthn'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def wpsploit(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    wpsploit(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    wpsploit(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    wpsploit(titles)

                else:
                    print(titles.invalid)
                    wpsploit(titles)

            print(titles.installing.format('WPSploit'))
            system("cd C:\\ && git clone https://github.com/offshores/WPSploit")

        else:
            paths = the_path(titles,'WPSploit')
            print(titles.installing.format('WPSploit'))
            system("cd {} && sudo git clone https://github.com/offshores/WPSploit".format(paths))
            
        print(titles.done.format('WPSploit'))
        print(titles.note_tools.format('WPSploit', 'python2 wpsploit.py'))
        print(titles.readmore.format('WPSploit','http://bit.ly/2MwTdeF'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def zoom(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    zoom(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    zoom(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    zoom(titles)

                else:
                    print(titles.invalid)
                    zoom(titles)

            print(titles.installing.format('Zoom'))
            system("""cd C:\\ && git clone https://github.com/gcxtx/Zoom
            cd Zoom && pip install -r requirements.txt""")

        else:
            paths = the_path(titles,'Zoom')
            print(titles.installing.format('Zoom'))
            system("""cd {} && sudo git clone https://github.com/gcxtx/Zoom
            cd Zoom && sudo pip2 install -r requirements.txt""".format(paths))
            
        print(titles.done.format('Zoom'))
        print(titles.note_tools.format('Zoom','python2 zoom.py'))
        print(titles.readmore.format('Zoom','http://bit.ly/2HLR66h'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def nosqlmap(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'NoSQLMap')
            print(titles.installing.format('NoSQLMap'))
            metasploit(titles)
            system("""cd {} && sudo git clone https://github.com/codingo/NoSQLMap
            cd NoSQLMap && sudo python2 setup.py install""".format(paths))
            print(titles.done.format('NoSQLMap'))
            print(titles.note_tools.format('NoSQLMap','python2 nosqlmap.py'))

        print(titles.readmore.format('NoSQLMap','http://bit.ly/2JcYuWF'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def sqlcake(titles):
    try:
        if name == 'nt':
            ruby = str(input(titles.installed_or_not.format('Ruby-lang')))
            action(titles,ruby)

            if ruby[0].upper() == 'Y':
                pass

            elif ruby[0].upper() == 'N':
                print(titles.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                print(titles.note_ruby)
                system('.\\rubyinstaller-2.6.3-1-x86.exe')

            elif (ruby.upper() == 'HELP' or ruby.upper() == 'CHANGELOG' or ruby.upper() == 'ABOUT'):
                sqlcake(titles)

            else:
                print(titles.invalid)
                sqlcake(titles)

            print(titles.downloading.format('sqlcake-v1.1.tar'))
            download('https://excellmedia.dl.sourceforge.net/project/sqlcake/sqlcake-v1.1.tar')
            print(titles.note_sqlcake)

        else:
            paths = the_path(titles,'sqlcake')
            print(titles.installing.format(titles))
            system("""cd {} && sudo mkdir sqlcake
            cd sqlmake && sudo wget https://excellmedia.dl.sourceforge.net/project/sqlcake/sqlcake-v1.1.tar
            sudo tar -xf sqlcake-v1.1.tar""".format(paths))
            print(titles.done.format('sqlcake'))
            print(titles.note_tools.format('sqlcake','ruby sqlcake.rb'))

        print(titles.readmore.format('sqlcake','http://bit.ly/2N0kOFl'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def bsqlinjector(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            ruby = str(input(titles.installed_or_not.format('Ruby-lang'))).strip()
            action(titles,ruby)

            if (git[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif ruby[0].upper() == 'N':
                    print(titles.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(titles.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    bsqlinjector(titles)

                elif (git.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    bsqlinjector(titles)

                elif (git.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    bsqlinjector(titles)

                else:
                    print(titles.invalid)
                    bsqlinjector(titles)

            print(titles.installing.format('BSQLinjector'))
            system("cd C:\\ && git clone https://github.com/enjoiz/BSQLinjector")

        else:
            paths = the_path(titles,'BSQLinjector')
            print(titles.installing.format('BSQLinjector'))
            system("cd {} && git clone https://github.com/enjoiz/BSQLinjector".format(paths))

        print(titles.done.format('BSQLinjector'))
        print(titles.note_tools.format('BSQLinjector','ruby BSQLinjector.rb'))
        print(titles.readmore.format('BSQLinjector','http://bit.ly/2M0HGn5'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def xxeinjector(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            ruby = str(input(titles.installed_or_not.format('Ruby-lang'))).strip()
            action(titles,ruby)

            if (git[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif ruby[0].upper() == 'N':
                    print(titles.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(titles.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    xxeinjector(titles)

                elif (git.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    xxeinjector(titles)

                elif (git.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    xxeinjector(titles)

                else:
                    print(titles.invalid)
                    xxeinjector(titles)

            print(titles.installing.format('XXEinjector'))
            system("cd C:\\ && git clone https://github.com/enjoiz/XXEinjector")

        else:
            paths = the_path(titles,'XXEinjector')
            print(titles.installing.format('XXEinjector'))
            system("cd {} && git clone https://github.com/enjoiz/XXEinjector".format(paths))

        print(titles.done.format('XXEinjector'))
        print(titles.note_tools.format('XXEinjector','ruby XXEinjector.rb'))
        print(titles.readmore.format('XXEinjector','http://bit.ly/2Opk8da'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def badmod(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'BadMod')
            print(titles.installing.format('BadMod'))

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install php php-curl")

            elif path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S php curl")

            system("cd {} && sudo git clone https://github.com/MrSqar-Ye/BadMod".format(paths))
            print(titles.done.format('BadMod'))
            print(titles.note_tools.format('BadMod','sudo php BadMod.php'))

        print(titles.readmore.format('BadMod','http://bit.ly/2IRyiRk'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def roxysploit(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_tools)

            else:
                paths = the_path(titles,'roxysploit')
                print(titles.installing.format('roxysploit'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""cd {} && sudo git clone https://github.com/andyvaikunth/roxysploit && sudo pacman -S android-tools
                    sudo pip2 install logging impacket pysmb threading socket socks zipfile shutil io struct re optparse binascii base64 urllib2 urllib requests commands paramiko scapy whois rlcompleter readline terminaltables platform""".format(paths))
                    print(titles.done.format('roxysploit'))
                    print(titles.note_tools.format('roxysploit','sudo python2 roxy.py'))

                else:
                    system("""cd {} && sudo git clone https://github.com/andyvaikunth/roxysploit
                    cd roxwpsploitysploit && sudo bash install""".format(paths))
                    print(titles.done.format('roxysploit'))
                    print(titles.note_tools2.format('roxyspoit','sudo rsfc'))

        print(titles.readmore.format('roxysploit','http://bit.ly/2HodbHU'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def lunar(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    lunar(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    lunar(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    lunar(titles)

                else:
                    print(titles.invalid)
                    lunar(titles)

            print(titles.installing.format('Lunar'))
            system("""cd C:\\ && git clone https://github.com/Zucccs/Lunar
            cd Lunar && .\\install.bat""")  
            print(titles.done.format('Lunar'))
            print(titles.note_tools.format('Lunar','python main.py'))

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Lunar')
                print(titles.installing.format('Lunar'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""cd {} && sudo git clone https://github.com/Zucccs/Lunar/
                    sudo pip2 install requests datetime subprocess colorama cryptography urllib2
                    sudo pacman -S wireshark-cli wireshark-qt
                    sudo git clone https://github.com/vanhauser-thc/thc-hydra
                    cd thc-hydra && sudo ./configure
                    sudo make && sudo make install
                    cd hydra-gtk && sudo ./configure
                    sudo make && sudo make install""".format(paths))

                elif path.exists('/usr/bin/apt') == True:
                    system("""cd {} && sudo git clone https://github.com/Zucccs/Lunar
                    cd Lunar && sudo bash install.sh""".format(paths))

                print(titles.done.format('Lunar'))
                print(titles.note_tools.format('Lunar','python2 main.py'))

        print(titles.readmore.format('Lunar','http://bit.ly/2IEOTvp'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def autordpwn(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            powershell = str(input(titles.installed_or_not.format('PowerShell'))).strip()
            action(titles,powershell)

            if (git.upper() == 'Y' and powershell.upper() == 'Y'):
                pass

            else:
                if git.upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif powershell.upper() == 'N':
                    print(titles.note_powershell)

                elif (git.upper() == 'HELP' or powershell.upper() == 'HELP'):
                    autordpwn(titles)

                elif (git.upper() == 'CHANGELOG' or powershell.upper() == 'CHANGELOG'):
                    autordpwn(titles)

                elif (git.upper() == 'ABOUT' or powershell.upper() == 'ABOUT'):
                    autordpwn(titles)

                else:
                    print(titles.invalid)
                    autordpwn(titles)

            print(titles.installing.format('AutoRDPwn'))
            system("cd C:\\ && git clone https://github.com/JoelGMSec/AutoRDPwn/")
            print(titles.done.format('AutoRDPwn'))
            print(titles.note_tools.format('AutoRDPwn','.\\AutoRDPwn.ps1'))

        else:
            print(titles.only_compatible.format('PowerShell'))

        print(titles.readmore.format('AutoRDPwn','http://bit.ly/2VNcpck'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def expliot(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if path.exists('/bin/efconsole') == True:
                print(titles.installed.format('eXpliot'))

            else:
                paths = the_path(titles,'eXpliot')
                print(titles.installing.format('eXpliot'))

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S libusb glib")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install libglib2.0-dev libusb-1.0")

                system("""cd {} && sudo git clone https://gitlab.com/expliot_framework/expliot
                cd expliot && sudo python3 setup.py install""".format(paths))
                print(titles.done.format('eXpliot'))

            print(titles.note_tools2.format('eXpliot','efconsole'))

        print(titles.readmore.format('eXpliot','http://bit.ly/2mQTkWN'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def rootos(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'rootOS')
            print(titles.installing.format('rootOS'))
            system("cd {} && sudo git clone https://github.com/thehappydinoa/rootOS".format(paths))
            print(titles.done.format('rootOS'))
            print(titles.note_tools.format('rootOS','python2 rootos.py'))

        print(titles.readmore.format('rootOS','http://bit.ly/2GvBSSl'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def pure_blood(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'Pure Blood')
            print(titles.installing.format('Pure Blood'))
            system("""cd {} && sudo git clone https://github.com/cr4shcod3/pureblood
            cd pureblood && sudo pip2 install -r requirements.txt""".format(paths))
            print(titles.done.format('Pure Blood'))
            print(titles.note_tools.format('Pure Blood','python2 pureblood.py'))

        print(titles.readmore.format('Pure Blood','http://bit.ly/2LOFfIh'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def termineter(titles):
    try:
        if name == 'nt':
            python3 = str(input(titles.installed_or_not.format('Python 3.7')))
            action(titles,python3)

            if python3[0].upper() == 'Y':
                pass

            elif python3[0].upper() == 'N':
                print(titles.downloading.format('python-3.7.3.exe'))
                download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                print(titles.note_python3)
                system('.\\python-3.7.3.exe')

            elif (python3.upper() == 'HELP' or python3.upper() == 'CHANGELOG' or python3.upper() == 'ABOUT'):
                termineter(titles)

            else:
                print(titles.invalid)
                termineter(titles)

            print(titles.installing.format('Termineter'))
            system("pip install termineter")
            print(titles.done.format('Termineter'))

        else:
            if path.exists('/usr/bin/termineter') == True:
                print(titles.installed.format('Termineter'))

            else:
                print(titles.installing.format('Termineter'))
                system("sudo pip3 install termineter")
                print(titles.done.format('Termineter'))
                
        print(titles.note_tools2.format('Termineter','termineter','Terminal & CMD'))
        print(titles.readmore.format('Termineter','http://bit.ly/2m5btzY'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def autosploit(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'AutoSploit')
            print(titles.installing.format('AutoSploit'))

            if path.exists('/usr/bin/pacman') == True:
                system("""cd {} && sudo git clone https://github.com/NullArray/AutoSploit
                sudo pacman -S metasploit postgresql apache
                cd AutoSploit && sudo pip2 install -r requirements.txt""".format(paths))

            elif path.exists('/usr/bin/apt') == True:
                system("""cd {} && sudo git clone https://github.com/NullArray/AutoSploit
                cd AutoSploit && sudo pip2 install -r requirements.txt
                sudo bash install.sh""".format(paths))

            print(titles.done.format('AutoSploit'))
            print(titles.note_tools.format('AutoSploit','python2 autosploit.py'))

        print(titles.readmore.format('AutoSploit','http://bit.ly/2xxvTu3'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def smod(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'smod')
            print(titles.installing.format('smod'))
            system("""cd {} && sudo git clone https://github.com/Exploit-install/smod && sudo pip2 install scapy""".format(paths))
            print(titles.done.format('smod'))
            print(titles.note_tools.format('smod','python2 smod.py'))

        print(titles.readmore.format('smod','http://bit.ly/2JS3C6f'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def thefatrat(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'TheFatRat')
            print(titles.installing.fomat('TheFatRat'))
            system("""cd {} && https://github.com/Screetsec/TheFatRat
            cd TheFatRat && sudo bash setup.sh""".format(paths))
            print(titles.done.format('TheFatRat'))
            print(titles.note_tools.format('TheFatRat','bash fatrat'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
                print(titles.wsl)

            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('TheFatRat','http://bit.ly/2BDa6PV'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def exploit_pack(titles):
    try:
        if name == 'nt':
            java = str(input(titles.installed_or_not.format('Java'))).strip()
            action(titles,java)

            if java[0].upper() == 'Y':
                pass

            elif java[0].upper() == 'N':
                print(titles.downloading.format('jre-8u211-windows-i586-iftw.exe'))
                download("https://sdlc-esd.oracle.com/ESD6/JSCDL/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-windows-i586-iftw.exe?GroupName=JSC&FilePath=/ESD6/JSCDL/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-windows-i586-iftw.exe&BHost=javadl.sun.com&File=jre-8u211-windows-i586-iftw.exe&AuthParam=1559705933_85bc6ea5c1eb928eabbe3a7733aca1df&ext=.exe")
                system(".\\jre-8u211-windows-i586-iftw.exe")

            elif (java.upper() == 'HELP' or java.upper() == 'CHANGELOG' or java.upper() == 'ABOUT'):
                exploit_pack(titles)

            else:
                print(titles.invalid)
                exploit_pack(titles)

            print(titles.downloading.format('exploitpack.zip'))
            download('https://github.com/ExploitPackBinaries/ExploitPack/raw/master/exploitpack.zip')
            print(titles.note_exploit_pack)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Exploit Pack')
                print(titles.installing.format('Exploit Pack'))
                
                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -sS jdk-openjdk jre-openjdk ")

                elif path.exists('/usr/bin/apt') == True:
                    system("""sudo add-apt-repository ppa:linuxuprising/java
                    sudo apt update && sudo apt install oracle-java11-installer""")

                system("""cd {} && https://github.com/ExploitPackBinaries/ExploitPack/raw/master/exploitpack.zip
                unzip exploitpack.zip -d exploitpack""".format(paths))
                print(titles.done.format('Exploit Pack'))
                print(titles.note_tools.format('Exploit Pack','sudo bash RunExploitPack.sh'))

        print(titles.readmore.format('Exploit Pack','http://bit.ly/2KWeeOe'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def mimikittenz(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            powershell = str(input(titles.installed_or_not.format('PowerShell'))).strip()
            action(titles,powershell)

            if (git[0].upper() == 'Y' and powershell[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif powershell[0].upper(titles) == 'N':
                    print(titles.note_powershell)

                elif (git.upper() == 'HELP' or powershell.upper() == 'HELP'):
                    mimikittenz(titles)

                elif (git.upper() == 'CHANGELOG' or powershell.upper() == 'CHANGELOG'):
                    mimikittenz(titles)

                elif (git.upper() == 'ABOUT' or powershell.upper() == 'ABOUT'):
                    mimikittenz(titles)

                else:
                    print(titles.invalid)
                    mimikittenz(titles)

            print(titles.installing.format('mimikittenz'))
            system("cd C:\\ && git clone https://github.com/putterpanda/mimikittenz")
            print(titles.done.format('mimikittenz'))
            print(titles.note_tools.format('mimikittenz','.\\Invoke-mimikittenz.ps1'))

        else:
            print(titles.only_compatible.format('PowerShell'))

        print(titles.readmore.format('mimikittenz','http://bit.ly/2FY0TD6'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def ezsploit(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'ezsploit')
                print(titles.installing.format('ezsploit'))
                metasploit(titles)
                system("cd {} && sudo git clone https://github.com/rand0m1ze/ezsploit".format(paths))
                print(titles.done.format('ezsploit'))
                print(titles.note_tools.format('ezsploit','ezsploit.sh'))

        print(titles.readmore.format('ezsploit','http://bit.ly/2EO62B8'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def auto_root_exploit(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'Auto-Exploit-Root')
            print(titles.installing.format('Auto-Exploit-Root'))
            system("cd {} && sudo git clone https://github.com/nilotpalbiswas/Auto-Root-Exploit".format(paths))
            print(titles.done.format('Auto-Root-Exploit'))
            print(titles.note_tools.format('Auto-Root-Exploit','bash autoroot.sh'))

        print(titles.readmore.format('Auto-Root-Exploit','http://bit.ly/2UqdvsV'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def ahmyth_android_rat(titles):
    try:
        if name == 'nt':
            java = str(input(titles.installed_or_not.format('Java'))).strip()
            action(titles,java)

            if java[0].upper() == 'Y':
                pass

            elif java[0].upper() == 'N':
                print(titles.downloading.format('jre-8u211-windows-i586-iftw.exe'))
                download("https://sdlc-esd.oracle.com/ESD6/JSCDL/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-windows-i586-iftw.exe?GroupName=JSC&FilePath=/ESD6/JSCDL/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-windows-i586-iftw.exe&BHost=javadl.sun.com&File=jre-8u211-windows-i586-iftw.exe&AuthParam=1559705933_85bc6ea5c1eb928eabbe3a7733aca1df&ext=.exe")
                system(".\\jre-8u211-windows-i586-iftw.exe")

            elif (java.upper() == 'HELP' or java.upper() == 'CHANGELOG' or java.upper() == 'ABOUT'):
                ahmyth_android_rat(titles)

            else:
                print(titles.invalid)
                ahmyth_android_rat(titles)

            print(titles.installing.format('AhMyth-Android-RAT'))
            print(titles.downloading.format('AhMyth_Win32.exe'))
            download('https://github.com/AhMyth/AhMyth-Android-RAT/releases/download/v1.0-beta.1/AhMyth_Win32.exe')
            system('.\\AhMyth_Win32.exe')

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/pacman') == True:
                    paths = the_path(titles,'AhMyth-Android-RAT')
                    print(titles.installing.format('AhMyth-Android-RAT'))
                    system("""sudo pacman -sS jdk-openjdk jre-openjdk electron
                    cd {} && sudo git clone https://github.com/AhMyth/AhMyth-Android-RAT""".format(paths))
                    print(titles.done.format('AhMyth-Android-RAT'))
                    print(titles.note_tools2.format('AhMyth-Android-RAT','sudo nmp start','AhMyth-Android-RAT/AhMyth-Server'))


                elif path.exists('/usr/bin/apt') == True:
                    print(titles.installing.format('AhMyth-Android-RAT'))
                    system("""sudo add-apt-repository ppa:linuxuprising/java
                    sudo apt update && sudo apt install oracle-java11-installer""")
                    system("wget https://github.com/AhMyth/AhMyth-Android-RAT/releases/download/v1.0-beta.1/AhMyth_linux32.deb && sudo dpkg -i AhMyth_linux32.deb")
                    print(titles.done.format('AhMyth-Android-RAT'))
                    print(titles.note_tools2.format('AhMyth-Android-RAT','sudo ahmyth','Terminal'))

        print(titles.readmore.format('AhMyth-Android-RAT','http://bit.ly/2YuBQAm'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def exploit_framework(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    exploit_framework(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    exploit_framework(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    exploit_framework(titles)

                else:
                    print(titles.invalid)
                    exploit_framework(titles)

            print(titles.installing.format('Exploit-Framework'))
            system("cd C:\\ && git clone https://github.com/WangYihang/Exploit-Framework")

        else:
            paths = the_path(titles,'Exploit-Framework')
            print(titles.installing.format('Exploit-Framework'))
            system("cd {} && sudo git clone https://github.com/WangYihang/Exploit-Framework".format(paths))
            
        print(titles.done.format('Exploit-Framework'))
        print(titles.note_tools.format('Exploit-Framework', 'python2 framework.py'))
        print(titles.readmore.format('Exploit-Framework','http://bit.ly/2L0UEjN'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def winroothelper(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            powershell = str(input(titles.installed_or_not.format('PowerShell'))).strip()
            action(titles,powershell)

            if (git[0].upper() == 'Y' and powershell[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif powershell[0].upper(titles) == 'N':
                    print(titles.note_powershell)

                elif (git.upper() == 'HELP' or powershell.upper() == 'HELP'):
                    winroothelper(titles)

                elif (git.upper() == 'CHANGELOG' or powershell.upper() == 'CHANGELOG'):
                    winroothelper(titles)

                elif (git.upper() == 'ABOUT' or powershell.upper() == 'ABOUT'):
                    winroothelper(titles)

                else:
                    print(titles.invalid)
                    winroothelper(titles)

            print(titles.installing.format('WinRootHelper'))
            system("cd C:\\ && git clone https://github.com/GreySec-Security-Forums/WinRootHelper")
            print(titles.done.format('WinRootHelper'))
            print(titles.note_tools.format('WinRootHelper','.\\winroot.ps1'))

        else:
            print(titles.only_compatible.format('PowerShell'))

        print(titles.readmore.format('WinRootHelper','http://bit.ly/2Uu0BKG'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def metasploit(titles):
    try:
        if name == 'nt':
            print(titles.installing.format('Metasploit Framework'))
            print(titles.downloading.format('metasploitframework-latest.msi'))
            download('https://windows.metasploit.com/metasploitframework-latest.msi')
            system(".\\metasploitframework-latest.msi")
            print(titles.done.format('Metasploit Framework'))
            print(titles.note_tools.format('Metasploit Framework','"C:\\metasploit\\console.bat"','CMD'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                if path.exists('/usr/bin/msfconsole') == True:
                    print(titles.installed.format('Metasploit Framework'))

                else:
                    print(titles.installing.format('Metasploit Framework'))

                    if path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S metasploit")

                    elif path.exists('/usr/bin/apt') == True:
                        system("""sudo curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
                        chmod 755 msfinstall && sudo ./msfinstall""")
                        
                    print(titles.done.format('Metasploit Framework'))

                print(titles.note_tools.format('Metasploit Framework','sudo msfconsole','Terminal'))

        print(titles.readmore.format('Metasploit Framework','http://bit.ly/2JkoOl9'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def zerodoor(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'ZeroDoor')
                print(titles.installing.format('ZeroDoor'))

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S gcc && git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64-gcc && makepkg -si")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install gcc mingw-w64")

                system("cd {} && sudo git clone https://github.com/Souhardya/Zerodoor".format(paths))
                print(titles.done.format('ZeroDoor'))
                print(titles.note_tools.format('ZeroDoor','python2 zerodoor.py'))

        print(titles.readmore.format('ZeroDoor','http://bit.ly/2LSjhnR'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def terminator(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Terminator')
                print(titles.installing.format('Terminator'))
                metasploit(titles)
                system("cd {} && sudo git clone https://github.com/MohamedNourTN/Terminator".format(paths))
                print(titles.done.format('Terminator'))
                print(titles.note_tools.format('Terminator','python2 terminator.py'))

        print(titles.readmore.format('Terminator','http://bit.ly/2vcD5If'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def winpayloads(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'WinPayloads')
                print(titles.installing.format('WinPayloads'))
                metasploit(titles)

                if path.exists('/usr/bin/pacman') == True:
                    system("""sudo pacman -S wine python2-crypto unzip curl wget libwbclient
                    sudo pip2 install requests netifaces blessed pyasn1
                    sudo pip2 install --force-reinstall prompt-toolkit==1.0.15""")

                system("""cd {} && sudo git clone https://github.com/nccgroup/Winpayloads
                cd Winpayloads && sudo bash setup.sh""".format(paths))
                print(titles.done.format('WinPayloads'))
                print(titles.note_tools.format('WinPayloads','sudo python2 WinPayloads.py'))

        print(titles.readmore.format('WinPayloads','http://bit.ly/2MkvmT7'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def saint(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'sAINT')
                print(titles.installing.format('sAINT'))

                if path.exists('/usr/bin/apt') == True:
                    system("""sudo add-apt-repository ppa:linuxuprising/java
                    sudo apt update && sudo apt install oracle-java8-installer
                    sudo apt install maven zlib1g-dev libncurses5-dev lib32z1 lib32ncurses6 -y""")

                elif path.exists('/usr/bin/apt') == True:
                    system("""sudo pacman -S jre8-openjdk jdk8-openjdk maven zlib ncurses lib32-ncurses""")

                system("""cd {} && sudo git clone https://github.com/tiagorlampert/sAINT
                cd sAINT && sudo bash configure.sh""".format(paths))
                print(titles.done.format('sAINT'))
                print(titles.note_tools.format('sAINT','java -jar sAINT.jar'))

        print(titles.readmore.format('sAINT','http://bit.ly/2LPtpcV'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def beelogger(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'BeeLogger')
                print(titles.installing.format('BeeLogger'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""sudo pacman -S wine""")

                system("""cd {} && sudo git clone https://github.com/4w4k3/BeeLogger
                cd BeeLogger && sudo bash install.sh""".format(paths))
                print(titles.done.formar('BeeLogger'))
                print(titles.note_tools.format('BeeLogger','python2 bee.py'))

        print(titles.readmore.format('BeeLogger','http://bit.ly/2LqJyJF'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def hacktheworld(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'HackTheWorld')
                print(titles.installing.format('HackTheWorld'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64 && makepkg -si
                    sudo pacman -S wine metasploit
                    cd {} && sudo git clone https://github.com/stormshadow07/HackTheWorld""".format(paths))

                elif path.exists('/usr/bin/apt') == True:
                    system("""cd {} && sudo git clone https://github.com/stormshadow07/HackTheWorld
                    cd HackTheWorld && sudo bash install.sh""".format(paths))

                print(titles.done.format('HackTheWorld'))
                print(titles.note_tools.format('HackTheWorld','python2 HackTheWorld.py'))

        print(titles.readmore.format('HackTheWorld','http://bit.ly/2JhzBfZ'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def hatkey(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)
            powershell = str(input(titles.installed_or_not.format('PowerShell'))).strip()
            action(titles,powershell)

            if (git.upper() == 'Y' and python2.upper() == 'Y' and powershell.upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif powershell.upper() == 'N':
                    print(titles.note_powershell)

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP' or powershell.upper() == 'HELP'):
                    hatkey(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG' or powershell.upper() == 'CHANGELOG'):
                    hatkey(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT' or powershell.upper() == 'ABOUT'):
                    hatkey(titles)

                else:
                    print(titles.invalid)
                    hatkey(titles)

            system("cd C:\\ && git clone https://github.com/Naayouu/Hatkey")
            print(titles.done.format('HatKey'))
            print(titles.note_tools.format('HatKey','python2 HatKey.py'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/dnf') == False and path.exists('/usr/bin/yum') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'HatKey')
                print(titles.installing.format('HatKey'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install powershell")

                elif path.exists('/usr/bin/yum') == True:
                    system("sudo yum install powershell")

                elif path.exists('/usr/bin/dnf') == True:
                    system("sudo dnf install powershell")

                elif path.exists('/usr/bin/pacman') == True:
                    system("git clone https://aur.archlinux.org/powershell.git && cd powershell && makepkg -si")

                system("cd {} && sudo git clone https://github.com/Naayouu/Hatkey".format(paths))
                print(titles.done.format('HatKey'))
                print(titles.note_tools.format('HatKey','python2 HatKey.py'))

        print(titles.readmore.format('HatKey','http://bit.ly/2HOZbDZ'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def trolo(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == True and path.exists('/usr/bin/pacman') == True):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'trolo')
                print(titles.installing.format('trolo'))
                metasploit(titles)

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install powershell")

                elif path.exists('/usr/bin/pacman') == True:
                    system("git clone https://aur.archlinux.org/powershell.git && cd powershell && makepkg -si")

                system("cd {} && sudo git clone https://github.com/b3rito/trolo".format(paths))
                print(titles.done.format('trolo'))
                print(titles.note_tools.format('trolo','bash trolo.sh'))

        print(titles.readmore.format('trolo','http://bit.ly/2Jj37Sj'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def getwin(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == True and path.exists('/usr/bin/pacman') == True):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'GetWin')
                print(titles.installing.format('GetWin'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""sudo pacman -S netcat php libssh2 openssh
                    git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64-gcc && makepkg -si""")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install netcat php ssh mingw-w64")

                system("cd {} && sudo git clone https://github.com/thelinuxchoice/getwin".format(paths))
                print(titles.done.format('GetWin'))
                print(titles.note_tools.format('GetWin','bash getwin.sh'))

        print(titles.readmore.format('GetWin','http://bit.ly/2R0reH5'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def dkmc(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == True and path.exists('/usr/bin/pacman') == True):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'DKMC')
                print(titles.installing.format('DKMC'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install powershell")

                elif path.exists('/usr/bin/pacman') == True:
                    system("git clone https://aur.archlinux.org/powershell.git && cd powershell && makepkg -si")

                system("cd {} && sudo git clone https://github.com/Mr-Un1k0d3r/DKMC && cd DKMC && sudo mkdir output".format(paths))
                print(titles.done.format('DKMC'))
                print(titles.note_tools.format('DKMC','python2 dkmc.py'))

        print(titles.readmore.format('DKMC','http://bit.ly/2IybKpD'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def parat(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git.upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2.upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    parat(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    parat(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    parat(titles)

                else:
                    print(titles.invalid)
                    parat(titles)

            print(titles.installing.format('Parat'))
            system("cd C:\\ && git clone https://github.com/fadinglr/Parat")

        else:
            paths = the_path(titles,'Parat')
            print(titles.installing.format('Parat'))
            system("cd {} && sudo git clone https://github.com/fadinglr/Parat".format(paths))

        print(titles.done.format('Parat'))
        print(titles.note_tools.format('Parat','python2 main.py'))
        print(titles.readmore.format('Parat','http://bit.ly/2wa5LC6'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def mkvenom(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'mkvenom')
                print(titles.installing.format('mkvenom'))
                metasploit(titles)
                system("cd {} && sudo git clone https://github.com/phraxoid/mkvenom".format(paths))
                print(titles.done.format('mkvenom'))
                print(titles.note_tools.format('mkvenom','bash mkvenom.sh'))

        print(titles.readmore.format('mkvenom','http://bit.ly/2MoYrg5'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def venom(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'venom')
                print(titles.installing.format('venom'))
                metasploit(titles)

                if path.exists('/usr/bin/apt') == True:
                    system("""sudo apt install wine gcc mingw32
                    git clone https://gitlab.com/kalilinux/packages/shellter && cd shellter/debian && sudo bash install""")

                elif path.exists('/usr/bin/pacman') == True:
                    system("""wget https://raw.githubusercontent.com/BlackArch/blackarch/37ad245e9b30abfc7fcc7e636c1df3675b134dee/packages/shellter/PKGBUILD && makepkg -si
                    git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64-gcc && makepkg -si
                    sudo pacman -S wine gcc""")

                system("cd {} && sudo git clone https://github.com/r00t-3xp10it/venom".format(paths))
                print(titles.done.format('venom'))
                print(titles.note_tools.format('venom','sudo bash venom.sh'))

        print(titles.readmore.format('venom','http://bit.ly/2MVHTc0'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def cloak(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Cloak')
                metasploit(titles)
                system("cd {} && sudo git clone https://github.com/s0md3v/Cloak".format(paths))
                print(titles.done.format('Cloak'))
                print(titles.note_tools.format('Cloak','python3 cloak.py'))

        print(titles.readmore.format('Cloak','http://bit.ly/2OQ2tLb'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def avoid(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'Metasploit AV Evasion')
                print(titles.installing.format('Metasploit AV Evasion'))
                metasploit(titles)

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S gcc && git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64-gcc && makepkg -si")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install gcc mingw-w64")

                system("cd {} && sudo git clone https://github.com/nccgroup/metasploitavevasion".format(paths))
                print(titles.done.format('Metasploit AV Evasion'))
                print(titles.note_tools.format('Metasploit AV Evasion','bash avoid.sh'))

        print(titles.readmore.format('Metasploit AV Evasion','http://bit.ly/2Kn3Q1p'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def avet(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(titles.unknow_distro)

            else:
                paths = the_path(titles,'AVET')
                print(titles.installing.format('AVET'))
                metasploit(titles)

                if path.exists('/usr/bin/pacman') == True:
                    system("""sudo pacman -S gcc wine && wget https://downloads.sourceforge.net/project/tdm-gcc/TDM-GCC%20Installer/tdm64-gcc-5.1.0-2.exe
                    sudo wine tdm64-gcc-5.1.0-2.exe && sudo rm tdm64-gcc-5.1.0-2.exe
                    cd {} && sudo git clone https://github.com/govolution/avet""".format(paths))

                elif path.exists('/usr/bin/apt') == True:
                    system("""cd {} && sudo git clone https://github.com/govolution/avet
                    cd avet && sudo bash setup.sh""".format(paths))

                print(titles.done.format('AVET'))
                print(titles.note_tools.format('AVET','python3 avet_fabric.py'))

        print(titles.readmore.format('AVET','http://bit.ly/2TltIE3'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def nxcrypt(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    nxcrypt(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    nxcrypt(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    nxcrypt(titles)

                else:
                    print(titles.invalid)
                    nxcrypt(titles)

            print(titles.installing.format('NXcrypt'))
            system("cd C:\\ && git clone https://github.com/Hadi999/NXcrypt")

        else:
            paths = the_path(titles,'NXcrypt')
            print(titles.installing.format('NXcrypt'))
            system("cd {} && sudo git clone https://github.com/Hadi999/NXcrypt".format(paths))

        print(titles.done.format('NXcrypt'))
        print(titles.note_tools.format('NXcrypt','python2 nxcrypt.py'))
        print(titles.readmore.format('NXcrypt','http://bit.ly/2xcyR6P'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def slowloris(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            python3 = str(input(titles.installed_or_not.format('Python 3.7'))).strip()
            action(titles,python3)

            if python3[0].upper() == 'Y':
                pass
                    
            elif python3[0].upper() == 'N':
                print(titles.downloading.format('python-3.7.3.exe'))
                download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                print(titles.note_python3)
                system('.\\python-3.7.3.exe')

            elif (python3.upper() == 'HELP' or python3.upper() == 'ABOUT' or python3.upper() == 'CHANGELOG'):
                slowloris(titles)

            else:
                print(titles.invalid)
                slowloris(titles)

            print(titles.installing.format("SlowLoris"))
            system("pip3 install slowloris")

        else:
            print(titles.installing.format("SlowLoris"))
            system("sudo pip3 install slowloris")

        print(titles.done.format('SlowLoris'))
        print(titles.note_tools2.format('SlowLoris','slowloris','Terminal & CMD'))
        print(titles.readmore.format('SlowLoris','http://bit.ly/2VipeKA'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def zambie(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'ZAmbIE')
            print(titles.installing.format('ZAmbIE'))
            system("""cd {} sudo git clone https://github.com/zanyarjamal/zambie
            cd zambie && sudo bash Installer.sh""".format(paths))
            print(titles.done.format('ZAmbIE'))
            print(titles.note_tools.format('ZAmbIE','python zambie.py'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
                print(titles.wsl)

            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('ZAmbIE','http://bit.ly/2JymfeZ'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def ufonet(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            paths = the_path(titles,'UFONet')
            print(titles.installing.format('UFONet'))
            system("""cd {} && sudo git clone https://github.com/epsylon/ufonet
            cd ufonet && sudo python2 setup.py install""".format(paths))
            print(titles.done.format('UFONet'))
            print(titles.note_tools.format('UFONet','python2 ufonet'))

        print(titles.readmore.format('UFONet','http://bit.ly/2C8i1YT'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def memcrashed(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python3 = str(input(titles.installed_or_not.format('Python 3.7'))).strip()
            action(titles,python3)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python3[0].upper() == 'N':
                    print(titles.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(titles.note_python3)
                    system('.\\python-3.7.3.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP'):
                    memcrashed(titles)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG'):
                    memcrashed(titles)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT'):
                    memcrashed(titles)

                else:
                    print(titles.invalid)
                    memcrashed(titles)

            print(titles.installing.format('Memcrashed-DDoS-Exploit'))
            system("""cd C:\\ && git clone https://github.com/649/Memcrashed-DDoS-Exploit Memcrashed
            cd Memcrashed && pip install -r requirements.txt""")

        else:
            paths = the_path(titles,'Memcrashed-DDoS-Exploit')
            print(titles.installing.format('Memcrashed-DDoS-Exploit'))
            system("""cd {} && git clone https://github.com/649/Memcrashed-DDoS-Exploit Memcrashed
            cd Memcrashed && pip install -r requirements.txt""".format(paths))

        print(titles.done.format('Memcrashed-DDoS-Exploit'))
        print(titles.note_tools.format('Memcrashed-DDoS-Exploit','python3 Memcrashed.py'))
        print(titles.readmore.format('Memcrashed-DDoS-Exploit','http://bit.ly/2NVzF42'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def fsociety(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if path.exists('/usr/bin/pacman') == True:
                paths = the_path(titles,'Fsociety')
                print(titles.installing.format)
                system("cd {} && sudo git clone https://github.com/Manisso/fsociety".format(paths))
                print(titles.done.format('Fsociety'))
                print(titles.note_tools.format('Fsociety','python2 fsociety.py'))

            else:
                if path.exists('/usr/local/bin/fsociety') == True:
                    print(titles.installed.format('Fsociety'))

                else:
                    paths = the_path(titles,'Fsociety')
                    print(titles.installing.format)
                    system("cd {} && sudo git clone https://github.com/Manisso/fsociety".format(paths))
                    print(titles.done.format('Fsociety'))
                    
                print(titles.note_tools2.format('Fsociety','fsociety','Terminal'))

        print(titles.readmore.format('Fsociety','http://bit.ly/2mJIRwi'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def malicious(titles):
    try:
        if name == 'nt':
            print(titles.note_saved)
            git = str(input(titles.installed_or_not.format('Git-scm'))).strip()
            action(titles,git)
            python2 = str(input(titles.installed_or_not.format('Python 2.7'))).strip()
            action(titles,python2)
            ruby = str(input(titles.installed_or_not.format('Ruby-lang'))).strip()
            action(titles,ruby)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(titles.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(titles.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(titles.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(titles.note_python2)
                    system('.\\python-2.7.16.msi')

                elif ruby[0].upper() == 'N':
                    print(titles.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(titles.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    malicious(titles)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    malicious(titles)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    malicious(titles)

                else:
                    print(titles.invalid)
                    malicious(titles)

            print(titles.installing.format('Malicious'))
            system("""cd C:\\ && git clone https://github.com/Hider5/Malicious
            cd Malicious && gem install lolcat && pip install -r requirements.txt""")

        else:
            paths = the_path(titles,'Malicious')
            print(titles.installing.format('Malicious'))

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install ruby")

            elif path.exists('/usr/bin/apt'):
                system("sudo pacman -S ruby")

            system("""cd {} && git clone https://github.com/Hider5/Malicious
            cd Malicious && gem install lolcat && pip install -r requirements.txt""".format(paths))

        print(titles.done.format('Malicious'))
        print(titles.note_tools.format('Malicious','python2 malicious.py'))
        print(titles.readmore.format('Malicious','http://bit.ly/2VHtLKP'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def tool_x(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'Tool-X')
            print(titles.installing.format('Tool-X'))
            system("""cd {} && sudo git clone https://github.com/Rajkumrdusad/Tool-X
            cd Tool-X && sudo bash install.aex""".format(paths))
            print(titles.done.format('Tool-X'))
            print(titles.note_tools2.format('Tool-X','Tool-X','Terminal'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
                print(titles.wsl)

            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('Tool-X','http://bit.ly/2ITHrfN'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def katoolin(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            if path.exists('/usr/bin/katoolin') == True:
                print(titles.installed.format('Katoolin'))

            else:
                paths = the_path(titles,'Katoolin')
                print(titles.installing.format('Katoolin'))
                system("""cd {} && sudo git clone https://github.com/LionSec/katoolin
                cd katoolin && sudo cp katoolin.py /usr/bin/katoolin
                sudo chmod +x /usr/bin/katoolin""".format(paths))
                print(titles.done.format('Katoolin'))

            print(titles.note_tools2.format('Katoolin','sudo katoolin','Terminal'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
                print(titles.wsl)

            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('Katoolin','http://bit.ly/2EXOU8G'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def intrec_pack(titles):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(titles,'IntRec-Pack')
            print(titles.installing.format('IntRec-Pack'))
            system("cd {} && sudo git clone https://github.com/NullArray/IntRec-Pack".format(paths))
            print(titles.done.format('IntRec-Pack'))
            print(titles.note_tools.format('IntRec-Pack','sudo bash intrec.sh'))

        else:
            if name == 'nt':
                print(titles.doesnt_support_windows)
                print(titles.wsl)

            else:
                print(titles.run_well.format('Debian'))

        print(titles.readmore.format('IntRec-Pack','http://bit.ly/2LI9vDL'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()


def ptf(titles):
    try:
        if name == 'nt':
            print(titles.doesnt_support_windows)
            print(titles.wsl)

        else:
            if path.exists('/usr/local/bin/ptf') == True:
                print(titles.installed.format('The PenTesters Framework'))

            else:
                paths = the_path(titles,'The PenTesters Framework')
                print(titles.installing.format('The PenTesters Framework'))
                system("""cd {} && sudo git clone https://github.com/trustedsec/ptf
                cd ptf && sudo python2 ptf""".format(paths))
                print(titles.done.format('The PenTesters Framework'))

            print(titles.note_tools2.format('The PenTesters Framework','sudo ptf','Terminal'))

        print(titles.readmore.format('The PenTesters Framework','http://bit.ly/2K3rsYS'))

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
