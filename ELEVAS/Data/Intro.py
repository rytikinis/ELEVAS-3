import time, pickle

def get_info():
    global data
    print('''
          *      *             *
             WELCOME TO ELEVAS    *
                 *
            *         *      *
          ''')
    time.sleep(0.5)
    while True:
        answer = input("ELEVAS\>")
        if answer == "new_simulation":
            data = create_simulation()
            print(data)
            break
        if answer == "new_file":
            create_file()
        if answer == "open_file":
            load_file()
            break

def create_simulation():
    frequency = -1
    time_speed = 1
    gass = float("inf")
    while True:
        sfr = input("Amount of stars born per xx Myr(SFR): ")
        while True:
            try:
                int(sfr)
                break
            except:
                print("Error: invalid character, please use numbers only")
                sfr = input("Amout of stars born per xx Myr(SFR): ")
        if int(sfr) > 0:
            break
        else:
            print("Error: sfr must be bigger than 0")
    while True:
        em = input("SFR stars will be born every Myr(EM): ")
        while True:
            try:
                int(em)
                break
            except:
                print("Error: invalid character, please use numbers only")
                em = input("SFR stars will be born every Myr(EM): ")
        if int(em) > 0:
            break
        else:
            print("Error: em must be bigger than 0")
    op = input("% of initial orange stars(op): ")
    yp = input("% of initial yellow stars(yp): ")
    bp = input("% of initial blue stars(bp): ")
    wp = input("% of initial white stars(wp): ")
    while True:
        try:
            if int(op) + int(yp) + int(bp) + int(wp) != 100:
                print("Error: ivalid star formating procentege")
                op = input("% of initial orange stars(op): ")
                yp = input("% of initial yellow stars(yp): ")
                bp = input("% of initial blue stars(bp): ")
                wp = input("% of initial white stars(wp): ")
            if int(op) + int(yp) + int(bp) + int(wp) == 100:
                break
        except:
            print("Error: invalid character, please use numbers only")
            op = input("% of initial orange stars(op): ")
            yp = input("% of initial yellow stars(yp): ")
            bp = input("% of initial blue stars(bp): ")
            wp = input("% of initial white stars(wp): ")
    while True:
        while True:
            ybp = input("% of yellow star being binary(ybp): ")
            try:
                ybp = int(ybp)
                break
            except:
                print("Error: ybp must be a number")
                ybp = input("% of yellow star being binary(ybp): ")
        if ybp > -1 and ybp < 101:
            break
        else:
            print("Error: ybp must be a number and it must be bigger than -1 and smaller than 101")
    while True:
        answer = input("ELEVAS\SIMULATION\>")
        if answer == "run":
            break
        elif answer == "create_output":
            while True:
                frequency = input("Frequency of creating output(mry): ")
                while True:
                    try:
                        float(frequency)
                        break
                    except:
                        print("Error: frequency must be a number")
                        answer = input("ELEVAS\SIMULATION\>")
                if int(frequency) > 0:
                    print("Frequency was set to " + frequency)
                    break
                else:
                    print("Error: the frequency must be a number and be bigger than 0")
        elif answer == "add_gass_amout":
            while True:
                gass = input("Enter gass amout: ")
                while True:
                    try:
                        float(gass)
                        break
                    except:
                        print("Error: gass must be a number")
                        gass = input("Enter gass amout: ")
                if int(gass) > 0:
                    break
                else:
                    print("Error: gass must be bigger than 0")
        elif answer == "add_time_speed":
            time_speed = input("Enter time speed(mry): ")
            while True:
                while True:
                    try:
                        float(time_speed)
                        break
                    except:
                        print("Error: time speed must be a number")
                        time_speed = input("Enter time speed(mry): ")
                if float(time_speed) > 0:
                    break
                else:
                    print("Error: time speed must be bigger than 0")
    print("Done")
    return sfr, em, op, yp, bp, wp, ybp, frequency, gass, time_speed

def create_file():
    frequency = -1
    time_speed = 1
    gass = float("inf")
    while True:
        sfr = input("Amout of stars born per xx Myr(SFR): ")
        while True:
            try:
                int(sfr)
                break
            except:
                print("Error: invalid character, please use numbers only")
                sfr = input("Amout of stars born per xx Myr(SFR): ")
        if int(sfr) > 0:
            break
        else:
            print("Error: sfr must be bigger than 0")
    while True:
        em = input("SFR stars will be born every Myr(EM): ")
        while True:
            try:
                int(em)
                break
            except:
                print("Error: invalid character, please use numbers only")
                em = input("SFR stars will be born every Myr(EM): ")
        if int(em) > 0:
            break
        else:
            print("Error: em must be bigger than 0")
    op = input("% of initial orange stars(op): ")
    yp = input("% of initial yellow stars(yp): ")
    bp = input("% of initial blue stars(bp): ")
    wp = input("% of initial white stars(wp): ")
    while True:
        try:
            if int(op) + int(yp) + int(bp) + int(wp) != 100:
                print("Error: ivalid star formating procentege")
                op = input("% of initial orange stars(op): ")
                yp = input("% of initial yellow stars(yp): ")
                bp = input("% of initial blue stars(bp): ")
                wp = input("% of initial white stars(wp): ")
            if int(op) + int(yp) + int(bp) + int(wp) == 100:
                break
        except:
            print("Error: invalid character, please use numbers only")
            op = input("% of initial orange stars(op): ")
            yp = input("% of initial yellow stars(yp): ")
            bp = input("% of initial blue stars(bp): ")
            wp = input("% of initial white stars(wp): ")
    while True:
        while True:
            ybp = input("% of yellow star being binary(ybp): ")
            try:
                ybp = int(ybp)
                break
            except:
                print("Error: ybp must be a number")
        if ybp > -1 and ybp < 101:
            break
        else:
            print("Error: ybp must be a number and it must be bigger than -1 and smaller than 101")
    filename = input("Enter filename: ")
    while True:
        answer = input("ELEVAS\SIMULATION\>")
        if answer == "save":
            break
        elif answer == "add_output":
            while True:
                frequency = input("Frequency of creating output(mry): ")
                while True:
                    try:
                        float(frequency)
                        break
                    except:
                        print("Error: frequency must be a number")
                        answer = input("ELEVAS\SIMULATION\>")
                if int(frequency) > 0:
                    print("Frequency was set to " + frequency)
                    break
                else:
                    print("Error: the frequency must be a number and be bigger than 0")
        elif answer == "add_gass_amout":
            while True:
                gass = input("Enter gass amount: ")
                while True:
                    try:
                        float(gass)
                        break
                    except:
                        print("Error: gass must be a number")
                if gass > 0:
                    break
                else:
                    print("Error: gass must be bigger than 0")
        elif answer == "add_time_speed":
            time_speed = input("Enter time speed(mry): ")
            while True:
                while True:
                    try:
                        float(time_speed)
                        break
                    except:
                        print("Error: time speed must be a number")
                        time_speed = input("Enter time speed(mry): ")
                if float(time_speed) > 0:
                    break
                else:
                    print("Error: time speed must be bigger than 0")
    print("Done")
    pickle.dump([sfr, em, op, yp, bp, wp, ybp, frequency, gass, time_speed], open("Data/Simulations/" + str(filename) + ".elv", "wb"))
    
def load_file():
    global data
    filename = input("Enter file name: ")
    while True:
        try:
            data = pickle.load(open("Data/Simulations/" + str(filename) + ".elv", "rb"))
            break
        except:
            print("Error: no such file named: " + str(filename))
            filename = input("Enter file name: ")
            continue