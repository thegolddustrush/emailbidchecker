

Check bid price on ebay

Simple python script that runs in a loop until the price changes or you kill it at the terminal. 
Will check price every 5 minutes.
If the price changes it will send an email to the address configured in the email_bid.py file

How to use:
* Takes no arguments
* Update the file so the variables match your desired usage.

Variables to change:
oldamt = "21.98" # this is the current price
gmail_user = "youremail@gmail.com" #sends the email
gmail_pwd = "somepassword" #sends the email
to_addr = "anotheremail@gmail.com" #destination mail
#example url for auction item. can be any item auctioned on ebay
url = 'https://www.ebay.com/itm/LOT-OF-ACTION-FIGURE-CAPN-CAPTAIN-CRUNCH-Pirate-Jean-LaFoote-CEREAL-LOOSE/391994457903?hash=item5b44b0bf2f:g:1N8AAOSwNSxVXrqO'




Gotchas:

You may get a warning in your gmail that a less secure app tried to login. Please consult this page for more details about changing your security settings. https://support.google.com/a/answer/6260879?hl=en

This script uses a regular expression to get the price. Should probably use an api. In the future hope to make this change.

