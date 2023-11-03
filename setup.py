
import os
import subprocess
print("""
                 █        █
                █ █      █ █
               █   █    █   █


                 ▀▀▀▀▀▀▀▀▀▀
Tor SetUp For Ubuntu Linux
================================
* Email required ^_^
* Please beware that there are legal stuff involved with running a tor relay

I recommend you using a cloud service 
      
Note: Do not skid, you will get caught skidding ^_^

Author: mr.akz                                                        
""")
email = input("Please enter your email: ")
email = email.split()
if email != "":
    subprocess.run(["sudo", "apt", "update"])

    subprocess.run(["sudo", "apt-get", "install", "unattended-upgrades", "apt-listchanges"])

    with open("/etc/apt/apt.conf.d/50unattended-upgrades", "w") as f:
        f.write('Unattended-Upgrade::Allowed-Origins {"${distro_id}:${distro_codename}-security";"TorProject:${distro_codename}";};Unattended-Upgrade::Package-Blacklist {};Unattended-Upgrade::Automatic-Reboot "true";')


    with open("/etc/apt/apt.conf.d/20auto-upgrades", "w") as f:
        f.write('APT::Periodic::Update-Package-Lists "1";APT::Periodic::AutocleanInterval "5"; APT::Periodic::Unattended-Upgrade "1"; APT::Periodic::Verbose "1";')

    
    subprocess.run(["sudo", "apt", "install", "apt-transport-https"])

    subprocess.run(["sudo", "apt-get", "install", "lsb-release"])

    yourdistro = subprocess.check_output(["lsb_release", "-cs"]).decode().strip()

    with open("/etc/apt/sources.list.d/tor.list", "w") as f:
        f.write(f"deb [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org {yourdistro} main\ndeb-src [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org {yourdistro} main")

    subprocess.run(["wget", "-qO-", "https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc"], stdout=subprocess.PIPE)
    subprocess.run(["gpg", "--dearmor"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    subprocess.run(["sudo", "tee", "/usr/share/keyrings/tor-archive-keyring.gpg"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    subprocess.run(["sudo", "apt", "update"])

    subprocess.run(["sudo", "apt", "install", "tor", "deb.torproject.org-keyring"])

    with open("/etc/tor/torrc", "w") as f:
        f.write(f"Nickname\nContactInfo {email}\nORPort 443\nExitRelay 0\nSocksPort 0\n\n## BANDWIDTH\n## The config below has a maximum of 800GB\n## (up/down) per month, starting on the 1st\n## at midnight\nAccountingMax 800 GB\nAccountingStart month 1 0:00\n\n## MONITORING\n\nControlPort 9051\nCookieAuthentication 1")

    subprocess.run(["sudo", "systemctl", "enable", "tor"])
    subprocess.run(["sudo", "systemctl", "restart", "tor"])

    subprocess.run(["sudo", "apt", "install", "nyx"])



