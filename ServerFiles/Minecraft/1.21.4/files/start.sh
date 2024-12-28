javaRequired="21"
javaInstallLocation="/usr/lib/jvm/java-${javaRequired}-openjdk-amd64/bin/java"

maxRam="2G"

"${javaInstallLocation}" -Xmx"${maxRam}" -Xms"${maxRam}" -jar server.jar nogui