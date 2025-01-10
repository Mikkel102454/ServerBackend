#Start Minecraft Server
apt update 
apt install -y openjdk-21-jdk
apt install golang
go install github.com/Tiiffi/mcrcon@latest
cd files
sh start.sh