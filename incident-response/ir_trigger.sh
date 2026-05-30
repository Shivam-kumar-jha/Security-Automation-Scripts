#!/bin/bash

ALERT_FILE=$1

if grep -q "bruteforce" "$ALERT_FILE"; then

    echo "[+] Incident Type: Brute Force"

    echo "[+] Step 1: Verify source IP"

    echo "[+] Step 2: Review failed logon activity"

    echo "[+] Step 3: Check account lockout status"

    echo "[+] Step 4: Escalate to SOC Analyst"

fi
