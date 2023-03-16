# gfylitter
2 rudimentary wip python script to dump your gfycat links since the service stopped accepting uploads and is (allegedly) about to go offline.
the scripts DO NOT download files they only dump links, use a download manager to get your videos

## What you need
- some sort of programming knowledge to follow the instructions and mainly to clown on me for how badly written this thing is (i was in a hurry)
- python 3
- dependencies should just be requests and json, look them up on pypi
- gfycat account and gfycat developer API key

## Quick walkthrough
GFYCAT DEVELOPER SECTION:
- Go to: https://developers.gfycat.com/signup/#/apiform and request an API key which you will receive in an email, make sure to keep the app type "App" and to add "http://localhost" to the redirect URIs
- Copy your Client id and Secret from the email and place them where it says to do so inside the script you want to use

SCRIPT SECTION:
- Go to: "https://gfycat.com/oauth/authorize?client_id={{CLIENTIDHERE}}&scope=all&state=test&response_type=code&redirect_uri=http://localhost" and allow access
- You'll reach a dead page (unless you have a web server running in which case you might want to turn it off) which is intended. you must copy whatever string of characters you see on the address bar between the word "code=" and the "&" symbol
- Paste the string of characters you just got inside the script you want to use, replacing {insertoauthcode}
- repeat these steps everytime you want to use the script

GOOD LUCK