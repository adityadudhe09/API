#!/bin/bash

set -e

jq -r '.timestamp, .ip_data.ip, .ip_data.country, .ip_data.city, .ip_data.org' ip.json | tee fetched_details.txt

# awk 'NR==1{print "TimeStamp: "$0}
#      NR==2{print "IP: "$0}
#      NR==3{print "Country: "$0}
#      NR==4{print "City: "$0}
#      NR==5{print "ISP: "$0}' fetched_details.txt | tee ip_log.txt

jq -r '"TimeStamp: \(.timestamp),\nIP: \(.ip_data.ip),\nCountry: \(.ip_data.country),\nCity: \(.ip_data.city),\nISP: (.ip_data.org)"' ip.json | tee ip_log.txt