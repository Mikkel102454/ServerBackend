#Start Minecraft Server
apt update 
apt install -y openjdk-21-jdk
apt install git
apt install make
git clone https://github.com/Tiiffi/mcrcon.git
cd mcrcon
make install
cd ..
cd files
sh start.sh