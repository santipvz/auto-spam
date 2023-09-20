# AUTO-SPAM

This script allows you to send a message multiple times using pyautogui. 
You can specify the message you want to send and the number of times it
will be sent. If the message is a number, it will send a sequence of numbers
from 1 to the specified number. If the message is not numeric, it will be sent
as-is

 \> S1
 
 ACTG

En este caso, el archivo contiene una única secuencia cuyo identificador es 'S1' y la secuencia de ADN es 'ACTG'. Como se mencionó anteriormente, un archivo puede tener varias secuencias y, a su vez, cada secuencia puede tener su contenido distribuido en varias líneas. Veamos otro ejemplo:

\> S1

ACTGAT

\> S2

AACCGC

En este caso, el archivo contiene dos secuencias con identificadores 'S1' y 'S2', y las secuencias de ADN son 'ACTGAT' y 'AACCGC' respectivamente (como puedes observar, las líneas que siguen al encabezado se juntan en una sola cadena que representa la secuencia completa). 

# Algunos comandos de uso
Cambiar nombre o formato de un archivo
>python fasta_format.py --input=test_1.fasta --output=test1.fasta --case=lower --maxLength=2

Renombrar cadenas con el mismo ID
>python disambiguate.py --input=test_3.fasta --output=test2.fasta --mode=rename

Eliminar cadenas con el mismo ID
>python disambiguate.py --input=test_3.fasta --output=test2_1.fasta --mode=remove

Obtener una cadena revertida y complementada
>python reverse_complement.py --input=test_3.fasta --output=test3.fasta --mode=both

Obtener la cadena complementaria de una dada
>python reverse_complement.py --input=test_4.fasta --output=test4.fasta --mode=complement 

Obtener la cadena revertida de una dada
>python reverse_complement.py --input=test_4.fasta --output=test4.fasta --mode=reverse

Obtener datos de un archivo en formato csv (Cantidad de A,C,T,G...) con la opción de mostrar gráficas de estos datos (--extra-plots-dir es un argumento opcional)
>python fasta_summary.py --input=INPUT --output=CSV_OUTPUT --extra-plots-dir=GRAPHS_OUTPUT
