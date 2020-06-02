#ebaytracker

A simple Python script that checks the price of a eBay listing and notifies you via email when the price hits a threshold.
Relies on SMTP and is currently designed around Gmail but can be adapted for other mail services.

Guide:

To use the script you must change the url to your desired listing, change the email to your email (authorization for less 
trusted apps must be enabled) and include the password. Change the time parameter that checks every certain seconds (defaults
24 hours) Change the threshold and run the script in the background or manually run it.

Once the threshold is met an email from yourself will notify you of the price drop alongside your provided link.
