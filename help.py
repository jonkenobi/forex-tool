# forex.py is a basic forex tool that can retrieve currency exchange rates and
#               show a cash value in another currency
# After download, open in terminal and navigate to the root directory.
# Then type the following commands for the functions!
HELPER_TEXT = '''Commands: forex --- Retrieve USD/JPY rates
                           forex  <From currency> <To currency>: Retrieve from/to currency rate
                           forex  <num> <From currency> <To currency>:  Show how much <num> <From currency>
                              is  in <To currency>
                           forex <currency> info: open xe.com's detail info on that currency
                           forex summary: open gloryskygroup HP 
                           forex help: print usage document
                               *all currencies are expressed in codes 
                               *K,M,B can be used equally as thousand, million, billion
                               e.g. entering 3M is the same as entering 3000000'''