project_gran = 143
project_lotus = 232
operation_dove = 653
other = 404
password = int(input("Password: "))
if password == 18438:
     passwordX = 18438
else:
    print (">>incorrect password<< 3 tries left")
    answer = int(input("Try again: "))
    if answer == 18438:
        passwordX = 18438
    else: 
        print (">>incorrect password<< 2 tries left")
        answer = int(input("Try again: "))
        if answer == 18438:
            passwordX = 18438
        else:
            print (">>incorrect password<< 1 try left<<")
            answer = int(input("Try again: "))
            if answer == 18438:
                    passwordX = 18438
            else:
                print ("<<Password limit reached>>")
                print ("-")
                print ("Restart program")
if passwordX == 18438:
    print ("Access Granted")
    print ("-")
    print ("Directories:")
    print ("143: Projekt Eula")
    print ("232: Project Lotus")
    print ("653: Operation Dove")
    print ("404: other;")
    print ("-")
    print ("-")
    print ("-")
    print ("-")
    print ("-")
    accesscode = int(input("Directory Code: "))
    if accesscode == 143:
        print ("/143")
        print ("(Project Eula)")
    if accesscode == 232:
        print ("/232")
        print ("<<<<Project Lotus>>>>")
        print ("-")
        print ("Type: Hypersonic Bomber")
        print ("Code type: Aurora X")
        print ("-")
        print ("BRIEF:")
        print ("^_^_^_^_^_^_^_^_^_^_^_^")
        print ("The Aurora X is a hypersonic bomber capable of carrying a payload of ≈5 000 kg of bombs. \nScramjets allow this aricraft to reach speeds beyond Mach 8. Estimated range lies at \naround 11 000 nm. Originally developed for the war efforts i Crimea.")
        print (">Lockheed Martin - Skunkworks")
        print ("-")
    if accesscode == 653:
        print ("/653")
        print ("(Operation Dove)")
    if accesscode == 404:
        print ("/404")
        print ("(other)")