#!/usr/bin/python3
exit
import os
from os import system, name, path
from titles import english
from tools import *
from banner import *
import time
import sys
print("Yikebox loading:")


#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[loading.   ■□□□□□□□□□□□□□]","[loading..  ■■□□□□□□□□□□□□]", "[loading... ■■■□□□□□□□□□□□]", "[loading.   ■■■■□□□□□□□□□□]", "[loading..  ■■■■■□□□□□□□□□]", "[loading... ■■■■■■□□□□□□□□]", "[loading.   ■■■■■■■□□□□□□□]", "[loading..  ■■■■■■■■□□□□□□]", "[loading... ■■■■■■■■■□□□□□]", "[loading.   ■■■■■■■■■■□□□□]", "[loading.   ■■■■■■■■■■■□□□]", "[loading.   ■■■■■■■■■■■■□□]", "[loading.   ■■■■■■■■■■■■■□]", "[DONE!      ■■■■■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.7)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
print(
'''
                         __________
                      .~#########%%;~.
                     /############%%;`\
                    /######/~\/~\%%;,;,\
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
 X# \.X        @#%,.@                  @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, "# #X            @#%,.@          @#%,.@            X ##
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`"
    . ";"                @#%.@#%,.@                ;"` ' .
      '                    @#%,.@                   ,.
      ` ,                @#%,.@  @@                `
                          @@@  @@@                  .
  _____________________________________________________
'''
    )
os.system('cls')


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def continue_or_not(titles):
    try:
        choice = str(input(titles.continue_or_not)).strip()
        action(titles,choice)
        
        if choice[0].upper() == 'Y':
            clear()
            choose_lang(titles)
        elif choice[0].upper() == 'N':
            print(titles.exiting)
            exit()
        elif (choice.upper() == 'HELP' or choice.upper() == 'CHANGELOG' or choice.upper() == 'ABOUT'):
            continue_or_not(titles)
        else:
            print(titles.invalid)
            continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        print(titles.invalid)
        continue_or_not(titles)

