class Color:
    no_colored = "\033[0m"
    white = "\033[37m"
    blue = "\033[34m"
    green = "\033[92m"
    red = "\033[91m"
    yellow = "\033[93m"
    purple = "\033[35m"

class english:
    exiting = "Exiting, Thank you for using Yikebox!  (＾〃＾)"
    invalid = Color.red+"[!] "+Color.green+"(Warning)"+Color.white+" Invalid choice Baka (╬ Ò﹏Ó)"
    doesnt_exists = Color.red+"[!] "+Color.green+"(Warning)"+Color.white+" That path is doesn't exist, Try manually create the given path if it isnt automatically created  	(*￣▽￣)b"
    unknow_distro = Color.red+"[!] "+Color.green+"(Warning)"+Color.white+" Sorry! I don't know What distro you are using  	(ಥ﹏ಥ) "
    doesnt_support_windows = Color.red+"[!] "+Color.green+"(Warning)"+Color.white+" This tool doesn't support Windows yet, however you can run it within the ``lunux subsystem for windows`` ╮(￣～￣)╭ "
    only_compatible = Color.red+"[!] "+Color.green+"(Warning)"+Color.white+" Sorry! This tool only compatible with your OS , however you can run it within the ``lunux subsystem for windows`` ╮(￣～￣)╭ "+Color.yellow+"{}"
    run_well = Color.red+"[!] "+Color.green+"(Warning)"+Color.white+" This tool can only run well on "+Color.yellow+"{}"
    wsl = Color.red+"[!] "+Color.green+"(Warning)"+Color.white+" But you can install Windows Subsystem for Linux: http://bit.ly/2wzmn6L"
    continue_or_not = Color.purple+"[?] "+Color.green+"(Request) "+Color.white+"Do you want to continue? [Y/N] > "+Color.no_colored
    installed_or_not = Color.purple+"[?] "+Color.green+"(Request) "+Color.white+" Have you install "+Color.yellow+"{} yet? [Y/N] > "+Color.no_colored
    done = Color.blue+"[+]"+Color.green+" (Info) "+Color.yellow+"{} "+Color.white+"has been installed succesfully "
    installing = Color.yellow+"[+] "+Color.green+"(Execute) "+Color.white+"Installing "+Color.yellow+"{}"+Color.white+"..."
    installed = Color.blue+"[i] "+Color.green+"(Info) "+Color.yellow+"{}"+Color.white+" is already installed! (￣ω￣;)"
    downloading = Color.yellow+"[+] "+Color.green+"(Execute) "+Color.white+"Downloading, please wait... (づ￣ ³￣)づ "+Color.yellow+"{}"+Color.white+"..."
    path_folder = Color.purple+"[?] "+Color.green+"(Request)"+Color.white+" Enter the path of folder to save "+Color.yellow+"{}"+Color.white+"  because Yikebox is unsure of whare to save it> "+Color.no_colored
    
    note_saved = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" All Hacking tools are saved in "+Color.yellow+"C:\\"
    note_python3 = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" In "+Color.yellow+"please  install Python 3.7 or above! (￣ω￣;)"+Color.white+", enable "+Color.yellow+"Add Python 3.7 to PATH"
    note_python2 = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" In "+Color.yellow+"Customize Python 2.7"+Color.white+", find "+Color.yellow+"Add python.exe to Path"+Color.white+" and choose "+Color.yellow+"Will be installed on local hard drive"+Color.white
    note_git = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" In "+Color.yellow+"Git Setup"+Color.white+", choose "+Color.yellow+"Use Git from Windows Command Propmt"
    note_ruby = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" When install Ruby-lang, choose "+Color.yellow+"Add Ruby executables to your PATH"+Color.white+" and "+Color.yellow+"Use UTF-8 as default external encoding"
    note_powershell = Color.red+"[!] "+Color.green+"(Info)"+Color.no_colored+" "+Color.green+"(Warning)"+Color.white+" You have to install PowerShell to run this tool: http://bit.ly/2Z3dz4A"+Color.no_colored
    note_sslscan = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" Extract sslscan-win-1.11.11-rbsec.zip and run sslscan.exe"
    note_evilginx2 = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" Extract evilginx_windows_x86_2.3.0.zip and run evilginx.exe"
    note_sqlcake = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" Extract sqlcake-v1.1.tar and run ruby sqlcake.rb on CMD"
    note_exploit_pack = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" Extract exploitpack.zip and open ExploitPack_12.jar with Java"
    note_tools = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" To run "+Color.yellow+"{}, "+Color.white+"enter "+Color.yellow+"{}"+Color.white+" on its folder"+Color.no_colored
    note_tools2 = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" To run "+Color.yellow+"{}, "+Color.white+"enter "+Color.yellow+"{} "+Color.white+"on "+Color.yellow+"{}"
    readmore = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" You can read more about "+Color.yellow+"{}"+Color.white+" here: "+Color.yellow+"{}"
    contribution = Color.blue+"[i] "+Color.green+"(Info)"+Color.white+" You can contribute to Yikeboxes development  here: Https://dsc.gg/Yikesec"

    Yikebox_description = "For use by Yikesec and verified users ONLY"
    billcipher_description = "An Information Gathering tool for a given Website or IP address"
    leaked_description = "A Checking tool for Hash codes, emails and passwords"
    devploit_description = "A simple python script for information Gathering"
    gorecon_description = "A lightweight Reconnaissance Tool written in Go lang"
    dracnmap_description = "Nmap is a program used to map and find exloits on a given network"
    nmap_description = "The Network Mapper and Exploiter"
    sublist3r_description = "Fast subdomains enumeration tool for Pentesting"
    sslscan_description = "A Fast SSL/TLS Open source Scanner"
    dnsmaper_description = "DNSMaper - Domain Transfer Tester, Subdomain Enumeration, Banner Detection and Generation Map, In short: a program that maps information and exploits within a DNS"
    a2sv_description = "SSL Vulnerability Auto Scanner"
    shodanhat_description = "Searches Server Information with Shodan"
    hatcloud_description = "Bypassing CloudFlare protected servers on Linux and Windows"
    sub6_description = "Website Application Scanner"
    masscan_description = "A Mass IP Port Open-source Scanner"
    dnsmap_description = "DNS domain name Gathering and Brute Forcing tool"
    infosploit_description = "An Information Gathering Tool written in Python 2"
    infoga_description = "Gathering Email Information from a given Website"
    httrack_description = "An Open-source Website Yoinker (copier)"
    subdomain_analyzer_description = "An Open-source Subdomain Analyzer written in Python 2"
    apt2_description = "An Automated PenTesting Toolkit written in Python 2"
    inspy_description = "A LinkedIn enumeration tool written in Python 2"
    setoolkit_description = "A Social-Engineering Open-source Toolkit written in Python 2"
    ghost_phisher_description = "An Open-source Phishing attack tool"
    phishx_description = "The most powerful Phishing tool"
    phisherman_description = "A Phishing tool that works with Ngrok to Make Phishing simple for everyone"
    aron_description = "Aron - A simple GO script for finding hidden GET & POST parameters with Brute-force"
    evilginx2_description = "Next Generation of Phishing Attacks and Bypassing 2FA written in Go lang"
    infinity_description = "Find Anyone’s Phone Number a Facebook account"
    credsniper_description = "A Phishing attacking Framework supports capturing 2FA tokens"
    sqlmap_description = "An Automatic SQL injection and database takeover tool"
    sqlmate_description = "A friend of SQLmap which will do what you always expected from SQLmap"
    searchsploit_description = "The offline Exploit Database Archive"
    brakeman_description = "A Security Scanner for Ruby on Rails apps"
    whatweb_description = "The Next generation of Website Security scanner"
    vulscan_description = "A Vulnerability Scanner with Nmap"
    takeover_description = "Sub-Domain TakeOver Vulnerability Scanner"
    openvas_description = "An Open-source Vulnerability Scanning System"
    droid_hunter_description = "Android Apps Vulnerability Analysis and Android Pentest tool"
    patrowl_description = "An Open Source and Free solution for orchestrating Security Operations written in Python 2"
    infection_monkey_description = "A Data center Security Testing Tool written in Python 2"
    vuls_description = "A Vulnerability Scanner for Linux and FreeBSD written in Golang"
    wpseku_description = "An Open-source Wordpress Security Scanner written in Python 3"
    wpscan_description = "A WordPress vulnerability scanner written in Ruby lang"
    routersploit_description = "An Exploitation Framework for Embedded Devices written in Python 3"
    xsstrike_description = "An Intelligent XSS Detection and Exploitation Suite"
    striker_description = "Offensive Information and Vulnerability Scanner for Websites"
    raptor_description = "Web-based Source Code Vulnerability Scanner"
    breacher_description = "An Advanced Admin Site and EAR vulnerabilites finder"
    wascan_description = "A Website Application Scanner written in Python 2"
    xsser_description = "Exploiting and Detecting XSS vulnerabilities in Web-based apps"
    spectre_meldown_checker_description = "Spectre and Meltdown checking tool for Linux and BSD"
    brutedum_description = "Brute Force attacks SSH, FTP, Telnet, PostgreSQL, RDP, VNC with Hydra, Medusa and Ncrack"
    ftpbruter_description = "A FTP Server brute forcing tool written in Python 3"
    hash_buster_description = "An Online Hash Cracking tool written in Python 3"
    socialbox_description = "A Bruteforce Attack Framework for Social Networks"
    blazy_description = "Crack Website Logins in seconds with Bruteforce attacks"
    ncrack_description = "An High-speed Open-source Network cracking tool"
    kickthemout_description = "Kick Any Device Off LAN Network with ARP Spoof Attack"
    sniffair_description = "An Open-source Wireless Security Framework written in Python 2"
    wifi_pumpkin_description = "A Framework for Rogue WiFi Access Point Attack"
    airgeddon_description = "Multi-use Bash Script for Linux Systems to audit Wireless Networks"
    pikarma_description = "Detects Wireless Network attacks performed by KARMA Module (Fake AP)"
    wifite2_description = "An Automated Wireless Attacking tool"
    pixiewps_description = "An offline WiFi Protected Setup bruteforce utility"
    fluxion_description = "The number 1 WiFi Cracking Tool"
    reaver_description = "An Wifi Protected Setup (WPS) Bruteforce attacking tool"
    zarp_description = "A Network Attacking Tool written in Python 2"
    xerosploit_description = "Toolkit to Perform MITM, Spoofing, DoS Attack, Images Sniffing"
    seth_description = "A MITM attacking tool with RDP connection written in Python 3"
    wifiphisher_description = "A Phishing attacking tool written in Python 2 using fake WiFi clients"
    sharp_description = "Scanning method to detect and remove any ARP-spoofer from the Network"
    sharp_2_description = "An updated version of shARP with more options and better performance"
    eviltwinframework_description = "A Framework written in Python 2 for Pentesters to Perform Evil Twin attacks"
    theroguetoolkit_description = "Perform Targeted Evil Twin Attacks with Evil Access Points"
    sitebroker_description = "A Website Pentesting Tool written in Python 2"
    websploit_description = "An Advanced Pentesting Framework written in Python 2"
    wpsploit_description = "A Wordpress Plugin Security Testing tool written in Python 2"
    zoom_description = "Fast and Automatic Wordpress Vulnerability Scanner"
    nosqlmap_description = "Automate the NoSQL Database and Web Apps Exploitation Tool"
    sqlcake_description = "Automatic SQL Injection Exploitation toolkit"
    bsqlinjector_description = "Blind SQL Injection Exploit tool"
    xxeinjector_description = "XXE Vulnerability Exploit tool"
    badmod_description = "Detect Website CMS and Website Scanner to Auto Exploit"
    roxysploit_description = "An Open-source Hacking Framework written in Python 2 for Hackers"
    lunar_description = "Python 2 Security Framework and Hacking toolkit"
    autordpwn_description = "The Shadow PowerShell script Framework attacking"
    expliot_description = "Internet Of Things Exploitation Framework"
    rootos_desscription = "An Mac OS X Exploitation tool written in Python 2"
    pure_blood_description = "A PenTesting Framework created for Security Professionals"
    termineter_description = "A Smart Meters Security Testing Framework written in Python 3"
    autosploit_description = "An Automated Exploiting tool written in Python 2"
    smod_description = "A MODBUS Pentesting Framework written in Python 2, MOBIUS REFERANCE??!?!?1!??!?1!??!?1!?!?"
    thefatrat_description = "A Massive Backdoor creation and Exploitation tool"
    exploit_pack_description = "The next generation of Security Framework Exploitation"
    mimikittenz_description = "A post-exploit PowerShell tool for extracting juicy info from memory"
    ezsploit_description = "An Automated Linux bash script for Metasploit Framework"
    auto_root_exploit_description = "Exploiting root of Unix-like systems"
    ahmyth_android_rat_description = "Android Remote Administration Tool for Linux and Windows"
    expliot_framework_description = "An Exploitation Framework written in Python 2 for Website Vulnerabilities"
    winroothelper_description = "Windows Privilege Escalation with PowerShell scripts"
    metasploit_description = "The best Pentesting Framework in the world, other than YIKEBOX OFCOURSE"
    zerodoor_description = "A multi-platform Backdoors Generator written in Python 2"
    terminator_description = "An Easy way to create Metasploit Payloads"
    winpayloads_description = "Undetectable Windows Payloads Generator written in Python 2"
    saint_description = "A Windows Spyware Generator written in Java"
    beelogger_description = "A Windows Keyloggers Generator written in Python 2"
    hacktheworld_dewcription = "Generating Payloads to Bypass All Antivirus"
    hatkey_description = "Python Command and Controler Keylogger"
    trolo_description = "An easy way to bypass Antivirus"
    getwin_description = "An Undetectable Win32 Payload Generator and Listener"
    dkmc_description = "A PowerShell Attacking tool and more"
    parat_description = "Backdoor creator for Remote Access Control"
    mkvenom_description = "A simple Bash script to create msfvenom Payloads"
    venom_description = "Metasploit shellcode Generator/Compiler/Listener"
    cloak_description = "An Intelligent Python Backdoors Framework"
    avoid_description = "A Metasploit Payloads Generator can Bypass Anti-Virus"
    avet_description = "An AntiVirus Bypassing tool working with Metasploit Framework"
    nxcrypt_description = "A Python backdoor Encryption tool written in Python 2"
    slowloris_description = "A DoS Attacking tool written in Python 3 for Low Bandwidth"
    zambie_description = "A DoS and DDoS Attacking toolkit written in Python 2"
    ufonet_description = "A DDoS Botnet via Web Abuse"
    memcrashed_description = "DDoS attack by sending fake UDP packets to vulnerable Memcached servers searched by Shodan"
    fsociety_description = "A Hacking tools Installer written in Python 2"
    malicious_description = "A Malware downloading tool written in Python 2"
    tool_x_description = "Turn your Linux distro to a Pentesting OS with 263 Hacking tools"
    katoolin_description = "A Kali Linux Pentesting tools Installer written in Python 2"
    intrec_pack_description = "An Intelligence and Reconnaissance Package/Bundle installer"
    ptf_description = "A Python 2 Script to Create a Similar and Familiar Distro for PenTesters"

    leaked_read_only = Color.blue+"[i]"+Color.green+" (Info) "+Color.white+"Leaked has been cancelled because its database (https://Lea.kz) has been gone"
    
    choose_category = Color.purple+"[?] "+Color.green+"(Choice)"+Color.white+" What kind of tools do you want to install? [1-10] > "+Color.no_colored
    which_tools = Color.purple+"[?] "+Color.green+"(Choice)"+Color.white+" Which tools do you want to install? [1-{}] > "+Color.no_colored
    choose_titles = Color.purple+"[?] "+Color.green+"(KEY-SYSTEM)"+Color.white+" Enter the Yikebox key > "+Color.no_colored
    category_info_garther = Color.yellow+"[+] "+Color.green+"(Home page/Information Garthering/{}) "+Color.white+">"+Color.no_colored
    category_vulner_analysis = Color.yellow+"[+] "+Color.green+"(Home page/Vulnerability Analysis/{}) "+Color.white+">"+Color.no_colored
    category_passwd_attack = Color.yellow+"[+] "+Color.green+"(Home page/Password Attacks/{}) "+Color.white+">"+Color.no_colored
    category_wireless_attack = Color.yellow+"[+] "+Color.green+"(Home page/Wireless and Network Attacks/{}) "+Color.white+">"+Color.no_colored
    category_web_apps = Color.yellow+"[+] "+Color.green+"(Home page/Website Applications/{}) "+Color.white+">"+Color.no_colored
    category_exploit_tools = Color.yellow+"[+] "+Color.green+"(Home page/Exploitation/{}) "+Color.white+">"+Color.no_colored
    category_sniff_spoof = Color.yellow+"[+] "+Color.green+"(Home page/Sniffing & Spoofing/{}) "+Color.white+">"+Color.no_colored
    category_malware_bypass = Color.yellow+"[+] "+Color.green+"(Home page/Malware Generator & Bypass AV/{}) "+Color.white+">"+Color.no_colored
    category_ddos_tools = Color.yellow+"[+] "+Color.green+"(Home page/DDoS Attacks/{}) "+Color.white+">"+Color.no_colored
    category_downloader_installer = Color.yellow+"[+] "+Color.green+"(Home page/DownloaderS & InstallerS/{}) "+Color.white+">"+Color.no_colored

    help = Color.yellow+"""[+]"""+Color.green+""" (Help) """+Color.white+""">
        homep    Back to Home page
         lang    Please enter the Yikebox Key
         exit    Exit Yikebox
  infogarther    List of Infomation Garthering tools
       vulner    List of Vulnerability Analysis tools
       passwd    List of Password Attacking tools
     wireless    List of Wireless and Network Attacking tools
      webapps    List of Website Applications Exploiting tools
    exploiter    List of Exploitation toptf_descriptionols
   sniffspoof    List of Sniffing & Spoofing tools
     malwarer    List of Malware Generator & Bypass AV tools
       ddoser    List of DDoS Attacking tools
    installer    List of Downloader & Installer tools
    changelog    List of the changes
        about    About Yikebox"""

    changelog = Color.blue+"""[i] """+Color.green+"""(Change log)"""+Color.white+"""
+ Yikebox 
  - Made With love And Hatered By Sakura 95"""

    about_Yikebox = Color.blue+"""[i] """+Color.green+"""(Info)"""+Color.white+""" About Yikebox
    """+Color.yellow+"""Description: """+Color.white+"""Skids beware
    """+Color.yellow+"""Developed by: """+Color.white+"""Yikesec"""
 
    titles_list = Color.green+"""            (KEY-SYSTEM)"""+Color.white+"""
+--------------------------------+
|             Verify             |
+--------------------------------+           
|      Please enter the key      | 
|        To use this tool        |
|                        o(0ω0)o | 
+--------------------------------+

    ████████                    
  ██        ██                  
██            ██████████████████
██  ████                      ██
██  ████      ░░░░██░░██░░██░░██
██░░        ░░████  ██  ██  ██  
  ██░░░░░░░░██                  
    ████████                    

"""                

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# I`m pretty sure that this is redundant as i removed he titles switcher becausde im a lazy fuck and cba coding it, i cant remember (he forgor💀)

    home_page = Color.yellow+"""[+] """+Color.green+"""(Home page)"""+Color.white+""" >
+----------------------------------------------------------------------------------+
|                            d(￣▽￣*)  HOME PAGE (*￣▽￣)b                        |
+----------------------------------------------------------------------------------+
| [1] Information Gathering               [2] Vulnerability Analysis               |
| [3] Password attacks                    [4] Wireless and Network Attacks         |
| [5] Web Applications                    [6] Exploitation Tools                   |
| [7] Sniffing & Spoofing                 [8] DDoS Attacks                         |
| [9] Malware Generator & Bypass AV       [10] Downloaders & Installers            |
|                                                                                  |
| [0] Exit                                                                         |
|                                                                     By Sakura 95 |
+----------------------------------------------------------------------------------+
    ⠀⠀       ⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀   ⠀⠀      ⠀⠀⠀⢀⣤⣶⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⠉⠙⠻⣦⢀⣠⣴⣾⡿⠿⠿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀           ⠀⠀   ⠀⢀⣾⡟⠉⠉⠉⠙⠛⠿⣷⣦⣤⣤⣶⣶⣶⣶⣶⣶⣶⣾⠋⠀⠀⠀⠀⠀⠹⣿⠛⠉⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀    ⠀⠀    ⠀⠀      ⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠉⠉⠉⠉⠉⠉⣽⠃⠀⠀⠀⣠⣤⣤⣀⣹⣇⣀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀    ⠀          ⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⣼⡏⢀⣿⠟⠉⠉⠙⠻⣦⣶⠶⠶⠿⠿⣦⡀⠀⠀⠀⠀
⠀⠀        ⠀  ⠀⠀    ⠀⢿⣇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠘⢷⣾⡇⠀⠀⠀⠀⠀⢻⣧⣀⠀⠀⠀⠈⣿⠀⠀⠀⠀
⠀⠀              ⠀⠀⠀⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⣀⣀⣀⣀⣽⣧⠀⠀⠀⠀⢀⣾⠏⢹⡇⠀⠀⢠⡟⠀⠀⠀⠀
⠀⠀              ⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠉⠁⠙⠷⣦⣤⣶⡿⠻⠶⠟⠁⠀⢀⣾⠃⠀⠀⠀⠀
⠀⠀              ⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⣠⣾⡇⠀⠀⠀⠀⠀
⠀⠀              ⠀⠀⢀⣿⠇⢀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⣀⣙⣻⣿⣟⡋⢹⣷⠀⠀⠀⠀⠀
⠀        ⠀      ⠀⠀⢸⣿⣾⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⡀⠀⠀⠀⠀
              ⣀⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠛⠃
              ⠈⠉⠀⠀⠘⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⡿⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀              ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡟⠁⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣃⣤⣤⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⡀⠀
⠀              ⠀⠰⠾⠟⠛⣿⣿⣿⡿⣋⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢿⣄⣠⡿⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀              ⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣯⣀⠀⠀⠀⠀⠀
⠀              ⠀⠀⠀⢀⣤⡶⠟⠛⢿⣦⣌⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⣠⣾⡿⠋⠉⠛⠿⢶⠀⠀⠀
⠀              ⠀⠀⠀⠛⠋⠀⠀⠀⠀⠉⠻⢿⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀    ⠀⠀    ⠀      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠿⣷⣶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣶⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀    ⠀    ⠀⠀⠀⠀    ⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

    info_gathering = Color.yellow+"""[+] """+Color.green+"""(Home page/Information Garthering)"""+Color.white+""" >
