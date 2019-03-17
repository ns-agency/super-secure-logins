#!/usr/bin/env bash

# Test 1 : Test if we can sql inject login

RES=$(php login.php "submit=&username=' OR 1=1--&password=")

if [[ "${RES}" == "SUCCESS" ]]; then
    echo "Test 1 failed; SQLi still present."
    exit 1
fi

# Test 2 : Test we can still login normally

RES=$(php login.php "submit=&username=admin&password=hizainthisisapassword")

if [[ "${RES}" != "SUCCESS" ]]; then
    echo "Test 2 failed; Regular login failed."
    exit 1
fi

