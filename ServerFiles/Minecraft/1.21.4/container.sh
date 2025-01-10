#Start Minecraft Server
# INSTAL JAVA
apt update 
apt install -y openjdk-21-jdk
# INSTALL MCRCON
apt install -y gcc build-essential make git
git clone https://github.com/Tiiffi/mcrcon.git
cd ./mcrcon
make
make install
# START SERVER
pwd
cd ..
ls
cd files
sh start.sh