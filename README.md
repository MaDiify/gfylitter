# gfylitter - Gfycat backup
2 rudimentary python script to dump your gfycat links since the service stopped accepting uploads and is (allegedly) about to go offline, which means that if in the process they block access to their API these scripts will become useless.
the scripts DO NOT download files they only dump links, use a download manager to get your videos (JDownloader 2 is a good one, some people use internet download manager too)

## What do the scripts do exactly?
- collection_scraper dumps in a text file every collection and giant.gfycat link inside it, your collections must not have any quotation mark or double quotation mark in them (") (')
- user_scraper dumps every single giant.gfycat link uploaded to your account in a text file, public or private, published or unpublished

- Why are you dumping giant.gfycat links and not just www.gfycat links? www.gfycat links have cloudflare ddos protection, giant.gfycat dont. 
- Why are there duplicate links? dont worry about it, the links are all there, your download manager will do the hard part

## What you need
- some sort of programming knowledge to follow the instructions and mainly to clown on me for how badly written this thing is (i was in a hurry to backup my stuff)
- python 3
- dependencies to download: only "requests"
- gfycat account and gfycat developer API key

## Quick walkthrough
GFYCAT DEVELOPER SECTION:
- Go to: https://developers.gfycat.com/signup/#/apiform and request an API key which you will receive in an email, make sure to keep the app type "App" and to add "http://localhost" to the redirect URIs
- Copy your Client id and Secret from the email and place them where it says to do so inside the script you want to use

SCRIPT SECTION:
- Go to: "https://gfycat.com/oauth/authorize?client_id={{CLIENTIDHERE}}&scope=all&state=test&response_type=code&redirect_uri=http://localhost", replacing {{CLIENTIDHERE}} with your client id and allow access to the script
- You'll reach a dead page (unless you have a web server running in which case you might want to turn it off) which is intended. You must copy whatever string of characters you see on the address bar between the word "code=" and the "&" symbol
- Paste the string of characters you just got inside the script you want to use, replacing {insertoauthcode}
- open a terminal window in the /scripts folder and just type python the_script_you_wanna_use.py
- repeat these steps everytime you want to use the script

GOOD LUCK
