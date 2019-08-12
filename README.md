# Forex-tool

   Ever wondered how much something is in another currency? 
   Forex-tool is a simple script that can help you know that by typing one line!
## Forex-tool is a simple script runnable from the command line that can:
   1. Instantly convert currencies according to the current exchange rate(e.g. 200000 yen => 1800 USD) 
   2. Instantly open several websites (e.g. your favorite financial news sites)
   3. Instantly display exchange rates for designated currencies  
      **...all by typing one line!**
  
  For example, just type in your terminal:    
  *forex 200K JPY USD*   
  and it will return 200,000 JPY is 1800 USD, according to the immediate currency rates.
  
  or, type:     
  *forex summary*   
  and your favorite financial sites will be opened in your browser at once.       
  For more detailed descriptions of functions and usage commands, please refer to help.py 
  
---------------------------------------
## Getting started   
### Prerequisites   
   ```
    1. Python3  
    2. pip install requests
    3. Git (Optional)
  ```
### Installing 
 1. Open your command line terminal
 2. Clone or download the repository
   ```
     git clone https://github.com/jonkenobi/  
     or download and unzip the file  
  ```  
 3.Navigate to the root folder   
   ```   
     cd forex-tool
   ```   
   4.Type your command  
   (e.g. I want to know how much a room booked for 6000 yen is in USD)
   ```   
     forex 6K jpy usd 
  ```
   It may display something like:  
 ```
   6,000 JPY is 54 USD 
  ```
### Further Options
  #### Add the .bat file to path variables to make access even easier 
  1. Navigate to forex-tool/forex.bat
  2. Change the absolute file path to point to forex.py and copy it 
  3. Navigate to your computer's path variables and paste the absolute path to PATH
  ##### Done!
  Now you can either run your forex commands directly in the cmd 
  or press win+R and type your forex commands there!
