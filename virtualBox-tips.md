# VirtualBox tips - things I've had to solve

## Getting network access

#### On windows

1st in windows, cmd.exe

> ping www-cache-n

return will be something like:

> Pinging www-cache-n.xuclh.nhs.uk [9.18.7.10] with 32 bytes of data:  
Reply from 9.18.7.10: bytes=32 time=1ms TTL=61  
Reply from 9.18.7.10: bytes=32 time<1ms TTL=61  

The IP address 9.18.7.10 (or whatever your computer returns is the address of the proxy).  VirtualBox can’t seem to resolve the translation from www-cache-n to this address which seems to be why all the tips online don’t work.  
Using this ip address rather than www-cache-n is what ended up working for me.

Based on various internet search, you need to make the following changes to files (I’ve made them all, you may be able to get away with fewer).  Replace:

> [username]:[password]@[proxy address]:[port]  

in the listed additions with your own medphysnt username and password version of:

> agosling:pa55W0rd@9.18.7.10:3128




#### Files to change in Linux
All changes need to be made as sudo  (for the vGate you are already an account with sudo access, the password is virtual).

###### /etc/apt/apt.conf.d/95proxies

>Acquire::http::Proxy "http://\<username>:\<password>@\<proxy address>:\<port>/";  
Acquire::https::Proxy "http://\<username>:\<password>@\<proxy address>:\<port>/";  
Acquire::ftp::Proxy "ftp://\<username>:\<password>@\<proxy address>:\<port>/";  



###### /etc/environment

>export http_proxy="http://\<username>:\<password>@\<proxy address>:\<port>/"  
export https_proxy="http://\<username>:\<password>@\<proxy address>:\<port>/"  
export ftp_proxy="http://\<username>:\<password>@\<proxy address>:\<port>/"  
no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"  
export HTTP_PROXY="http://\<username>:\<password>@\<proxy address>:\<port>/"  
export HTTPS_PROXY="http://\<username>:\<password>@\<proxy address>:\<port>/"  
export FTP_PROXY="http://\<username>:\<password>@\<proxy address>:\<port>/"  
NO_PROXY="localhost,127.0.0.1,localaddress,.localdomain.com"



###### ~/.bash_aliases

>export http_proxy=http://\<username>:\<password>@\<proxy address>:\<port>  
export https_proxy=https://\<username>:\<password>@\<proxy address>:\<port>  



###### /etc/profile.d/proxy.sh

>export http_proxy=http://\<username>:\<password>@\<proxy address>:\<port>  
export https_proxy=https://\<username>:\<password>@\<proxy address>:\<port>  



###### /etc/wgetrc

>http_proxy = http://\<username>:\<password>@\<proxy address>:\<port>  
https_proxy = https://\<username>:\<password>@\<proxy address>:\<port>  
