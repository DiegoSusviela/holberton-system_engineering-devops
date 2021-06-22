#!/usr/bin/env bash
# asdfasda asd

echo "$$" > "/var/run/holbertonscript.pid"
trap "rm -f /var/run/holbertonscript.pid & exit 0" SIGQUIT
trap "rm -f /var/run/holbertonscript.pid & echo I hate the kill command & exit 0" SIGTERM
trap "echo Y U no love me?! & exit 0" SIGINT
while true; do
    echo "To infinity and beyond"
    sleep 2
done
