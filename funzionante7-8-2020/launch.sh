#!/bin/bash

#lxd init

echo "Creating virtual rasp "test2"!"

lxc launch ubuntu:16.04 test2

MYUID=`sudo ls -l /home/ubuntu/storage/containers/test2/rootfs/ | grep root | awk '{}{print $3}{}'`

lxc exec test2 -- addgroup gpio
sleep 20
lxc exec test2 -- usermod -a -G gpio ubuntu
sleep 1
MYGID=$(($MYUID + `lxc exec test2 -- sed -nr "s/^gpio:x:([0-9]+):.*/\1/p" /etc/group`))
echo $MYGID $MYUID

sudo mkdir -p /gpio_mnt/test2
sudo chmod 777 -R /gpio_mnt/
sudo mkdir -p /gpio_mnt/test2/sys/devices/platform/soc/3f200000.gpio
sudo mkdir -p /gpio_mnt/test2/sys/class/gpio

lxc exec test2 -- mkdir -p /gpio_mnt/sys/class/gpio
lxc exec test2 -- mkdir -p /gpio_mnt/sys/devices/platform/soc/3f200000.gpio

sudo chmod -R 777 /gpio_mnt/

lxc config set test2 security.privileged true
lxc restart test2

lxc config device add test2 gpio disk source=/gpio_mnt/test2/sys/class/gpio path=/gpio_mnt/sys/class/gpio
lxc config device add test2 devices disk source=/gpio_mnt/test2/sys/devices/platform/soc/3f200000.gpio path=/gpio_mnt/sys/devices/platform/soc/3f200000.gpio


sleep 5
wget https://raw.githubusercontent.com/marcogaro/rasp/master/pass3.py -P /tmp/passthrough/
cd /tmp/passthrough/

ls

sudo chmod -R 777 /sys/class/gpio/
sudo chmod -R 777 /sys/devices/platform/soc/
sudo chmod -R 777 /gpio_mnt/
sudo chmod -R 777 /gpio_mnt/test2/sys/

sleep 10

python3 pass3.py /sys/devices/platform/soc/3f200000.gpio /gpio_mnt/test2/sys/devices/platform/soc/3f200000.gpio/ &
python3 pass3.py /sys/class/gpio/ /gpio_mnt/test2/sys/class/gpio/ &
#sudo chown "$MYUID"."$MYGID" -R /gpio_mnt/test2/sys/

cd

lxc exec test2 -- su --login ubuntu -l
