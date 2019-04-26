#!/bin/bash -e
echo "----> run up containers ...."
cd stx/
docker-compose up -d
if [ $? -ne 0 ]; then
    echo "failed to run containers!"
    exit
fi
cd -

