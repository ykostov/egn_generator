import my_colors


def askForYearReturnBorders():
    year = 0
    borders = []
    userInput = input(
        my_colors.INFO + "Do you know year of born? (Y/N): " + my_colors.ENDC
    ).lower()

    if userInput == "y":
        year = int(input("Enter year: "))
        borders.append(year)
        borders.append(year + 1)
    else:
        userInput = input(
            my_colors.INFO
            + "Can you give two years for borders? (Y/N): "
            + my_colors.ENDC
        ).lower()
        if userInput == "y":
            firstYear = int(input("Enter 1st year (left border): "))
            secondYear = int(input("Enter 2nd year (right border, not inclusive): "))
            borders.append(firstYear)
            borders.append(secondYear)
        else:
            borders.append(1950)
            borders.append(2024)

    return borders


def askForMonthReturnBorders():
    month = 0
    borders = []
    userInput = input(
        my_colors.INFO + "Do you know month of born? (Y/N): " + my_colors.ENDC
    ).lower()

    if userInput == "y":
        month = int(input("enter month (1, 2, 3 - 12): ").zfill(2))
        borders.append(month)
        borders.append(month + 1)
    else:
        userInput = input(
            my_colors.INFO
            + "Can you give two months for borders? (Y/N): "
            + my_colors.ENDC
        ).lower()
        if userInput == "y":
            firstMonth = int(input("Enter 1st month (left border): "))
            secondMonth = int(input("Enter 2nd month (right border, not inclusive): "))
            borders.append(firstMonth)
            borders.append(secondMonth)
        else:
            borders.append(1)
            borders.append(13)

    return borders


def askForDayReturnBorders():
    day = 0
    borders = []
    userInput = input(
        my_colors.INFO + "Do you know day of born? (Y/N): " + my_colors.ENDC
    ).lower()

    if userInput == "y":
        day = int(input("enter day (1, 2, 3 - 32): "))
        borders.append(day)
        borders.append(day + 1)
    else:
        userInput = input(
            my_colors.INFO
            + "Can you give two dates for borders? (Y/N): "
            + my_colors.ENDC
        ).lower()
        if userInput == "y":
            firstDay = int(input("Enter 1st day (left border): "))
            secondDay = int(input("Enter 2nd day (right border, not inclusive): "))
            borders.append(firstDay)
            borders.append(secondDay)
        else:
            borders.append(1)
            borders.append(32)

    return borders


def askForBirthplaceReturnBorders():
    birthplace = 0
    borders = []
    userInput = input(
        my_colors.INFO + "Do you know place of birth? (Y/N): " + my_colors.ENDC
    ).lower()

    if userInput == "y":
        cities = (
            my_colors.WARNING
            + """
        1. Blagoevgrad
        2. Burgas
        3. Varna
        4. Veliko Tarnovo
        5. Vidin
        6. Vratsa
        7. Gabrovo
        8. Kardzhali
        9. Kustendil
        10. Lovech
        11. Montana
        12. Pazarzdhik
        13. Pernik
        14. Pleven
        15. Plovdiv
        16. Razgrad
        17. Ruse
        18. Silistra
        19. Sliven
        20. Smolyan
        21. Sofia - Grad
        22. Sofia - Okrug
        23. Stara Zagora
        24. Dobrich
        25. Targovishte
        26. Haskovo
        27. Shumen
        28. Yambol
        29. Other
        """
            + my_colors.ENDC
        )
        print(cities)
        userInput = int(input("Choose one: "))

        if userInput == 1:
            borders.append(0)
            borders.append(43)
        elif userInput == 2:
            borders.append(44)
            borders.append(93)
        elif userInput == 3:
            borders.append(94)
            borders.append(139)
        elif userInput == 4:
            borders.append(140)
            borders.append(169)
        elif userInput == 5:
            borders.append(170)
            borders.append(183)
        elif userInput == 6:
            borders.append(184)
            borders.append(217)
        elif userInput == 7:
            borders.append(218)
            borders.append(233)
        elif userInput == 8:
            borders.append(234)
            borders.append(281)
        elif userInput == 9:
            borders.append(282)
            borders.append(301)
        elif userInput == 10:
            borders.append(302)
            borders.append(319)
        elif userInput == 11:
            borders.append(320)
            borders.append(341)
        elif userInput == 12:
            borders.append(342)
            borders.append(377)
        elif userInput == 13:
            borders.append(378)
            borders.append(395)
        elif userInput == 14:
            borders.append(396)
            borders.append(435)
        elif userInput == 15:
            borders.append(436)
            borders.append(501)
        elif userInput == 16:
            borders.append(502)
            borders.append(527)
        elif userInput == 17:
            borders.append(528)
            borders.append(555)
        elif userInput == 18:
            borders.append(556)
            borders.append(575)
        elif userInput == 19:
            borders.append(576)
            borders.append(601)
        elif userInput == 20:
            borders.append(602)
            borders.append(623)
        elif userInput == 21:
            borders.append(624)
            borders.append(721)
        elif userInput == 22:
            borders.append(722)
            borders.append(751)
        elif userInput == 23:
            borders.append(752)
            borders.append(789)
        elif userInput == 24:
            borders.append(790)
            borders.append(821)
        elif userInput == 25:
            borders.append(822)
            borders.append(843)
        elif userInput == 26:
            borders.append(844)
            borders.append(871)
        elif userInput == 27:
            borders.append(872)
            borders.append(903)
        elif userInput == 28:
            borders.append(904)
            borders.append(925)
        elif userInput == 29:
            borders.append(926)
            borders.append(999)

    else:
        borders.append(1)
        borders.append(999)

    return borders


