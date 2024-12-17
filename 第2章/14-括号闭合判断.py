# 给定一个只包含小写字母的字符串，判断该字符串中的括号是否闭合，如果每个左括号都有对应的右括号，并且括号的嵌套顺序正确，那么括号就能正确闭合。否则，括号不能正确闭合，字符串中括号仅限于 "(" 和 ")"。

str1 = input("请输入: ")
stack = []
for i in str1:
    if i == '(':
        stack.append(i)
    elif i == ')':
        if not stack:
            print(False)
            break
        stack.pop()
else:
    print(len(stack) == 0)
