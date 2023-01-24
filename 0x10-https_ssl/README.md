## Tasks on HTTPS SSL

### 0. World wide web 

- Add subdomains to domain and write a bash script that must use: 
1. awk
2. at least one Bash function

- Your Bash script must accept 2 arguments:

* domain:
type: string
what: domain name to audit
mandatory: yes

* subdomain:
type: string
what: specific subdomain to audit
mandatory: no

* Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]

### 1. HAproxy SSL termination

* *Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain*

- Requirements:

HAproxy must be listening on port TCP 443
HAproxy must be accepting SSL traffic
HAproxy must serve encrypted traffic that will return the / of your web server
When querying the root of your domain name, the page returned must contain Holberton School
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 1-haproxy_ssl_termination must be your HAproxy configuration file

### 2. No loophole in your website traffic

* *Configure HAproxy to automatically redirect HTTP traffic to HTTPS.*

- Requirements:

This should be transparent to the user
HAproxy should return a 301
HAproxy should redirect HTTP traffic to HTTPS
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
