"""def function1():
    lista = ["some","thing","more"];
    some = "something";

    lista.append("other");

    if some == "something" :
        print("son iguales");
        print("o eso creo");
        lista.insert(1,"some");
        print(lista);
        print(len(lista));
    else:
        print("o no");

function1();
print("\n\n");

numbers = [(x**2 - 6*x -3) for x in range(22)];

print(numbers);"""

"""import requests;

req = requests.get("https://demo.api-platform.com/books");

print(req.encoding);      # returns 'utf-8'
print(req.status_code)   # returns 200
print(req.elapsed)       # returns datetime.timedelta(0, 1, 666890)
print(req.url)           # returns 'https://tutsplus.com/'
 
print(req.history)      
# returns [<Response [301]>, <Response [301]>]
 
req.headers['Content-Type']"""

import multitasking
import time
import random
import signal

# kill all tasks on ctrl-c
signal.signal(signal.SIGINT, multitasking.killall)

# or, wait for task to finish on ctrl-c:
# signal.signal(signal.SIGINT, multitasking.wait_for_tasks)

@multitasking.task # <== this is all it takes :-)
def hello(count):
    sleep = random.randint(1,10)/2
    print("Hello %s (sleeping for %ss)" % (count, sleep))
    time.sleep(sleep)
    print("Goodbye %s (after for %ss)" % (count, sleep))

if __name__ == "__main__":
    for i in range(0, 10):
        hello(i+1)