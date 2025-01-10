#Start Minecraft Server
apt update 
apt install -y openjdk-21-jdk
git clone https://github.com/Tiiffi/mcrcon.git
cd mcrcon
make
sudo make install
cd ..
cd files
sh start.sh