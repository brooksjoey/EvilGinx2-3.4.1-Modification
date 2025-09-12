#!/bin/bash
# Monitoring script for EvilGinx2
while true; do
    systemctl status evilginx || systemctl restart evilginx
    sleep 30
done
