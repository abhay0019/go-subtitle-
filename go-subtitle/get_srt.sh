IFS_BAK=$IFS
IFS="
"

for line in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
        full_path="/home/"$USER"/Desktop/py/go-subtitle/"go_subtitle.py
        python $full_path $line 
        if [ $? -eq 0 ];then
        notify-send $line
        else
        notify-send "Sorry ! Not Present in Our Database"
        fi
done

IFS=$IFS_BAK
