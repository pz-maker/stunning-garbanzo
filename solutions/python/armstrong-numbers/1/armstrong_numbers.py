from datetime import datetime


def is_armstrong_number(number):
    """判断是否为阿姆斯特朗数，统一返回布尔值"""
    if not isinstance(number, int) or number < 0:
        return False

    # 0 是阿姆斯特朗数
    if number == 0:
        return True

    # 提取各位数字
    digits = []
    temp = number
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10

    # 计算各位数字的 n 次幂之和
    
    total = sum(d ** len(digits) for d in digits)  # ✅ 简洁且不会重复累加
    

    return total == number  # ✅ 统一返回 True/False


if __name__ == '__main__':
    print('开始运行.....')
    start_time = datetime.now()

    armstrong_number_list = []
    for number in range(0, 10000):
        result = is_armstrong_number(number)  # ✅ 只调用一次
        print(f'检查数字: {number}, 是否为阿姆斯特朗数: {result}')
        if result:
            armstrong_number_list.append(number)  # ✅ 追加数字本身
            print(f'找到阿姆斯特朗数: {number}')

    print(f'\n结果列表: {armstrong_number_list}')
    end_time = datetime.now()
    print(f'运行结束，总共花费时间: {end_time - start_time}')