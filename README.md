# FormBruteforcer

A simple script to brute force wordpress logins using a caesar cipher encoder.

Requires chromedriver to work, of which the latest version can be found here: http://chromedriver.chromium.org/downloads
Simply put the driver in the same folder as the scripts, and you are done with the setup :)


# Usage:
1. Put the words you wish into the file "unEncodedWordlist.txt", which is located in the wordlists folder.
2. Run the "Caesar encoder" script
3. Change the username in the "BruteForce" script
4. Change the URL in the "BruteForce" script
4. Run the "BruteForce" script.

The script will then have converted the passwords in the "unEncodedWordlist.txt", encode them, and put them in "EncodedWordlist.txt". The brute force script will then use this list as the passwords for the user you defined, and run the script towards the defined URL.

This script is only for educational and ethical purposes!! usage in other areas are not endorsed by BadNameException.