def choose_lang(titles):
    try:
        print(titles.titles_list)
        choice = str(input(titles.choose_titles.format(2))).strip()
        action(titles,choice)

        if choice == '0':
            exit()
        elif choice == 'Sakura95':
            clear()
            Yikebox_banner(english)
            home_page(english)
        elif (choice.upper() == "HELP" or choice.upper() ==  "CHANGELOG" or choice.upper() == "ABOUT"):
            choose_lang(titles)
        else:
            print(titles.invalid)
            choose_lang(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        print(titles.invalid)
        choose_lang(titles)

def home_page(titles):
    try:
        print(titles.home_page)
        choice = str(input(titles.choose_category.format(12))).strip()
        clear()
        action(titles,choice)

        if choice == '0':
            print(titles.exiting)
            exit()
        elif choice == '1':
            info_gathering(titles)
        elif choice == '2':
            vulner_analysis(titles)
        elif choice == '3':
            passwd_attack(titles)
        elif choice == '4':
            wireless_attack(titles)
        elif choice == '5':
            web_apps(titles)
        elif choice == '6':
            exploit_tools(titles)
        elif choice == '7':
            sniff_spoof(titles)
        elif choice == '8':
            ddos_tools(titles)
        elif choice == '9':
            malware_bypass(titles)
        elif choice == '10':
            downloader_installer(titles)
        elif (choice.upper() == "HELP" or choice.upper() ==  "CHANGELOG" or choice.upper() == "ABOUT"):
            home_page(titles)
        else:
            print(titles.invalid)
            home_page(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        home_page(titles)

def info_gathering(titles):
    try:
        print(titles.info_gathering)
        tool = str(input(titles.which_tools.format(35))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_info_garther.format('BillCipher'))
            billcipher_banner(titles)
            billcipher(titles)

        elif tool == '2':
            print(titles.category_info_garther.format('Leaked'))
            leaked_banner(titles)
            leaked(titles)

        elif tool == '3':
            print(titles.category_info_garther.format('Devploit'))
            devploit_banner(titles)
            devploit(titles)

        elif tool == '4':
            print(titles.category_info_garther.format('Gorecon'))
            gorecon_banner(titles)
            gorecon(titles)

        elif tool == '5':
            print(titles.category_info_garther.format('Dracnmap'))
            dracnmap_banner(titles)
            dracnmap(titles)

        elif tool == '6':
            print(titles.category_info_garther.format('Nmap'))
            nmap_banner(titles)
            nmap(titles)

        elif tool == '7':
            print(titles.category_info_garther.format('Sublist3r'))
            sublist3r_banner(titles)
            sublist3r(titles)

        elif tool == '8':
            print(titles.category_info_garther.format('SSLScan'))
            sslscan_banner(titles)
            sslscan(titles)

        elif tool == '9':
            print(titles.category_info_garther.format('DNSMaper'))
            dnsmaper_banner(titles)
            dnsmaper(titles)

        elif tool == '10':
            print(titles.category_info_garther.format('ShodanHat'))
            shondanhat_banner(titles)
            shodanhat(titles)

        elif tool == '11':
            print(titles.category_info_garther.format('HatCloud'))
            hatcloud_banner(titles)
            hatcloud(titles)

        elif tool == '12':
            print(titles.category_info_garther.format('A2SV'))
            a2sv_banner(titles)
            a2sv(titles)

        elif tool == '13':
            print(titles.category_info_garther.format('Sub6'))
            sub6_banner(titles)
            sub6(titles)

        elif tool == '14':
            print(titles.category_info_garther.format('Masscan'))
            masscan_banner(titles)
            masscan(titles)

        elif tool == '15':
            print(titles.category_info_garther.format('dnsmap'))
            dnsmap_banner(titles)
            dnsmap(titles)

        elif tool == '16':
            print(titles.category_info_garther.format('InfoSploit'))
            infosploit_banner(titles)
            infosploit(titles)

        elif tool == '17':
            print(titles.category_info_garther.format('Infoga'))
            infoga_banner(titles)
            infoga(titles)

        elif tool == '18':
            print(titles.category_info_garther.format('HTTrack'))
            httrack_banner(titles)
            httrack(titles)

        elif tool == '19':
            print(titles.category_info_garther.format('APT2'))
            apt2_banner(titles)
            apt2(titles)

        elif tool == '20':
            print(titles.category_info_garther.format('InSpy'))
            inspy_banner(titles)
            inspy(titles)

        elif tool == '21':
            print(titles.category_info_garther.format('SEToolkit'))
            setoolkit_banner(titles)
            setoolkit(titles)

        elif tool == '22':
            print(titles.category_info_garther.format('PhishX'))
            phishx_banner(titles)
            phishx(titles)

        elif tool == '23':
            print(titles.category_info_garther.format('PhisherMan'))
            phisherman_banner(titles)
            phisherman(titles)

        elif tool == '24':
            print(titles.category_info_garther.format('Aron'))
            aron_banner(titles)
            aron(titles)

        elif tool == '25':
            print(titles.category_info_garther.format('Evilginx 2'))
            evilginx2_banner(titles)
            evilginx2(titles)

        elif tool == '26':
            print(titles.category_info_garther.format('Infinity'))
            infinity_banner(titles)
            infinity(titles)

        elif tool == '27':
            print(titles.category_info_garther.format('CredSniper'))
            credsniper_banner(titles)
            credsniper(titles)

        elif tool == '28':
            print(titles.category_info_garther.format('Striker'))
            striker_banner(titles)
            striker(titles)

        elif tool == '29':
            print(titles.category_info_garther.format('WAScan'))
            wascan_banner(titles)
            wascan(titles)

        elif tool == '30':
            print(titles.category_info_garther.format('Ghost Phisher'))
            ghost_phisher_banner(titles)
            ghost_phisher(titles)

        elif tool == '31':
            print(titles.category_info_garther.format('Breacher'))
            breacher_banner(titles)
            breacher(titles)

        elif tool == '32':
            print(titles.category_info_garther.format('SiteBroker'))
            sitebroker_banner(titles)
            sitebroker(titles)

        elif tool == '33':
            print(titles.category_info_garther.format('WebSploit'))
            websploit_banner(titles)
            websploit(titles)

        elif tool == '34':
            print(titles.category_info_garther.format('Pure Blood'))
            pure_blood_banner(titles)
            pure_blood(titles)

        elif tool == '35':
            print(titles.category_info_garther.format('Subdomain Analyzer'))
            subdomain_analyzer_banner(titles)
            subdomain_analyzer(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            info_gathering(titles)

        else:
            print(titles.invalid)
            info_gathering(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        info_gathering(titles)

def vulner_analysis(titles):
    try:
        print(titles.vulner_analysis)
        tool = str(input(titles.which_tools.format(26))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_vulner_analysis.format('Nmap'))
            nmap_banner(titles)
            nmap(titles)

        elif tool == '2':
            print(titles.category_vulner_analysis.format('SQLMap'))
            sqlmap_banner(titles)
            sqlmap(titles)

        elif tool == '3':
            print(titles.category_vulner_analysis.format('SQLMate'))
            sqlmate_banner(titles)
            sqlmate(titles)

        elif tool == '4':
            print(titles.category_vulner_analysis.format('SearchSploit'))
            searchsploit_banner(titles)
            searchsploit(titles)

        elif tool == '5':
            print(titles.category_vulner_analysis.format('Brakeman'))
            brakeman_banner(titles)
            brakemen(titles)

        elif tool == '6':
            print(titles.category_vulner_analysis.format('WhatWeb'))
            whatweb_banner(titles)
            whatweb(titles)

        elif tool == '7':
            print(titles.category_vulner_analysis.format('vulscan'))
            vulscan_banner(titles)
            vulscan(titles)

        elif tool == '8':
            print(titles.category_vulner_analysis.format('TakeOver'))
            takeover_banner(titles)
            takeover(titles)

        elif tool == '9':
            print(titles.category_vulner_analysis.format('OpenVAS'))
            openvas_banner(titles)
            openvas(titles)

        elif tool == '10':
            print(titles.category_vulner_analysis.format('Droid-Hunter'))
            droid_hunter_banner(titles)
            droid_hunter(titles)

        elif tool == '11':
            print(titles.category_vulner_analysis.format('PatrOwl'))
            patrowl_banner(titles)
            patrowl(titles)

        elif tool == '12':
            print(titles.category_vulner_analysis.format('Zoom'))
            zoom_banner(titles)
            zoom(titles)

        elif tool == '13':
            print(titles.category_vulner_analysis.format('Vuls'))
            vuls_banner(titles)
            vuls(titles)

        elif tool == '14':
            print(titles.category_vulner_analysis.format('WPSeku'))
            wpseku_banner(titles)
            wpseku(titles)

        elif tool == '15':
            print(titles.category_vulner_analysis.format('WPScan'))
            wpscan_banner(titles)
            wpscan(titles)

        elif tool == '16':
            print(titles.category_vulner_analysis.format('RouterSploit'))
            routersploit_banner(titles)
            routersploit(titles)

        elif tool == '17':
            print(titles.category_vulner_analysis.format('XSStrike'))
            xsstrike_banner(titles)
            xsstrike(titles)

        elif tool == '18':
            print(titles.category_vulner_analysis.format('Striker'))
            striker_banner(titles)
            striker(titles)

        elif tool == '19':
            print(titles.category_vulner_analysis.format('Raptor'))
            raptor_banner(titles)
            raptor(titles)

        elif tool == '20':
            print(titles.category_vulner_analysis.format('XSSer'))
            xsser_banner(titles)
            xsser(titles)

        elif tool == '21':
            print(titles.category_vulner_analysis.format('Breacher'))
            breacher_banner(titles)
            breacher(titles)

        elif tool == '22':
            print(titles.category_vulner_analysis.format('A2SV'))
            a2sv_banner(titles)
            a2sv(titles)

        elif tool == '23':
            print(titles.category_vulner_analysis.format('BadMod'))
            badmod_banner(titles)
            badmod(titles)

        elif tool == '24':
            print(titles.category_vulner_analysis.format('Pure Blood'))
            pure_blood_banner(titles)
            pure_blood(titles)

        elif tool == '25':
            print(titles.category_vulner_analysis.format('Infection Monkey'))
            infection_monkey_banner(titles)
            infection_monkey(titles)

        elif tool == '26':
            print(titles.category_vulner_analysis.format('spectre-meltdown-checker'))
            spectre_meldown_checker_banner(titles)
            spectre_meldown_checker(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            vulner_analysis(titles)

        else:
            print(titles.invalid)
            vulner_analysis(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        vulner_analysis(titles)

def passwd_attack(titles):
    try:
        print(titles.passwd_attack)
        tool = str(input(titles.which_tools.format(7))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_passwd_attack.format('BruteDum'))
            brutedum_banner(titles)
            brutedum(titles)

        elif tool == '2':
            print(titles.category_passwd_attack.format('FTPBruter'))
            ftpbruter_banner(titles)
            ftpbruter(titles)

        elif tool == '3':
            print(titles.category_passwd_attack.format('Leaked'))
            leaked_banner(titles)
            leaked(titles)

        elif tool == '4':
            print(titles.category_passwd_attack.format('Ncrack'))
            ncrack_banner(titles)
            ncrack(titles)

        elif tool == '5':
            print(titles.category_passwd_attack.format('SocialBox'))
            socialbox_banner(titles)
            socialbox(titles)

        elif tool == '6':
            print(titles.category_passwd_attack.format('Blazy'))
            blazy_banner(titles)
            blazy(titles)

        elif tool == '7':
            print(titles.category_passwd_attack.format('Hash-Buster'))
            hash_buster_banner(titles)
            hash_buster(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            passwd_attack(titles)

        else:
            print(titles.invalid)
            passwd_attack(titles)

        continue_or_not(titles)
    
    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        passwd_attack(titles)

def wireless_attack(titles):
    try:
        print(titles.wireless_attack)
        tool = str(input(titles.which_tools.format(23))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_wireless_attack.format('SniffAir'))
            sniffair_banner(titles)
            sniffair(titles)

        elif tool == '2':
            print(titles.category_wireless_attack.format('WiFi-Pumpkin'))
            wifi_pumpkin_banner(titles)
            wifi_pumpkin(titles)

        elif tool == '3':
            print(titles.category_wireless_attack.format('Airgeddon'))
            airgeddon_banner(titles)
            airgeddon(titles)

        elif tool == '4':
            print(titles.category_wireless_attack.format('PiKarma'))
            pikarma_banner(titles)
            pikarma(titles)

        elif tool == '5':
            print(titles.category_wireless_attack.format('Wifite 2'))
            wifite2_banner(titles)
            wifite2(titles)

        elif tool == '6':
            print(titles.category_wireless_attack.format('PixieWPS'))
            pixiewps_banner(titles)
            pixiewps(titles)

        elif tool == '7':
            print(titles.category_wireless_attack.format('Fluxion'))
            fluxion_banner(titles)
            fluxion(titles)

        elif tool == '8':
            print(titles.category_wireless_attack.format('Reaver'))
            reaver_banner(titles)
            reaver(titles)

        elif tool == '9':
            print(titles.category_wireless_attack.format('Ghost Phisher'))
            ghost_phisher_banner(titles)
            ghost_phisher(titles)

        elif tool == '10':
            print(titles.category_wireless_attack.format('zarp'))
            zarp_banner(titles)
            zarp(titles)

        elif tool == '11':
            print(titles.category_wireless_attack.format('Xerosploit'))
            xerosploit_banner(titles)
            xerosploit(titles)

        elif tool == '12':
            print(titles.category_wireless_attack.format('Seth'))
            seth_banner(titles)
            seth(titles)

        elif tool == '13':
            print(titles.category_wireless_attack.format('KickThemOut'))
            kickthemout_banner(titles)
            kickthemout(titles)

        elif tool == '14':
            print(titles.category_wireless_attack.format('Dracnmap'))
            dracnmap_banner(titles)
            dracnmap(titles)

        elif tool == '15':
            print(titles.category_wireless_attack.format('Wifiphisher'))
            wifiphisher_banner(titles)
            wifiphisher(titles)

        elif tool == '16':
            print(titles.category_wireless_attack.format('PhishX'))
            phishx_banner(titles)
            phishx(titles)

        elif tool == '17':
            print(titles.category_wireless_attack.format('CredSniper'))
            credsniper_banner(titles)
            credsniper(titles)

        elif tool == '18':
            print(titles.category_wireless_attack.format('shARP'))
            sharp_banner(titles)
            sharp(titles)

        elif tool == '19':
            print(titles.category_wireless_attack.format('PhisherMan'))
            phisherman_banner(titles)
            phisherman(titles)

        elif tool == '20':
            print(titles.category_wireless_attack.format('shARP 2'))
            sharp_2_banner(titles)
            sharp_2(titles)

        elif tool == '21':
            print(titles.category_wireless_attack.format('EvilTwinFramework'))
            eviltwinframework_banner(titles)
            eviltwinframework(titles)

        elif tool == '22':
            print(titles.category_wireless_attack.format('The Rogue Toolkit'))
            the_rogue_toolkit_banner(titles)
            the_rogue_toolkit(titles)

        elif tool == '23':
            print(titles.category_wireless_attack.format('WebSploit'))
            websploit_banner(titles)
            websploit(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            wireless_attack(titles)

        else:
            print(titles.invalid)
            wireless_attack(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        wireless_attack(titles)

def web_apps(titles):
    try:
        print(titles.web_apps)
        tool = str(input(titles.which_tools.format(18))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_web_apps.format('WhatWeb'))
            whatweb_banner(titles)
            whatweb(titles)

        elif tool == '2':
            print(titles.category_web_apps.format('NoSQLMap'))
            nosqlmap_banner(titles)
            nosqlmap(titles)

        elif tool == '3':
            print(titles.category_web_apps.format('SQLMate'))
            sqlmate_banner(titles)
            sqlmate(titles)

        elif tool == '4':
            print(titles.category_web_apps.format('SQLMap'))
            sqlmap_banner(titles)
            sqlmap(titles)

        elif tool == '5':
            print(titles.category_web_apps.format('sqlcake'))
            sqlcake_banner(titles)
            sqlcake(titles)

        elif tool == '6':
            print(titles.category_web_apps.format('BSQLinjector'))
            bsqlinjector_banner(titles)
            bsqlinjector(titles)

        elif tool == '7':
            print(titles.category_web_apps.format('XSSer'))
            xsser_banner(titles)
            xsser(titles)

        elif tool == '8':
            print(titles.category_web_apps.format('XXeinjector'))
            xxeinjector_banner(titles)
            xxeinjector(titles)

        elif tool == '9':
            print(titles.category_web_apps.format('XSStrike'))
            xsstrike_banner(titles)
            xsstrike(titles)

        elif tool == '10':
            print(titles.category_web_apps.format('Striker'))
            striker_banner(titles)
            striker(titles)

        elif tool == '11':
            print(titles.category_web_apps.format('WPScan'))
            wpscan_banner(titles)
            wpscan(titles)

        elif tool == '12':
            print(titles.category_web_apps.format('WPSeku'))
            wpseku_banner(titles)
            wpseku(titles)

        elif tool == '13':
            print(titles.category_web_apps.format('WAScan'))
            wascan_banner(titles)
            wascan(titles)

        elif tool == '14':
            print(titles.category_web_apps.format('WebSploit'))
            websploit_banner(titles)
            websploit(titles)

        elif tool == '15':
            print(titles.category_web_apps.format('WPSploit'))
            wpsploit_banner(titles)
            wpsploit(titles)

        elif tool == '16':
            print(titles.category_web_apps.format('SiteBroker'))
            sitebroker_banner(titles)
            sitebroker(titles)

        elif tool == '17':
            print(titles.category_web_apps.format('BadMod'))
            badmod_banner(titles)
            badmod(titles)

        elif tool == '18':
            print(titles.category_web_apps.format('Zoom'))
            zoom_banner(titles)
            zoom(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            web_apps(titles)

        else:
            print(titles.invalid)
            web_apps(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        web_apps(titles)

def exploit_tools(titles):
    try:
        print(titles.exploit_tools)
        tool = str(input(titles.which_tools.format(32))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_exploit_tools.format('roxysploit'))
            roxysploit_banner(titles)
            roxysploit(titles)

        elif tool == '2':
            print(titles.category_exploit_tools.format('Lunar'))
            lunar_banner(titles)
            lunar(titles)

        elif tool == '3':
            print(titles.category_exploit_tools.format('AutoRDPwn'))
            autordpwn_banner(titles)
            autordpwn(titles)

        elif tool == '4':
            print(titles.category_exploit_tools.format('RouterSploit'))
            routersploit_banner(titles)
            routersploit(titles)

        elif tool == '5':
            print(titles.category_exploit_tools.format('rootOS'))
            rootos_banner(titles)
            rootos(titles)

        elif tool == '6':
            print(titles.category_exploit_tools.format('SearchSploit'))
            searchsploit_banner(titles)
            searchsploit(titles)

        elif tool == '7':
            print(titles.category_exploit_tools.format('BSQLinjector'))
            bsqlinjector_banner(titles)
            bsqlinjector(titles)

        elif tool == '8':
            print(titles.category_exploit_tools.format('eXpliot'))
            expliot_banner(titles)
            expliot(titles)

        elif tool == '9':
            print(titles.category_exploit_tools.format('Pure Blood'))
            pure_blood_banner(titles)
            pure_blood(titles)

        elif tool == '10':
            print(titles.category_exploit_tools.format('XXEinjector'))
            xxeinjector_banner(titles)
            xxeinjector(titles)

        elif tool == '11':
            print(titles.category_exploit_tools.format('SQLMap'))
            sqlmap_banner(titles)
            sqlmap(titles)

        elif tool == '12':
            print(titles.category_exploit_tools.format('SQLMate'))
            sqlmate_banner(titles)
            sqlmate(titles)

        elif tool == '13':
            print(titles.category_exploit_tools.format('Termineter'))
            termineter_banner(titles)
            termineter(titles)

        elif tool == '14':
            print(titles.category_exploit_tools.format('WebSploit'))
            websploit_banner(titles)
            websploit(titles)

        elif tool == '15':
            print(titles.category_exploit_tools.format('sqlcake'))
            sqlcake_banner(titles)
            sqlcake(titles)

        elif tool == '16':
            print(titles.category_exploit_tools.format('AutoSploit'))
            autosploit_banner(titles)
            autosploit(titles)

        elif tool == '17':
            print(titles.category_exploit_tools.format('smod'))
            smod_banner(titles)
            smod(titles)

        elif tool == '18':
            print(titles.category_exploit_tools.format('NoSQLMap'))
            nosqlmap_banner(titles)
            nosqlmap(titles)

        elif tool == '19':
            print(titles.category_exploit_tools.format('TheFatRat'))
            thefatrat_banner(titles)
            thefatrat(titles)

        elif tool == '20':
            print(titles.category_exploit_tools.format('Exploit Pack'))
            exploit_pack_banner(titles)
            exploit_pack(titles)

        elif tool == '21':
            print(titles.category_exploit_tools.format('XSStrike'))
            xsstrike_banner(titles)
            xsstrike(titles)

        elif tool == '22':
            print(titles.category_exploit_tools.format('mimikittenz'))
            mimikittenz_banner(titles)
            mimikittenz(titles)

        elif tool == '23':
            print(titles.category_exploit_tools.format('Dracnmap'))
            dracnmap_banner(titles)
            dracnmap(titles)

        elif tool == '24':
            print(titles.category_exploit_tools.format('XSSer'))
            xsser_banner(titles)
            xsser(titles)

        elif tool == '25':
            print(titles.category_exploit_tools.format('ezsploit'))
            ezsploit_banner(titles)
            ezsploit(titles)

        elif tool == '26':
            print(titles.category_exploit_tools.format('SEToolkit'))
            setoolkit_banner(titles)
            setoolkit(titles)

        elif tool == '27':
            print(titles.category_exploit_tools.format('Auto-Root-Exploit'))
            auto_root_exploit_banner(titles)
            auto_root_exploit(titles)

        elif tool == '28':
            print(titles.category_exploit_tools.format('AhMyth-Android-RAT'))
            ahmyth_android_rat_banner(titles)
            ahmyth_android_rat(titles)

        elif tool == '29':
            print(titles.category_exploit_tools.format('Exploit-Framework'))
            exploit_framework_banner(titles)
            exploit_framework(titles)

        elif tool == '30':
            print(titles.category_exploit_tools.format('WinRootHelper'))
            winroothelper_banner(titles)
            winroothelper(titles)

        elif tool == '31':
            print(titles.category_exploit_tools.format('Metasploit Framework'))
            metasploit_banner(titles)
            metasploit(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            exploit_tools(titles)

        else:
            print(titles.invalid)
            exploit_tools(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        exploit_tools(titles)

def sniff_spoof(titles):
    try:
        print(titles.sniff_spoof)
        tool = str(input(titles.which_tools.format(8))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_sniff_spoof.format('Airgeddon'))
            airgeddon_banner(titles)
            airgeddon(titles)

        elif tool == '2':
            print(titles.category_sniff_spoof.format('Xerosploit'))
            xerosploit_banner(titles)
            xerosploit(titles)

        elif tool == '3':
            print(titles.category_sniff_spoof.format('WebSploit'))
            websploit_banner(titles)
            websploit(titles)

        elif tool == '4':
            print(titles.category_sniff_spoof.format('SniffAir'))
            sniffair_banner(titles)
            sniffair(titles)

        elif tool == '5':
            print(titles.category_sniff_spoof.format('The Rogue Toolkit'))
            the_rogue_toolkit_banner(titles)
            the_rogue_toolkit(titles)

        elif tool == '6':
            print(titles.category_sniff_spoof.format('zarp'))
            zarp_banner(titles)
            zarp(titles)

        elif tool == '7':
            print(titles.category_sniff_spoof.format('WiFi-Pumpkin'))
            wifi_pumpkin_banner(titles)
            wifi_pumpkin(titles)

        elif tool == '8':
            print(titles.category_sniff_spoof.format('Seth'))
            seth_banner(titles)
            seth(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            sniff_spoof(titles)

        else:
            print(titles.invalid)
            sniff_spoof(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        sniff_spoof(titles)

def malware_bypass(titles):
    try:
        print(titles.malware_bypass)
        tool = str(input(titles.which_tools.format(21))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_malware_bypass.format('ZeroDoor'))
            zerodoor_banner(titles)
            zerodoor(titles)

        elif tool == '2':
            print(titles.category_malware_bypass.format('Terminator'))
            terminator_banner(titles)
            terminator(titles)

        elif tool == '3':
            print(titles.category_malware_bypass.format('WinPayloads'))
            winpayload_banner(titles)
            winpayloads(titles)

        elif tool == '4':
            print(titles.category_malware_bypass.format('sAINT'))
            saint_banner(titles)
            saint(titles)

        elif tool == '5':
            print(titles.category_malware_bypass.format('BeeLogger'))
            beelogger_banner(titles)
            beelogger(titles)

        elif tool == '6':
            print(titles.category_malware_bypass.format('HackTheWorld'))
            hacktheworld_banner(titles)
            hacktheworld(titles)

        elif tool == '7':
            print(titles.category_malware_bypass.format('HatKey'))
            hatkey_banner(titles)
            hatkey(titles)

        elif tool == '8':
            print(titles.category_malware_bypass.format('ezsploit'))
            ezsploit_banner(titles)
            ezsploit(titles)

        elif tool == '9':
            print(titles.category_malware_bypass.format('trolo'))
            trolo_banner(titles)
            trolo(titles)

        elif tool == '10':
            print(titles.category_malware_bypass.format('GetWin'))
            getwin_banner(titles)
            getwin(titles)

        elif tool == '11':
            print(titles.category_malware_bypass.format('The Fat Rat'))
            thefatrat_banner(titles)
            thefatrat(titles)

        elif tool == '12':
            print(titles.category_malware_bypass.format('DKMC'))
            dkmc_banner(titles)
            dkmc(titles)

        elif tool == '13':
            print(titles.category_malware_bypass.format('Parat'))
            parat_banner(titles)
            parat(titles)

        elif tool == '14':
            print(titles.category_malware_bypass.format('mkvenom'))
            mkvenom_banner(titles)
            mkvenom(titles)

        elif tool == '15':
            print(titles.category_malware_bypass.format('venom'))
            venom_banner(titles)
            venom(titles)

        elif tool == '16':
            print(titles.category_malware_bypass.format('Metasploit Framework'))
            metasploit_banner(titles)
            metasploit(titles)

        elif tool == '17':
            print(titles.category_malware_bypass.format('Cloak'))
            cloak_banner(titles)
            cloak(titles)

        elif tool == '18':
            print(titles.category_malware_bypass.format('Metasploit AV Evasion'))
            avoid_banner(titles)
            avoid(titles)

        elif tool == '19':
            print(titles.category_malware_bypass.format('AVET'))
            avet_banner(titles)
            avet(titles)

        elif tool == '20':
            print(titles.category_malware_bypass.format('AhMyth-Android-RAT'))
            ahmyth_android_rat_banner(titles)
            ahmyth_android_rat(titles)

        elif tool == '21':
            print(titles.category_malware_bypass.format('NXcrypt'))
            nxcrypt_banner(titles)
            nxcrypt(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            malware_bypass(titles)

        else:
            print(titles.invalid)
            malware_bypass(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()

    except IndexError:
        clear()
        print(titles.invalid)
        malware_bypass(titles)

def ddos_tools(titles):
    try:
        print(titles.ddos_tools)
        tool = str(input(titles.which_tools.format(7))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_ddos_tools.format('SlowLoris'))
            slowloris_banner(titles)
            slowloris(titles)

        elif tool == '2':
            print(titles.category_ddos_tools.format('ZAmbIE'))
            zambie_banner(titles)
            zambie(titles)

        elif tool == '3':
            print(titles.category_ddos_tools.format('Airgeddon'))
            airgeddon_banner(titles)
            airgeddon(titles)

        elif tool == '4':
            print(titles.category_ddos_tools.format('WebSploit'))
            websploit_banner(titles)
            websploit(titles)

        elif tool == '5':
            print(titles.category_ddos_tools.format('UFONet'))
            ufonet_banner(titles)
            ufonet(titles)

        elif tool == '6':
            print(titles.category_ddos_tools.format('zarp'))
            zarp_banner(titles)
            zarp(titles)

        elif tool == '7':
            print(titles.category_ddos_tools.format('Memcrashed-DDoS-Exploit'))
            memcrashed_banner(titles)
            memcrashed(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            ddos_tools(titles)

        else:
            clear()
            print(titles.invalid)
            ddos_tools(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        ddos_tools(titles)

def downloader_installer(titles):
    try:
        print(titles.downloader_installer)
        tool = str(input(titles.which_tools.format(8))).strip()
        clear()
        action(titles,tool)

        if tool == '0':
            home_page(titles)

        elif tool == '1':
            print(titles.category_downloader_installer.format('Fsociety'))
            fsociety_banner(titles)
            fsociety(titles)

        elif tool == '2':
            print(titles.category_downloader_installer.format('Malicious'))
            malicious_banner(titles)
            malicious(titles)

        elif tool == '3':
            print(titles.category_downloader_installer.format('Tool-X'))
            tool_x_banner(titles)
            tool_x(titles)

        elif tool == '4':
            print(titles.category_downloader_installer.format('Katoolin'))
            katoolin_banner(titles)
            katoolin(titles)

        elif tool == '5':
            print(titles.category_downloader_installer.format('IntRec-Pack'))
            intrec_pack_banner(titles)
            intrec_pack(titles)

        elif tool == '6':
            print(titles.category_downloader_installer.format('ZAmbIE'))
            zambie_banner(titles)
            zambie(titles)

        elif tool == '7':
            print(titles.category_downloader_installer.format('The PenTesters Framework'))
            ptf_banner(titles)
            ptf(titles)

        elif tool == '8':
            print(titles.category_downloader_installer.format('Lunar'))
            lunar_banner(titles)
            lunar(titles)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            downloader_installer(titles)

        else:
            clear()
            print(titles.invalid)
            downloader_installer(titles)

        continue_or_not(titles)

    except KeyboardInterrupt:
        print(titles.exiting)
        exit()
    except IndexError:
        clear()
        print(titles.invalid)
        downloader_installer(titles)

action(english,"LANG")