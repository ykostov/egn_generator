import my_colors


def extractDay(egn):
    return egn[4:6]


def extractMonth(egn):
    if int(egn[2:4]) > 12:
        return int(egn[2:4]) - 40
    return egn[2:4]


def extractYear(egn):
    if int(egn[2:4]) > 39:
        return "20" + egn[0:2]
    return "19" + egn[0:2]


def extractBirthplace(egn):
    birthdig = int(egn[6:9])
    if birthdig < 44:
        return "Blagoevgrad"
    elif birthdig < 94:
        return "Burgas"
    elif birthdig < 140:
        return "Varna"
    elif birthdig < 170:
        return "Veliko Tarnovo"
    elif birthdig < 184:
        return "Vidin"
    elif birthdig < 218:
        return "Vratsa"
    elif birthdig < 234:
        return "Gabrovo"
    elif birthdig < 282:
        return "Kardzhali"
    elif birthdig < 302:
        return "Kustendil"
    elif birthdig < 320:
        return "Lovech"
    elif birthdig < 342:
        return "Montana"
    elif birthdig < 378:
        return "Pazardzhik"
    elif birthdig < 396:
        return "Pernik"
    elif birthdig < 436:
        return "Pleven"
    elif birthdig < 502:
        return "Plovdiv"
    elif birthdig < 528:
        return "Razgrad"
    elif birthdig < 556:
        return "Ruse"
    elif birthdig < 576:
        return "Silistra"
    elif birthdig < 602:
        return "Sliven"
    elif birthdig < 624:
        return "Smolyan"
    elif birthdig < 722:
        return "Sofia - grad"
    elif birthdig < 752:
        return "Sofia - okrug"
    elif birthdig < 790:
        return "Stara Zagora"
    elif birthdig < 822:
        return "Dobrich"
    elif birthdig < 844:
        return "Targovishte"
    elif birthdig < 872:
        return "Haskovo"
    elif birthdig < 904:
        return "Shumen"
    elif birthdig < 926:
        return "Yambol"
    return "Unknown"


def validateLastDigit(egn):
    sum = (
        0
        + int(egn[0]) * 2
        + int(egn[1]) * 4
        + int(egn[2]) * 8
        + int(egn[3]) * 5
        + int(egn[4]) * 10
        + int(egn[5]) * 9
        + int(egn[6]) * 7
        + int(egn[7]) * 3
        + int(egn[8]) * 6
    )

    result = sum % 11

    if result < 10:
        return int(egn[9]) == result
    return int(egn[9]) == 0


def extractGender(egn):
    if int(egn[8]) % 2 == 0:
        return "Boy"
    return "Girl"


def start():
    flag = True
    while flag:
        try:
            egn = input("enter EGN (0000000000): ")
            year = extractYear(egn)
            month = extractMonth(egn)
            day = extractDay(egn)
            birthplace = extractBirthplace(egn)
            lastDigit = validateLastDigit(egn)
            gender = extractGender(egn)
            print(
                (
                    my_colors.WARNING
                    + "Year: {}, Month: {}, Date: {}. Place of birth: {}. Gender: {}"
                    + my_colors.ENDC
                ).format(year, month, day, birthplace, gender)
            )
            if lastDigit:
                print("This EGN is valid")
            else:
                print(my_colors.FAIL + "This EGN is NOT valid!" + my_colors.ENDC)
            flag = False
        except:
            print("Something went wrong. Try again. ")
