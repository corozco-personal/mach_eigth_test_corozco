import sys

## Prints on the screen all the pairs of numbers whose sum is
## the value sent as a parameter by the user
## @param arr List of integers
## @param value given by user
def find_pairs(arr, value) :
    possible_pairs = {}
    result = {}

    for i in range(0,len(arr)) :
        current = arr[i] ## Assign value for readability

        ##Calculate the possible pair according to the current value on the list
        x = value - current

        ## If the current value is already on the possible_pair map and is it's first ocurrence you have a valid sum pair
        if possible_pairs.get(current) != None and result.get(current) == None :
          result[current] = x
          print(arr[i], x)
        else :
          possible_pairs[x] = current

##Test function with example given previously
def test_app() :
    arr = (1,9,5,0,20,-4,12,16,7)
    find_pairs(arr, 12)

if len(sys.argv) == 2 and "-test" == sys.argv[1] :
    test_app()
elif len(sys.argv) == 3 :
    arr = [int(i) for i in sys.argv[1].split(',')]
    value = int(sys.argv[2])
    find_pairs(arr, value)
else :
    print("Check the documentation on how to call the app")
    print("Correct syntax: app.py comma_separated_list target")
    print("Example: app.py 1,2,3,4,5 3")
    print("Test: app.py -test")
