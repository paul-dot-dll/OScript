cmdlist = {
    'echo ' : "cmd = command.partition('echo ')[2]\nruncmd = 'print (cmd)'\nexec(runcmd)",
    'help' : "print('''Commands include: \n *echo (arg) #returns any string inputted\n *help #lists all current commands''')",
}

#this simplifies the code even further, it looks into the dictionary, sees if the command is in there, and if it is, it executes the command's code
def main(command):
        for key in cmdlist:
                if command.startswith(key):
                        exec(cmdlist[key])
                #if not command.startswith(key): \\this would cause it to say not recognized for every command in the dictionary, so that will have to be fixed later
                        #print("not recognized")
if __name__ == "__main__": #this splits up the code into two parts, if it's running from the UI program (as a module), then it uses GUIRUN, if you run this file, it uses the original one.
    while True:
        command = input()
        main(command)
