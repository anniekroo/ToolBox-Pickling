""" A program that stores and updates a counter using a Python pickle file"""
import os.path
from os.path import exists
import sys
import pickle
from pickle import dump, load


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """

    if reset == False:
        if os.path.exists(file_name) == True: #checking whether or not the file exists
            with open(file_name, 'rb+') as f: #opens file to be read and written
                count = pickle.load(f) #reads previous count
                count = int(count)+1 #increments count by 1
                f.seek(0) #goes to begining of file
                pickle.dump(str(count), f) #overwrites previous number
                f.seek(0) #goes back to begining of file
                return int(pickle.load(f)) #returns count from file
        else:
            with open(file_name, 'wb') as f: #opens existing file and erases data
                pickle.dump(1, f) #writes 1 into the file
            with open(file_name, 'rb') as fOut: #opens the file to be read
                return pickle.load(fOut) #returns count from file
    else:
        with open(file_name, 'wb') as f: #opens existing file and erases data
            pickle.dump(1, f) #writes 1 into the file
        with open(file_name, 'rb') as fOut: #opens the file to be read
            return pickle.load(fOut) #returns count from file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))

"""
The following code was my first pass attempt at writing this program.
In this first pass I used no pickling. The limitations of this design
was that if the counter was more than one digit, the output would be
the second digit of the multi-digit number. Additionally, the files do
not so much contain how many times it has been opened, but the counter
each time it was opened previously.

if reset == False:
    if os.path.exists(file_name) == True:
        try:
            f = open(file_name, 'rb+')
        except:
            print('Something went wrong.')
        count = f.read()
        count = int(count)+1
        f.write(str(count))
        f.close()
        fout = open(file_name)
        return int(fout.read()[-1])
        fout.close
    else:
        f = open(file_name, 'w')
        f.write('1')
        f.close()
        fout = open(file_name)
        return int(fout.read()[-1])
        fout.close
else:
    f = open(file_name, 'w')
    f.write('1')
    f.close()
    fout = open(file_name)
    return int(fout.read()[-1])
    fout.close
"""
