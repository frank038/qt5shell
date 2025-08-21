#!/bin/bash
# echo `lsof /dev/video0|grep video0`
echo `lsof /dev/$1|grep $1`
