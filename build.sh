#!/usr/bin/env bash
npm run start
cp dist/content.js .
zip lightsaber.zip content.js manifest.json img/storelogo.png