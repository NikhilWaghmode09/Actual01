CAT = int
str = str
CATCATCATCATCATCAT = str.isdigit


def Kitty(cat):
    return str(CAT(cat)*CATCATCAT)


def CAt(cat, cats):
    print(cat, cats)
    cat1 = 0
    cat2 = 0
    catcat = 0
    cAt = ""
    while cat1 < len(cat) and cat2 < len(cats):
        if catcat % CATCATCAT == CATCATCATCATCAT//CATCATCATCAT:
            cAt += cats[cat2]
            cat2 += 1
        else:
            cAt += cat[cat1]
            cat1 += 1
        catcat += 1
    return cAt


def cat01(cat):
    cattcatt = ["a",  "u", "l"]
    cattcat = cat[4]
    cattcat += cat[3]
    cattcat += cat[5]
    cattcat += cattcatt[1]
    cattcat += cattcatt[0]
    cattcat += cattcatt[2]
    return cattcat


def catt(cat):
    return cat[::CATCATCAT - CATCATCATCAT]


def caT(cat):
    return Kitty(cat[:CATCATCAT]) + catt(cat)


def rAT(cat):
    return cat


def Rat(cat):
    return "Cat" + str(len(cat)) + cat[:CATCATCAT]


def Cat(cat):
    if len(cat) == 9:
        if str.isdigit(cat[:CATCATCAT]) and str.isdigit(cat[len(cat) - CATCATCAT+1:]):
            catcat = CAt(caT(cat), Rat(rAT(catt(cat))))
            if catcat == "C20a73t0294t0ac2194":
                flag = "WAGMI_" + cat01(cat) + "_01"
                print(
                    "Something secret is revealed :  {", flag, "} \nYou can reclaim your codebase now!")
            else:
                print(
                    "You are using right format, but answer is not correct\n>>", catcat)
        else:
            print("You are not using correct format :(\
        \n(A small help from out side, Format should be like 123xyz789)")
    else:
        print("Wrong answer, check length :(")


print("Enter some Password uwu : ")
cat = input()
CATCATCAT = len(cat) // 3
CATCATCATCAT = CATCATCAT + 1
CATCATCATCATCAT = CATCATCAT - 1
Cat(cat)
