#! /bin/bash

password=$1

output="$(sshpass -p $password ssh -o StrictHostKeyChecking=no 10.225.147.156 -p 2222)"
echo "${output}"

