"""

给定两个表示复数的字符串。
返回表示它们乘积的字符串。注意，根据定义 i ** 2 = -1 。

示例 1:
输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i ** 2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

示例 2:
输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i ** 2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。

"""


def complexNumberMultiply(a, b):
    import re
    a_list = re.findall(r'-\d+|\d+', a)
    b_list = re.findall(r'-\d+|\d+', b)
    a_real_num = int(a_list[0])
    a_imag_num = int(a_list[1])
    b_real_num = int(b_list[0])
    b_imag_num = int(b_list[1])

    real_imag = a_real_num * b_imag_num + a_imag_num * b_real_num
    real = a_real_num * b_real_num
    imag = a_imag_num * b_imag_num
    res = real - imag
    return str(res) + '+' + str(real_imag) + "i"


print(complexNumberMultiply("1+1i", "1+1i"))
print(complexNumberMultiply("1+-1i", "1+-1i"))
print(complexNumberMultiply("3+-5i", "4+-8i"))
print(complexNumberMultiply("78+-76i", "-86+72i"))
