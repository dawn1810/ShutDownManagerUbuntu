#!/bin/bash

case $1 in
    shutdown)
        echo "Shutting down the system..."
        shutdown now
        ;;
    restart)
        echo "Restarting the system..."
        shutdown -r now
        ;;
    suspend)
        echo "Suspending the system..."
        systemctl suspend
        ;;
    logout)
        echo "Logging out..."
        gnome-session-quit --logout --no-prompt
        ;;
    *)
        echo "Invalid action specified!"
        ;;
esac