+----------------------------------------------------------------+
|       o(>ω<)o         INFORMATION GARTHERING       o(>ω<)o     |
+----------------------------------------------------------------+
| [1] BillCipher       [2] Leaked              [3] Devploit      |
| [4] Gorecon          [5] Dracnmap            [6] Nmap          |
| [7] Sublist3r        [8] SSLScan             [9] DNSMaper      |
| [10] ShodanHat       [11] HatCloud           [12] A2SV         |
| [13] sub6            [14] Masscan            [15] dnsmap       |
| [16] InfoSploit      [17] Infoga             [18] HTTrack      |
| [19] APT2            [20] InSpy              [21] SEToolkit    |
| [22] PhishX          [23] PhisherMan         [24] Aron         |
| [25] Evilginx 2      [26] infinity           [27] CredSniper   |
| [28] Striker         [29] WAScan             [30] Ghost Phisher|
| [31] Breacher        [32] SiteBroker         [33] WebSploit    |
| [34] Pure Blood      [35] SubDomain-Analyzer                   |  
| [0] Back to the Home page                                      |          
+----------------------------------------------------------------+"""

    vulner_analysis = Color.yellow+"""[+] """+Color.green+"""(Home page/Vulnerability Analysis)"""+Color.white+""" >
+-------------------------------------------+
| (*・ω・)ﾉVULNERABILITY ANALYSIS(*・ω・)ﾉ  |
+-------------------------------------------+
| [1] Nmap       [2] SQLMap                 |
| [3] SQLMate    [4] SearchSploit           |
| [5] Brakeman   [6] WhatWeb                |
| [7] vulscan    [8] TakeOver               |
| [9] OpenVAS    [10] Droid-Hunter          |
| [11] PatrOwl   [12] Zoom                  |
| [13] Vuls      [14] WPSeku                |
| [15] WPScan    [16] RouterSploit          |
| [17] XSStrike  [18] Striker               |
| [19] Raptor    [20] XSSer                 |
| [21] Breacher  [22] A2SV                  |
| [23] BadMod    [24] Pure Blood            |
| [25] Infection Monkey                     |
| [26] Spectre & Meltdown checker for Linux |
| [0] Back to the Home page                 |
+-------------------------------------------+"""

    passwd_attack = Color.yellow+"""[+] """+Color.green+"""(Home page/Password Attacks)"""+Color.white+""" >
