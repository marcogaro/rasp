#!/bin/bash

#if [ "$#" -ne 1 ]; then
  #  echo "Usage: destroy_virtual_rasp.sh <virtual_rasp_name>"
 #   exit;
#fi

#name=$1


#echo nome della raspberry?
#read name


pass=passt3.5


echo "qual è il nome della raspberry da eliminare? "
read -r nome



echo "Destroying virtual rasp "$nome"!"




sudo umount /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio
sudo umount /gpio_mnt/"$nome"/sys/class/gpio

sudo rm -rf $pass.$nome.py

sudo umount /gpio_mnt/sys/devices/platform/soc/soc\:firmware/soc\:firmware\:expgpio/gpio/gpiochip504/
sudo umount --force /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio
sudo umount --force /gpio_mnt/"$nome"/sys/class/gpio

sudo umount --force /gpio_mnt/sys/devices/platform/soc/soc\:firmware/soc\:firmware\:expgpio/gpio/gpiochip504/

lxc config device remove "$nome" gpio disk 
lxc config device remove "$nome" devices disk
lxc config device remove "$nome" soc disk
lxc config device remove "$nome" firmware disk
lxc config device remove "$nome" bus disk

sudo rm -rf /gpio_mnt/"$nome"
#sudo rm -rf /gpio_mnt/
sudo rm -rf /tmp/passthrough/

lxc delete --force "$nome"
