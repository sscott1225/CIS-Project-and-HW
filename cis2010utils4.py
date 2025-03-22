# cisutils.py
__all__ = ['StartHere','EndHere'
           'console','nchar', 'paste',
           'showBits','showNum','ToShell',
           'h32','hecho','strhash','runsql']
# Module of support functions for CIS2010, version 3  (Dec 6, 2022)
# Module of support functions for CIS2010, version 4  (April 6, 2023)
z_utils = "v4.2"
# Author: Kurt Schmitz (c) 2022, 2023
#
#
#
from datetime import datetime
from sys import platform
import pandas as pd
import os
# Global Variables
#global z_MyName
#global z_now
#global DateTime
#global z_path
#global z_os
#global z_osn
z_MyName = ""
z_task = ""
z_now = datetime.now()
DateTime = type(z_now)
z_path = os.path.expanduser('~')
z_os = platform
z_osn = os.name
z_cks = 0
z_sess = ""
z_un = ""
z_hek = ""
#
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FGRED = '\033[31m'
    FGGREEN = '\033[32m'
    FGBLUE = '\033[34m'
    FGMAGENTA = '\033[35m'
    BGYELLOW = '\033[43m'
#
#
# Functions:
#    StartHere( sname,session, task)  - function to create basic variables
#    EndHere( sname, atd)     - function to store variables for grading
#    ShowBits( data )         - function to return bits for a character
#    h32( str )
#    hecho(msg)
#    strhash( msg )
#    runsql(  msg )

######################### runsql
def runsql( s, db_conn ) :
    dframe = 'SQL Error'
    try :
        dframe = pd.read_sql(s , db_conn)
        print( "\nSQL results\n", dframe)
    except :
        if len(s.lstrip()) :
            print(bcolors.FGRED + "\nYour SQL statement has an error that must be fixed" + bcolors.OKBLUE )
            print( s )
            print(bcolors.FGRED + " " + "Start by checking the spelling of each field in the list" )
            print("Also consider spelling of your table name, and SQL statements\n" + bcolors.ENDC )
        # Endif
    return(dframe)
# end of runsql()

######################### New function "strhash"
def strhash (msg) :
    x = 0; h = 1337801; nc = len(msg) 
    while (x<nc) :
        cval = ord( msg[x] )  # get num value of char
        h = ((h & 0xffffff) * 33) + cval
        x += 1
    return(h); # Add one blank line after this



######################### New function "h32"
def h32 (msg) :
    x = 0; h = 728143; nc = len(msg) 
    while (x<nc) :
        cval = ord( msg[x] )  # get num value of char
        h = ((h & 0xffffffff) << 3) + cval
        x += 1
    return(h); # Add one blank line after this

######################### New function "hecho"
def hecho (msg) :
    patrn = "ab^CdF]GTi_jklM}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0"
    i = len(patrn)
    mz = len(msg)
    nz = 0
    omsg = ''
    if msg[0] == '$':
        nz = ord(msg[1]) - 31
        imsg = msg[4:nz+4]
        adj = -5
    else :
        nz = min(mz,64)
        salt = chr( nz + 31)
        omsg = omsg +'$' + salt + chr(ord(msg[0])-30) + chr(ord(msg[1])-29)
        imsg = msg.upper()
        adj = +5
    for c in imsg :
            omsg = omsg + chr(ord(c)+adj)
    lz = len(omsg)
    if adj > 0 : omsg = omsg + patrn[lz:i]
    #print(omsg)
    return(omsg); # Add one blank line after this
#
# end of hecho
#


######################### New function "EndHere"
def StartHere( sname, sessn, task) -> None :
    """
    Starts a CIS2010 activity recording <student name>, <session> and <task> 
    these will be recorded for grading purpose to the filename <task>_vars.txt
    into the folder c:\\Users\\Public\\CIS2010   or //Users//Shared//CIS2010
    """

# create some global variables
    global z_MyName
    global z_sess
    global z_task
    global z_now
    global DateTime
    global z_path
    global z_os
    global z_cks
    global z_osn
    global z_un
    global z_hek
    
    
    if (len(sname) == 0) :
        print("\033[91mName not provided to StartHere. Name is required!\nYou must solve this problem or your work cannot be saved.")
        exit()
    #End if
    z_MyName = sname.upper()
    z_sess = sessn
    #z_task = z_task + task 
    z_task = task   #v2
    z_cks = h32(sname.upper())
   
    if  z_os == 'win32':
        z_un = os.getlogin()
    z_hek = hecho(sname)

    print('\n\n %s' % sname, " %s " % z_now)
    print( "good to go with", task, "\n\n")
    return

######################### Endwrite is used by EndHere
def Endwrite( varbls, file1 ) :
    """
    write records from a variable list <varbls> using file handle <file1>
    return filename of __file__
    Used by EndHere

    """
#    DateTime = type(z_now)              #??? only works if z_now is global
#    NoneType = type(None)
    fnx = 'unknown file'
    for key, value in list(varbls.items()):
