# !python 3
# forex.py--A basic forex tool
# for detailed usages please refer to help.py

import sys, webbrowser, re
from retrievejson import exchg_rate
from help import HELPER_TEXT

# ----------helper code------
def quickcur(argv):
    ''' quickcur() : a function that helps translate single letters into currency codes
            argv (list) : takes in sys.argv
            return : a list of proper currency codes and prices in str   '''
    new_argv = argv
    for i in range(len(new_argv)):
        new_argv[i] = new_argv[i].upper()
        if new_argv[i] == 'T':
            new_argv[i] = 'TWD'
        if new_argv[i]== 'JP':
            new_argv[i] = "JPY"
        if new_argv[i] == 'EURO':
            new_argv[i] = 'EUR'
        if Money_val(new_argv[i]) != None:
            new_argv[i] = Money_val(new_argv[i])
    return new_argv

def Money_val(foo):
    '''
    This function translates quicktypes (e.g. B, M, K) into their actual number values with multiple 0s.
    :param foo (string) : command line argument
    :return: translated foo (int)
                or None if foo was not a money_val obj
    '''
    B_regobj = re.compile(r'(^\d+\.?\d*)(B)')
    M_regobj = re.compile(r'(^\d+\.?\d*)(M)')
    K_regobj = re.compile(r'(^\d+\.?\d*)(K)')
    W_regobj = re.compile(r'(^\d+\.?\d*)(W)')
    regobjs = [B_regobj, M_regobj, K_regobj, W_regobj]
    translator_d = {B_regobj:1000000000, M_regobj:1000000, K_regobj:1000, W_regobj:10000}
    for regobj in regobjs:
        mo = regobj.search(foo)
        if mo != None:
            temp = float(mo.group(1)) * translator_d[regobj]
            return int(temp)
    return None
##-----------end of helper code-----------------------
formatted_argv = quickcur(sys.argv) # format sys.argv input

# if len = 1 , the hot key functionality (USD/JPY for now)
if len(formatted_argv) == 1:
    rate = exchg_rate('USD', 'JPY')[2]
    print('The exchange rate for USD/JPY is '+ str(rate))
# if len = 2, run summary or help
if len(formatted_argv) == 2:
    if formatted_argv[1].lower() == 'summary':
        print('Opening forex news...')
        webbrowser.open('https://www.gloryskygroup.com/')
        webbrowser.open('https://www.gaitameonline.com/academy01.jsp')
        sys.exit()
    if formatted_argv[1].lower() == 'help':
        print(HELPER_TEXT)

# if len = 3, open currency info or else exchange rate
elif len(formatted_argv) == 3:
    #open currency info
    if formatted_argv[2].lower() == 'info':
        print('Opening info webpage for '+ formatted_argv[1] + '...')
        webbrowser.open('https://www.xe.com/'+formatted_argv[1])
    # print exchange rate
    else:
        from_cur_name, to_cur_name = formatted_argv[1], formatted_argv[2]
        APIdata = exchg_rate(from_cur_name,to_cur_name)
        from_cur_code, to_cur_code, rate = APIdata[0], APIdata[1], APIdata[2]
        print("The exchange rate for {}/{} is {}".format(APIdata[0],APIdata[1],APIdata[2]))
#   retrieve API and calculate the how much it is worth
elif len(formatted_argv) == 4:
    from_cur_name, to_cur_name = formatted_argv[2], formatted_argv[3]
    # gotta reverse
    APIdata = exchg_rate(from_cur_name,to_cur_name)
    from_cur_code, to_cur_code, rate = APIdata[0], APIdata[1], APIdata[2]
    thing_price = str(formatted_argv[1]) #string of numbers
    new_price = round(float(formatted_argv[1])*rate,2)
    def thd_separator(val):
        ''' This function adds commas as thousand separators
            val (int or float)
            return: string'''
        try:
            val_len = len(str(int(val)))
            q, r = divmod(val_len, 3)
            foo = list(str(int(val)))
            for i in range(q):
                foo.insert(r, ',')
                r +=4
            if foo[0] == ',':
                foo.pop(0)
            return ''.join(foo)
        except ValueError:
            return val
    thing_price = thd_separator(thing_price)
    new_price = thd_separator(new_price)
        
      
    print('{} {} is {} {}'.format(thing_price, from_cur_code,new_price, to_cur_code))
    # print("With exchange rate {}/{} : {}".format(APIdata[0], APIdata[1], APIdata[2]))

