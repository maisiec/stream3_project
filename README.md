# Stream 3 Project - Wayv Videos 


## Overview 

This app is a Media Hub where users can purchase old Hi 8 video footage for personal use. 

### What does it do?

This website is a media hub where users can browse through and purchase old video footage for personal use. 

### How does it work
- The app uses the Django framework which is written on Python. 
- Paypal is also used allowing users to carry out simple transactions through their Paypal accounts. 
- This app uses the default db Sqlite3.


#Features
- Landing home page featuring images taken from stock video footage found on the products page. 
- ability to register an account, login and out.
- products page populated with stock footage user can purchase 
- ability to view each seperate product stock video description and purchase.
- ability to add products to a cart.
- ability to checkout cart and purchase videos.
- ability to download videos once purchased. 
- about page describing the website purpose.
- user accout showing previous orders where user can also download orders.
- static and media files hosted on Amazon S3 to host videos properly with heroku.
- ability to fill out and send a contact form for any questions.
- footer navigation.

### Features Left to Implement / Improve on
- imrpove secruity of accessing download videos. 



## Tech Used
### Some the tech used includes:
- [Django](https://www.djangoproject.com/)
    -  **Django** is used to handle page routing, create additional apps, make calls to the REST API and build custom directives.
- [Python](https://www.python.org/)
  	- **Pyton** lets you work quickly
	and integrate systems more effectively
- [Pip](https://pip.pypa.io/en/stable/)
  - **pip** pip is a package management system used to install and manage software packages written in Python.
-[Bootstrap](http://getbootstrap.com/)
	- **Bootstrap** to give the website a simple, responsive layout. 
- [PayPal](https://developer.paypal.com/developer/accounts/)
  - **PayPal Sandbox** The PayPal Sandbox is a self-contained, virtual testing environment that mimics the live PayPal production environment. Providing a shielded space where you can initiate and watch your application process the requests you make to the PayPal APIs without touching any live PayPal accounts.
-[Amazon S3](https://aws.amazon.com/s3/)
 - **Amazon S3** Amazon S3 stores data as objects within resources called "buckets". You can store as many objects as you want within a bucket, and write, read, and delete objects in your bucket.


## Testing
- Django testing
- cross browser / platform testing. 

## Credits
- modified Codrops [gridlayout](https://github.com/codrops/GridLayoutSlideshow/) for home page.
- Shopping Cart [Django By Example - Antonio Mele](http://djangobyexample.com/) followed this and modified to fit project