#        print("key :", key, " type ", type(value))
        if (isinstance(value, str)):
            l2 = "\n"+ 's`' + key + "`" + value# + "~eos"
            file1.write(l2)
            if key == '__file__' : fnx = value
        elif (isinstance( value, (float))):
            fs =  '%0.6f' % value
            l2 = "\n"+ 'r`' + key + "`" + fs #+ "\n"
            file1.write(l2)
        elif (isinstance( value, (int))):
            l2 = "\n"+ 'v`' + key + "`" + str(value) #+ "\n"
            file1.write(l2)
#        elif (isinstance( value, NoneType)):
#            continue
        elif (isinstance( value, (list))):
            l2 = "\n"+ 'l`' + key + "`" + str(list(value)) + "`" + str(len(value)) #+ "\n"
            file1.write(l2)
        elif (isinstance( value, (tuple))):
            # tuples will be treated the similar to lists [V4]
            l2 = "\n"+ 't`' + key + "`" + str(list(value)) + "`" + str(len(value)) #+ "\n"
            file1.write(l2)
        elif (isinstance( value, pd.DataFrame)):
#            print("Dataframe type found")
#            info1 = ','.join(map(str, value.shape))
            info1 = str(value.shape)
#            print(info1)
            info = '\n' + 'd`' + key + '`' + info1 + '` tail 10 follows\n'
            file1.write( info )
            file1.write(value.tail(10).to_string())
#            file1.write('~eod')
        elif (isinstance( value, DateTime)):
#            print("datetime type found")
            file1.write("\n" + 't`' + key + "`%s"%value )
        elif (isinstance( value, type(console) )):
            file1.write("\n" + 'f`{}`{}'.format(key,value ))
        else:
            continue
    return( fnx )

######################### New function "EndHere"
def EndHere( lv ) -> None:
    """
    
    Ends a CIS2010 activity by writing variables (both local and global)
    to a filename Sxx_vars.txt
    into the local folder from which the parent python script is running
    """

#    DateTime = type(z_now)              #??? only works if z_now is global
#    NoneType = type(None)
    
    if (z_os == 'win32') :
        fname = os.getcwd() + "\\" + z_sess +"_vars.txt"
    else: 
        fname = os.getcwd() + "/" + z_sess  + "_vars.txt"
    file1 = open(fname, "w")
    file1.write("#`vtype`vname`vvalue`vextra")  # header of vars file does not have \n, done at start of recs later

    #print("\n\nSaving SH global variables to ", fname)
    mg = globals()
    fn1 = Endwrite( mg, file1)
    file1.write("\n#` End of global variables.")

    #print("\n\nSaving local variables to ", fname)
    fn2 = Endwrite( lv, file1)
    
    file1.write("\n#` End of task variables.\n")
    file1.close()
    print("\nVariable log saved here ", fname)
    #print( "\n ***** END ")
    
    # [V4] code to add Attribution to source file
    fname = fn2
    rAtr = '#Atr`' + z_hek + '\n'
    NoAtr = True
    
    file1 = open(fname, 'r')
    line = file1.readline()
    while line:
        if line == rAtr :
            NoAtr = False
        line = file1.readline()
    file1.close()
        
    # Add Atr if it does not exist for this user
    if NoAtr :
        file1 = open(fname,'a')
        file1.write(rAtr)
        file1.close()
    # End of Attribution [V4]
    
    return

######################### New function "showBits"
import ctypes
def showBits ( d ) :
    """
    
    Display the binary representation of input data
    works for integer, float and string
    """
    if type(d) == int :
        print (int(d), bin(int(d)))
        return 
    elif type(d) == float :
        print (d, bin(ctypes.c_uint.from_buffer(ctypes.c_float(d)).value))
        return     
    else :
        for c in d:
            print(c, ord(c), bin(ord(c)))
        return 

######################### New function "showBits"
def nchar( l ) :
    """
    
    Display number of characters in each element of list <l>
        displays count of characters for strings
        displays count of digits & sign for numbers
        displays count of digits & decimal & sign for float
    """
    if( type(l) == str ) :
        v = len(str(l))    
        print( v )
    elif( type(l) == int ) :
        v = len(str(l))    
        print( v )
    elif( type(l) == list ) :
        v2 = []
        v2 = [len(str(s)) for s in l]  
        print( v2 )
    elif( type(l) == tuple ) :
        v2 = []
        v2 = [len(str(s)) for s in l]  
        print( v2 )
    elif( type(l) == bool ) :
        print( 1 )
    else :
        v = len(str(l)) 
        print( v )

######################### New function "showBits"
def showNum( msg ) -> None :
    """
    Display ordinal int value for each character in the string <msg>
    """
    v = [ord(s) for s in msg]
    print( v )
    
######################### New function paste
def paste( *msg ) :
    """
    contatenate multiple strings
    """
    l1 = [str('')]
    for c1 in msg :
        l1.extend(str(c1))
    return ''.join(l1)

######################### New function "console"
def console( *msg ) -> None :
    """
    Display <msg> to Shell using print
    This function joins multiple arguments into a single message
    """
    l1 = [str('')]
    for c1 in msg :
        l1.extend(str(c1))
    print( ''.join(l1) )

######################### New function "console"
def ToShell( *msg ) -> None :
    """
    Display <msg> to Shell using print
    This function joins multiple arguments into a single message
    """
    l1 = [str('')]
    for c1 in msg :
        l1.extend(str(c1))
    print( ''.join(l1) )

######### End of cis2010utils ################