+-------------------------------+
|   PASSWORD ATTACKS(＃￣ω￣)   |
+-------------------------------+
| [1] BruteDum    [2] FTPBruter |
| [3] Leaked      [4] Ncrack    |
| [5] SocialBox   [6] Blazy     |
| [7] Hash-Buster               |
| [0] Back to the Home page     |
+-------------------------------+
|  Note:                        |
|        Dont use this shit     |
|        unless you know its    |
|        safe   (ノ_<、)        |
+-------------------------------+
"""

    wireless_attack = Color.yellow+"""[+] """+Color.green+"""(Home page/Wireless and Network Attacks)"""+Color.white+""" >
+-------------------------------------+
|    WIRELESS AND NETWORK ATTACKS     |
+-------------------------------------+
| [1] SniffAir       [2] WiFi-Pumpkin |
| [3] Airgeddon      [4] PiKarma      |
| [5] Wifite 2       [6] PixieWPS     |
| [7] Fluxion        [8] Reaver       |
| [9] Ghost Phisher  [10] zarp        |
| [11] Xerosploit    [12] Seth        |
| [13] KickThemOut   [14] Dracnmap    |
| [15] Wifiphisher   [16] PhishX      |
| [17] CredSniper    [18] shARP       |
| [19] PhisherMan    [20] shARP 2.0   |
| [21] EvilTwinFramework              |
| [22] The Rouge Toolkit              |
| [23] WebSploit                      |
| [0] Back to the Home page           | 
+-------------------------------------+"""

    web_apps = Color.yellow+"""[+] """+Color.green+"""(Home page/Website Applications)"""+Color.white+""" >
