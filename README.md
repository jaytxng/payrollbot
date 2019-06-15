# PaylocityBot
This bot will help you automatically log into your Paylocity account. It basically saves time and energy typing the username and password again and again. It also has been enhanced to punch in the correct punch type of your choice at a predetermined time.

## Set up
- Install Python3 (recommend using Homebrew) 
- Install [Selenium](https://pypi.org/project/selenium/) using `pip3 install selenium`
- Create a copy of the `config.example.py` and rename it as `config.py` with all your credentials updated in it
- Follow the instructions in `payrollBot.py` file to update the time and uncomment the desired button lines
- Currently it uses Safari webdriver, but feel free to change this if you want
- For Safari, Preferences > Advanced Tab > check Show Develop menu in menu bar. Go to Develop menu > check Allow Remote Automation
- Run `python3 payrollBot.py` in the root directory of this repo

Note: Make sure you log in within the hour to ensure security question will let you trust this device.


*Disclaimer: Companies, employers, nor the author of this bot be responsible for any errors and/or issues that arise from using this. Please use responsibly.*
