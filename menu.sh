while true; do
    echo "1. Open video2imgs/start.sh"
    echo "2. Open img2ascii/start.sh"
    read -p "Select number (1/2): " choice

    case "$choice" in
        1)
            cd video2imgs
            ./start.sh
            break
            ;;
        2)
            cd img2ascii
            ./start.sh
            break
            ;;
        *)
            echo "Wrong Answer!"
            ;;
    esac
done
