# amazon-price-tracker

Amazon price tracker is basically a python program where user gives link for a
particular product on amazon and the program fetches information from the given
link. This fetches current price of product and take 1 more input as user price. If
current price of product is less than the user price then program sends an mail on an
email address specified by user. In the mail user is given link to that particular
product and further he can buy the product.

If the price of product is higher the code will call check again function which will
basically update the price of product after every 20 sec . this will continue for infinite
times until current price becomes lesser than the user given price and comes out of
loop & finally sends an email to user.

# Modules & Libraries used

Tkinter is used to provide GUI to our mini project.
REQUESTS module is used to send HTTP requests and in return gives information
present on website. 
Using BEAUTIFULSOUP module, price is extracted from whole
bunch of information & 
SMTPLIB module is used here to send emails to user.
