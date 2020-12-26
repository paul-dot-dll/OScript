def main(command):
        if command.startswith('echo'):
            # print(command) (used to check if string formatting was correct
            cmd = command.partition('echo ')[2]
            runcmd = "print ('" + cmd + "')"
            #print(runcmd) (was also used to check if string was done correctly)
            exec(runcmd)
        elif command.startswith('help') or command == "help" or command == "/?":
            print("Commands include:\n *echo (arg) \\\returns any string inputted\n *help \\\lists all current commands")
        else:
            print("Command not recognized!")

            

if __name__ == "__main__": #this splits up the code into two parts, if it's running from the UI program (as a module), then it uses GUIRUN, if you run this file, it uses the original one.
    while True:
        command = input()
        main(command)
