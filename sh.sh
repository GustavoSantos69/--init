 systemctl is-active mariadb > /dev/null 2>&1
 sudo systemctl is-active postgresql > /dev/null 2>&1

MARIADB_ACTIVE=$?
POSTGRESQL_ACTIVE=$?

if  [[ "$MARIADB_ACTIVE" -eq 0 ]]; 
 then mysql; 
elif  [[ "$POSTGRESQL_ACTIVE" -eq 0 ]]; 
 then psql; 
else sqlite3; 
fi


#!/bin/bash

a=5
b=10

if [ $a -ne $b ]; then
    echo "Os valores não são iguais."
else
    echo "Os valores são iguais."
fi



vim=$?
 if [["$vim" -ne 0]];
  then vim; fi


  for HOST in servera serverb
do
ssh student@${HOST} hostname
done


#!/bin/bash

for file in *.txt; do
    echo "Arquivo encontrado: $file"
done

#!/bin/bash

count=5
while [ $count -gt 0 ]; do
    echo "Contagem regressiva: $count"
    ((count--))
done

#!/bin/bash

read -p "Digite um número: " num

if [ $num -gt 0 ]; then
    echo "Número é positivo."
elif [ $num -lt 0 ]; then
    echo "Número é negativo."
else
    echo "Número é zero."
fi

