import random

# テストデータを生成する関数
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
        s = strings[gnum][random.randint(0, len(strings[gnum]) - 1)] + str(random.randint(100, 99999))
        c = colors[random.randint(0, 4)]
        size = sizes[random.randint(0, 5)]
        price = random.randint(100, 100000)
        data.append([g, s, c, size, price])

    return data

# コードから数値部分を抽出する関数
def divide_code(code):
    for i in range(len(code)):
        if code[i].isdigit():
            return int("".join(filter(str.isdigit, code[i:])))
    return 0

# マージソートを使用してリストをソートする関数
def merge_sort(A):
    if len(A) <= 1:
        return A
    
    center = len(A) // 2
    left = A[:center]
    right = A[center:]

    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        lnum = divide_code(list(left[i].keys())[0])
        rnum = divide_code(list(right[j].keys())[0])
        if lnum <= rnum:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# データをソートする関数
def sort_datas(data):
    B = [[] for _ in range(3)]
    for a in data["codes"].keys():
        initial = a[0]
        if initial == "A":
            B[0].append({a: data["codes"][a]})
        elif initial == "M" or initial == "W":
            B[1].append({a: data["codes"][a]})
        else:
            B[2].append({a: data["codes"][a]})

    res = []
    for b in B:
        res += merge_sort(b)

    return res

# メインロジック
A = create_test(10)

genders = ["Men", "Women", "Kids"]
sizes = ["XS", "S", "M", "L", "XL", "2XL"]

result = [{"codes": {}} for _ in range(3)]
for a in A:
    gender, code, color, size, price = a
    g = genders.index(gender)

    if code not in result[g]["codes"]:
        result[g]["codes"][code] = {"colors": {}}
    if color not in result[g]["codes"][code]["colors"]:
        result[g]["codes"][code]["colors"][color] = {"sizes": {si: 0 for si in sizes}}

    result[g]["codes"][code]["colors"][color]["sizes"][size] += 1
    result[g]["codes"][code]["colors"][color]['price'] = price

# ソートしたデータを表示
for data in result:
    sorted_data = sort_datas(data)
    print(sorted_data)
