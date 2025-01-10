#Start Minecraft Server
# INSTAL JAVA
cd /
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
cd /files
sh start.sh