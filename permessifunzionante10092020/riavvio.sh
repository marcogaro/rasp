#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: destroy_virtual_rasp.sh <virtual_rasp_name>"
    exit;
fi

nome=$1


echo nome della raspberry: $nome
#read name

file=passt3.5




#echo "qual è il nome della raspberry per cui riavviare il filesystem? "
#read -r nome



sudo rm -rf $file.$nome.py

#creo passt
sed 's/test2/'$nome'/g' example.py > $file.$nome.py



pass=""$file"."$nome".py"
echo $pass



echo "restarting filesystem "$nome"!"

sudo umount --force /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio
sudo umount --force /gpio_mnt/"$nome"/sys/class/gpio

sudo umount --force /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio
sudo umount --force /gpio_mnt/"$nome"/sys/class/gpio


python3 "$pass" /sys/devices/platform/soc/3f200000.gpio /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio/ &
python3 "$pass" /sys/class/gpio/ /gpio_mnt/"$nome"/sys/class/gpio/ &