def askIsBoyReturnString():
    userInput = input(my_colors.INFO + "Girl or Boy? (G/B): " + my_colors.ENDC).lower()

    if userInput == "g":
        return False
    return True


def calculateSpecialNumber(nineDigit):
    sum = (
        0
        + int(nineDigit[0]) * 2
        + int(nineDigit[1]) * 4
        + int(nineDigit[2]) * 8
        + int(nineDigit[3]) * 5
        + int(nineDigit[4]) * 10
        + int(nineDigit[5]) * 9
        + int(nineDigit[6]) * 7
        + int(nineDigit[7]) * 3
        + int(nineDigit[8]) * 6
    )
    result = sum % 11
    if result < 10:
        return result
    return 0


def generateEgn(borderYear, borderMonth, borderDay, borderBirthplace, isBoy, fileName):
    text_file = open("wordlists/{}.txt".format(fileName), "w")
    counter = 0

    for year in range(int(str(borderYear[0])[2:]), int(str(borderYear[1])[2:]), 1):
        if borderYear[0] > 1999:
            year = "0" + str(year)
        for month in range(int(borderMonth[0]), int(borderMonth[1]), 1):
            if month < 10:
                month = str(month).zfill(2)
            if borderYear[0] > 1999:
                month = int(month) + 40

            for day in range(int(borderDay[0]), int(borderDay[1]), 1):
                if day < 10:
                    day = str(day).zfill(2)

                for region in range(
                    int(borderBirthplace[0]), int(borderBirthplace[1]), 1
                ):
                    if region < 100:
                        region = str(region).zfill(3)

                    if (
                        isBoy
                        and int(str(region)[2]) % 2 == 0
                        or not isBoy
                        and int(str(region)[2]) % 2 == 1
                    ):
                        nineDigitStr = str(year) + str(month) + str(day) + str(region)
                        specialNumber = calculateSpecialNumber(nineDigitStr)
                        text_file.write("{}{}\n".format(nineDigitStr, specialNumber))
                        counter += 1
    text_file.close()
    print(
        "{} Writed {} EGNs in wordlists/{}.txt {}".format(
            my_colors.WARNING, counter, fileName, my_colors.ENDC
        )
    )


def start():
    try:
        borderYear = askForYearReturnBorders()
        borderMonth = askForMonthReturnBorders()
        borderDay = askForDayReturnBorders()
        borderBirthplace = askForBirthplaceReturnBorders()
        askIsBoy = askIsBoyReturnString()
        fileName = input("Enter name of subject: ")

        generateEgn(
            borderYear, borderMonth, borderDay, borderBirthplace, askIsBoy, fileName
        )
    except Exception as e:
        print(
            my_colors.WARNING
            + "Something went wrong! Please, try again"
            + e
            + my_colors.ENDC
        )
