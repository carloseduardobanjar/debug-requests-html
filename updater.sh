#!/bin/bash

python3 Updater.py &

PYTHON_PID=$!

print_process_info() {
    echo "Informações do processo PID $PYTHON_PID:"
    ps -p $PYTHON_PID -o pid,etime,%cpu,%mem,cmd
    sudo netstat -anp | grep $PYTHON_PID
    echo "-----------------------------------"
}

while kill -0 $PYTHON_PID 2> /dev/null; do
    print_process_info
    sleep 60
done

echo "O processo PID $PYTHON_PID foi concluído."
print_process_info