import my_colors
import egn_generator
import egn_extractor


def welcome():
    print(
        """

  ______    _____   _   _                                  _                  
 |  ____|  / ____| | \ | |                                | |                 
 | |__    | |  __  |  \| |     ___   _ __    ___    __ _  | |_    ___    _ __ 
 |  __|   | | |_ | | . ` |    / __| | '__|  / _ \  / _` | | __|  / _ \  | '__|
 | |____  | |__| | | |\  |   | (__  | |    |  __/ | (_| | | |_  | (_) | | |   
 |______|  \_____| |_| \_|    \___| |_|     \___|  \__,_|  \__|  \___/  |_|   
                                                                              
                         created by: github.com/ykostov                                                     

          """
    )


def chooseMode():
    flag = True
    while flag:
        try:
            userInput = int(
                input(
                    my_colors.INFO
                    + """
Choose:
1. Create EGN from data
2. Extract data from EGN
"""
                    + my_colors.ENDC
                )
            )
            flag = False
            return userInput
        except:
            print(my_colors.WARNING + "Try again" + my_colors.ENDC)


# ============== MAIN ==============

welcome()

if chooseMode() == 1:
    egn_generator.start()
elif chooseMode() == 2:
    egn_extractor.start()
