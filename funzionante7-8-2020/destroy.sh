#!/bin/bash

echo "il nome della raspberry è test2 !"

echo "Destroying virtual rasp "test2"!"

sudo umount /gpio_mnt/test2/sys/devices/platform/soc/3f200000.gpio
sudo umount /gpio_mnt/test2/sys/class/gpio
sudo umount --force /gpio_mnt/test2/sys/devices/platform/soc/3f200000.gpio
sudo umount --force /gpio_mnt/test2/sys/class/gpio

lxc config device remove test2 gpio disk 
lxc config device remove test2 devices disk

sudo rm -rf /gpio_mnt/test2
sudo rm -rf /gpio_mnt/
sudo rm -rf /tmp/passthrough/
lxc delete --force test2
