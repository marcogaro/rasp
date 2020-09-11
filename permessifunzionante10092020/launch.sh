#!/bin/bash

echo "scegli tra test1 test2 test3 test4: "

file=passt3.5

read -r b
#echo $b


   if [ "$b" == "test1" ]
   	then
     	nome="test1"
	pass=""$file"."$nome".py"
     	echo "$nome"
	echo "$pass"
   elif [ "$b" == 'test2' ]
	then
	nome="test2"
	pass=""$file".""$nome"".py"
     	echo $nome
	echo "$pass"
   elif [ "$b" == 'test3' ]
	then
	nome="test3"
	pass=""$file"."$nome".py"
     	echo "$nome" 
	echo "$pass"
   elif [ "$b" == 'test4' ]
	then
	nome="test4"
	pass=""$file"."$nome".py"
     	echo $nome
	echo "$pass"
   else
   	echo "errore" 
   	exit
   fi  
   
   
   echo $nome
   echo "$pass"
   
   

sudo rm -rf $file.$nome.py

#creo passt
sed 's/test2/'$nome'/g' example.py > $file.$nome.py


#aggiorno i permessi
#sudo groupadd gpio
#sudo chgrp gpio -R /sys/class/gpio/
#sudo chmod 777 -R /sys/class/gpio/




 #distruggo container nel caso fosse già attivo
   
   echo "Destroying virtual rasp "$nome"!"

sudo umount /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio
sudo umount /gpio_mnt/"$nome"/sys/class/gpio
sudo umount --force /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio
sudo umount --force /gpio_mnt/"$nome"/sys/class/gpio


lxc config device remove "$nome" gpio disk 
lxc config device remove "$nome" devices disk
lxc config device remove "$nome" soc disk

sudo rm -rf /gpio_mnt/"$nome"
sudo rm -rf /tmp/passthrough/
lxc delete --force "$nome"
   
   
   
lxc list   
   













#da qui creo container

echo "Creating virtual rasp "$nome"!"

lxc launch ubuntu:16.04 "$nome"

#MYUID=`sudo ls -l /home/ubuntu/storage/containers/"$nome"/rootfs/ | grep root | awk '{}{print $3}{}'`

lxc exec "$nome" -- addgroup gpio
sleep 20
lxc exec "$nome" -- usermod -a -G gpio ubuntu
sleep 1
#MYGID=$(($MYUID + `lxc exec "$nome" -- sed -nr "s/^gpio:x:([0-9]+):.*/\1/p" /etc/group`))
#echo $MYGID $MYUID

sudo mkdir -p /gpio_mnt/"$nome"
sudo chmod 777 -R /gpio_mnt/"$nome"
sudo mkdir -p /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio
sudo mkdir -p /gpio_mnt/"$nome"/sys/class/gpio

sudo mkdir -p /gpio_mnt/"$nome"/sys/devices/platform/soc/soc\:firmware/soc\:firmware\:expgpio/gpio/gpiochip504/

#sudo chown "$MYUID"."$MYGID" -R /gpio_mnt/test2/sys/

lxc exec "$nome" -- mkdir -p /gpio_mnt/sys/class/gpio
lxc exec "$nome" -- mkdir -p /gpio_mnt/sys/devices/platform/soc/3f200000.gpio

lxc exec "$nome" -- mkdir -p /gpio_mnt/sys/devices/platform/soc/soc\:firmware/soc\:firmware\:expgpio/gpio/gpiochip504/

lxc exec "$nome" -- mkdir -p /gpio_mnt/sys/firmware/devicetree/base/soc/gpio@7e200000/

lxc exec "$nome" -- mkdir -p /gpio_mnt/sys/bus/gpio/
#######################################
lxc exec "$nome" -- mkdir -p /gpio_mnt/sys/bus/platform/drivers/
lxc exec "$nome" -- mkdir -p /gpio_mnt/sys/bus/platform/




sudo chmod -R 777 /gpio_mnt/"$nome"

#lxc config set test2 raw.idmap "both 1000 1000000"
lxc config set "$nome" security.privileged true
lxc restart "$nome"

lxc config device add "$nome" gpio disk source=/gpio_mnt/"$nome"/sys/class/gpio path=/gpio_mnt/sys/class/gpio
lxc config device add "$nome" devices disk source=/gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio path=/gpio_mnt/sys/devices/platform/soc/3f200000.gpio

lxc config device add "$nome" soc disk source=/sys/devices/platform/soc/soc\:firmware/soc\:firmware\:expgpio/gpio/gpiochip504/ path=/gpio_mnt/sys/devices/platform/soc/soc\:firmware/soc\:firmware\:expgpio/gpio/gpiochip504/

#lxc config device add "$nome" firmware disk source=/sys/firmware/devicetree/base/soc/gpio@7e200000/ path=/gpio_mnt/sys/firmware/devicetree/base/soc/gpio@7e200000/

#lxc config device add "$nome" bus disk source=/sys/bus/gpio/ path=/gpio_mnt/sys/bus/gpio/


sleep 2
#wget https://raw.githubusercontent.com/marcogaro/rasp/master/permessifunzionante24082020/pass1.4chesembrafunzionare.py -P /tmp/passthrough/
#cd /tmp/passthrough/

ls

sudo chmod -R 777 /sys/class/gpio/
sudo chmod -R 777 /sys/devices/platform/soc/
#sudo chmod -R 777 /gpio_mnt/
sudo chmod -R 777 /gpio_mnt/"$nome"
sudo chmod -R 777 /gpio_mnt/"$nome"/sys/

sudo groupadd gpio
sudo chgrp gpio -R /sys/class/gpio/

sleep 10

python3 "$pass" /sys/devices/platform/soc/3f200000.gpio /gpio_mnt/"$nome"/sys/devices/platform/soc/3f200000.gpio/ &
python3 "$pass" /sys/class/gpio/ /gpio_mnt/"$nome"/sys/class/gpio/ &



#sudo chown "$MYUID"."$MYGID" -R /gpio_mnt/test2/sys/

cd

lxc exec "$nome" -- su --login ubuntu -l
#lxc exec test2 bash

#adduser utente
#adduser utente gpio
#su - utente
