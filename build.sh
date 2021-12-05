#!/usr/bin/env bash
# ./build.sh 0 for prod
# ./build.sh 1 for dev

DEBUG=$1 npm run start
cp dist/content.js .
zip lightsaber.zip content.js manifest.json img/storelogo.png