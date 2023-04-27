import keyboard as kb
print("Enter cps as number and enter keys as [keyinput-nospace-keyout]: ")
try:
    cps = int(input("Enter cps: "))
    keys = input("Enter keys as [keyinput-nospace-keyout]: ")
except:
    exit()
if len(str(cps)) == 0 | len(keys) > 2 | len(keys) == 0:
    print("Exiting...")
    exit()
else:
    while True:
        if kb.is_pressed(keys[0]) == True:
            for c in cps:
                kb.send(keys[1])
        
        else:
            if kb.is_pressed("q") == True:
                exit()
            continue
