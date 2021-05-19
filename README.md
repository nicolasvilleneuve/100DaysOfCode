## FlightDealWebScraper
The following scrapes the web (namely, google flights) for flight deals from a major airport in Canada (Pearson) to several key travel destinations.



## Description
This app uses the power of object-oriented programming to scrape the web for flights, compare those prices to a price specified by the user (in a google sheet), and notfiy you via email and SMS if those prices 
are less than the values set in the google sheet. 
If you are an avid traveller, I would recommend uploading this code to pythonanywhere and scheduling a taks everyday (or so) for the same time such that you get a notification whenevr a place you want to go to, suddenly becomes an irresistable price). 

## Usage
You can freely access this app so long as you have a version of python 3 (this was made in python 3.9.1), the proper credentials to access the
sheety API, the tequila API, the Twilio API, SMTPLib (which, in order to use, you must enable thrid-party control of your chosen email account) 
the json module, the datetime module. While as I am aware I could simply export all of my credentials to the environment and pull those to make this program work directly with this code, 
that would compromise all of my credentials. 


Below, you will find figures to detail exactly what lines of code you need to change in order for this program to work for you too. 


The first batch of code that you will need to sub-out is lines 7 to 13 of the notifications_manager.py file. This is exemplified by Figure 1, below. 
<img src="https://github.com/nicolasvilleneuve/FlightDealWebScraper/blob/main/figures/Figure1.png" alt="Figure1">

Next, you will need to navigate to the flight_search.py file and fill-in your API key for usage of the tequila-API (exemplified by lines 6 and 7 of Figure 2, below).
<img src="https://github.com/nicolasvilleneuve/FlightDealWebScraper/blob/main/figures/Figure2.png" alt="Figure2">

Finally, you will need to navigate to the data_manager.py file and fill-in the endpoint for your google sheet (which is to contain you flight destination, destination code, and desired price). This is exemplified by line 5, or figure 3, below. 
<img src="https://github.com/nicolasvilleneuve/FlightDealWebScraper/blob/main/figures/Figure1.png" alt="Figure3"> 


## Contributing/Support
If you would like to create a PULL request, please feel free. Whether the intent be to pilfer from the code as you like some elements of the app, or to suggest improvements, you are most welcome to. If the changes are to be major, however, please open an issue first so we can discuss if/what you would like to change. Should you have a problem in doing so, please feel free to let me know (my email is on my website (nicolasvilleneuve.github.io/Portfolio or nicolasvilleneuve.pythonanywhere.com so please find it there in case it has changed since writing this).


## License
MIT License

Copyright (c) 2021 Nicolas Villeneuve

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
