import random

def create_test(n):
    genders = ["Men", "Women", "Kids"]
    strings = [
        ["AMT", "AMS", "AMP", "AMJ", "JMJL", "JMPL", "JMTL", "MT", "MS", "MP"],
        ["AWT", "AWS", "AWP", "AWJ", "JWJL", "JWPL", "JWTL", "WT", "WS", "WP"],
        ["JJJJ"]
    ]
    colors = ["BK", "WT", "NVY", "SST", "CMO"]
    sizes = ["XS", "S", "M", "L", "XL", "2XL"]
    data = []

    for _ in range(n):
        gnum = random.randint(0, 2)
        g = genders[gnum]
        s = strings[gnum][random.randint(0, len(strings[gnum]) - 1)] + str(random.randint(1, 3) * 1000)
        c = "C" + colors[random.randint(0, 4)]
        size = sizes[random.randint(0, 5)]
        price = random.randint(100, 100000)
        hour = random.randint(10, 20)
        time = random.randint(202406030000, 202406042359)
        data.append([g, s, c, size, price, hour, time])

    for d in data:
        print(",".join(list(map(str, d))))

if __name__ == "__main__":
    create_test(30)