mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below
def mixed_list(arr):
    for item in arr:
        print(type(item))

mixed_list(mix)