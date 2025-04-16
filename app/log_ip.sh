#!/bin/bash

set -e

jq -r '.timestamp, .ip_data.ip, .ip_data.country, .ip_data.city, .ip_data.org' ip.json | tee fetched_details.txt

awk 'NR==1{print "TimeStamp: "$0}
     NR==2{print "IP: "$0}
     NR==3{print "Country: "$0}
     NR==4{print "City: "$0}
     NR==5{print "ISP: "$0}' fetched_details.txt | tee ip_log.txt