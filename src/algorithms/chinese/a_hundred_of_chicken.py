"""
今有鸡翁一，值钱伍；鸡母一，值钱三；鸡鶵三，值钱一。凡百钱买鸡百只，问鸡翁、母、鶵各几何？
"""


def get_solutions():
    solutions = []
    for x in range(0, 100 // 5):
        for y in range(0, 100 // 3):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                solutions.append({'5': x, '3': y, '1': z})
    return solutions


def main():
    fmt_str = "鸡翁: {:2d}, 鸡母: {:2d}, 鸡鶵: {:2d}"
    for solution in get_solutions():
        print(fmt_str.format(solution['5'], solution['3'], solution['1']))


if __name__ == '__main__':
    main()
