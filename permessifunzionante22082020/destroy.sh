
#!/bin/bash

#if [ "$#" -ne 1 ]; then
  #  echo "Usage: destroy_virtual_rasp.sh <virtual_rasp_name>"
 #   exit;
#fi

#name=$1


#echo nome della raspberry?
#read name



echo "il nome della raspberry è test2 !"



echo "Destroying virtual rasp "test2"!"

sudo umount /gpio_mnt/test2/sys/devices/platform/soc/3f200000.gpio
sudo umount /gpio_mnt/test2/sys/class/gpio
sudo umount /gpio_mnt/sys/devices/platform/soc/soc\:firmware/soc\:firmware\:expgpio/gpio/gpiochip504/
sudo umount --force /gpio_mnt/test2/sys/devices/platform/soc/3f200000.gpio
sudo umount --force /gpio_mnt/test2/sys/class/gpio

sudo umount --force /gpio_mnt/sys/devices/platform/soc/soc\:firmware/soc\:firmware\:expgpio/gpio/gpiochip504/

lxc config device remove test2 gpio disk 
lxc config device remove test2 devices disk
lxc config device remove test2 soc disk

sudo rm -rf /gpio_mnt/test2
sudo rm -rf /gpio_mnt/
sudo rm -rf /tmp/passthrough/
lxc delete --force test2
