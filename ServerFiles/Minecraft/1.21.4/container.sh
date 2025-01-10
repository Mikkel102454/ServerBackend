#Start Minecraft Server
cd /
apt update 
apt install -y openjdk-21-jdk
apt install -y gcc build-essential make git
git clone https://github.com/Tiiffi/mcrcon.git
cd ./mcrcon
pwd
ls
make
make install
cd ..
pause
cd files
sh start.sh