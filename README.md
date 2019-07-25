# PaylocityBot
This bot will help you automatically log into your Paylocity account. It basically saves time and energy typing the username and password again and again. It also has been enhanced to punch in the correct punch type of your choice at a predetermined time.

## Set up
- Install Python3 (recommend using Homebrew) 
- Install [Selenium](https://pypi.org/project/selenium/) using `pip3 install selenium`
- Create a copy of the `config.example.py` and rename it as `config.py` with all your credentials updated in it
- Follow the instructions in `payrollBot.py` file to update the time and uncomment the desired button lines.

The automation steps from here largely depends on your browser of choice. 

If you plan to use Chrome...
- You will need Chrome Driver to help run the automation steps. Download the one that suits your browser directly from Google: https://sites.google.com/a/chromium.org/chromedriver/downloads
- Unzip the chrome driver and find the path to the executable file. You will paste this into the `config.py` file

If you plan to use Safari...
- For Safari, Preferences > Advanced Tab > check Show Develop menu in menu bar. Go to Develop menu > check Allow Remote Automation
- Change `webdriver.Chrome(config.LOGIN_CONFIG['pathtodriver'])` to just `webdriver.Safari()`

Finally:
- Run `python3 payrollBot.py` in the root directory of this repo

Note: You may need to log first to ensure security question will let you trust this device.


*Disclaimer: Companies, employers, nor the author of this bot be responsible for any errors and/or issues that arise from using this. Please use responsibly.*