+---------------------------------+
|  (¯▿¯)WEBSITE APPLICATIONS(¯▿¯) |
+---------------------------------+
| [1] WhatWeb    [2] NoSQLMap     |
| [3] SQLMate    [4] SQLMap       |
| [5] sqlcake    [6] BSQLinjector |
| [7] XSSer      [8] XXEinjector  |
| [9] XSStrike   [10] Striker     |
| [11] WPScan    [12] WPSeku      |
| [13] WAScan    [14] WebSploit   |
| [15] WPSploit  [16] SiteBroker  |
| [17] BadMod    [18] Zoom        |
| [0] Back to the Home page       |
+---------------------------------+"""

    exploit_tools =  Color.yellow+"""[+] """+Color.green+"""(Home page/Exploitation)"""+Color.white+""" >
+------------------------------------------------------+
|           („ಡωಡ„)   EXPLOITATION   („ಡωಡ„)           |
+------------------------------------------------------+
| [1] roxysploit    [2] Lunar         [3] AutoRDPwn    |
| [4] routersploit  [5] rootOS        [6] SearchSploit |
| [7] BSQLinjector  [8] eXpliot       [9] Pure Blood   |
| [10] XXEinjector  [11] SQLMap       [12] SQLMate     |
| [13] Termineter   [14] WebSploit    [15] sqlcake     |
| [16] AutoSploit   [17] smod         [18] NoSQLMap    |
| [19] TheFatRat    [20] Exploit Pack [21] XXStrike    |
| [22] mimikittenz  [23] Dracnmap     [24] XSSer       |
| [25] ezsploit     [26] SEToolkit                     |
| [27] Auto-Root-Exploit    [28] AhMyth-Android-RAT    |
| [29] Exploit-Framework    [30] WinRootHelper         |
| [31] Metasploit Framework [0] Back to Home page      |
+------------------------------------------------------+"""

    sniff_spoof = Color.yellow+"""[+] """+Color.green+"""(Home page/Sniffing & Spoofing)"""+Color.white+""" >
