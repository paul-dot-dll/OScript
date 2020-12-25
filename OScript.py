command = input()
if command.startswith('echo'):
    # print(command) (used to check if string formatting was correct
    cmd = command.partition('echo ')[2]
    runcmd = "print ('" + cmd + "')"
    #print(runcmd) (was also used to check if string was done correctly)
    exec(runcmd)
if command.startswith('help') or command == "help" or command == "/?":
    print("Commands include:\n *echo (arg) \\\returns any string inputted\n *help \\\lists all current commands")
