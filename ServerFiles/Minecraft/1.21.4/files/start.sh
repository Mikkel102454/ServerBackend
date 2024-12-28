javaRequired="21"
javaInstallLocation="/usr/lib/jvm/java-${javaRequired}-openjdk-amd64/bin/java"

maxRam="2G"
"${javaInstallLocation}" --version
"${javaInstallLocation}" -XshowSettings:properties -version 2>&1 | grep java.security

#"${javaInstallLocation}" -Xmx"${maxRam}" -Xms"${maxRam}" -jar server.jar nogui