+---------------------------------+
|     SNIFFING & SPOOFING(＞﹏＜)|
+---------------------------------+
| [1] Airgeddon    [2] Xerosploit |
| [3] WebSploit    [4] SniffAir   |
| [5] The Rouge Toolkit  [6] zarp |
| [7] WiFi-Pumpkin       [8] Seth |
| [0] Back to the Home page       |
+---------------------------------+"""

    malware_bypass = Color.yellow+"""[+] """+Color.green+"""(Home page/Malware Generator & Bypass AV)"""+Color.white+""" >
+------------------------------------------------------+
|             MALWARE GENERATOR & BYPASS AV            |
+------------------------------------------------------+
| [1] ZeroDoor   [2] Terminator   [3] WinPayloads      |
| [4] sAINT      [5] BeeLogger    [6] HackTheWorld     |
| [7] HatKey     [8] ezsploit     [9] trolo            |
| [10] GetWin    [11] TheFatRat   [12] DKMC            |
| [13] Parat     [14] mkvenom     [15] venom           |
| [16] Metasploit Framework       [17] Cloak           |
| [18] Metasploit AV Evasion      [19] AVET            |
| [20] AhMyth-Android-RAT         [21] NXcrypt         |
| [0] Back to the Home page                            |
+------------------------------------------------------+"""

    ddos_tools = Color.yellow+"""[+] """+Color.green+"""(Home page/DDoS Attacks)"""+Color.white+""" >
+----------------------------------------------+
|       (×﹏×)   DDOS ATTACKS   (×﹏×)         |
+----------------------------------------------+
| [1] slowloris    [2] ZAmbIE    [3] Airgeddon |
| [4] WebSploit    [5] UFONet    [6] zarp      |
| [7] Memcrashed-DDoS-Exploit                  |
| [0] Back to the Home page                    |
+----------------------------------------------+"""

    
    downloader_installer = Color.yellow+"""[+] """+Color.green+"""(Home page/Downloader & Installer)"""+Color.white+""" >
+----------------------------------------------+
|         DOWNLOADER & INSTALLERS  (⌒ω⌒)       |
+----------------------------------------------+
| [1] Fsociety    [2] Malicious     [3] Tool-X |
| [4] Katoolin    [5] IntRec-Pack   [6] ZAmbIE |
| [7] The PenTesters Framework      [8] Lunar  |
| [0] Back to the Home page                    |
+----------------------------------------------+"""

#                                             end