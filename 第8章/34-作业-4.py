# 假设我们正在创建一个银行账户管理系统，设计一个银行账户类（BankAccount），具有以下功能：

# 每个人都有：账号号码（account_number）和账户余额（balance），因为账户号码和账户余额都是隐身信息，所以只有账户持有人才有查看权限。
# 每个账户都可用于验证用户输入的PIN码是否正确validate_pin(self, pin)，因为对密码安全性保护较高，只有账户持有人才有输入密码，尝试密码是否正确的权限。
# 每个账户都可以被存款deposit(amount)
# 每个账户都可以被取款，即从账户中取款指定金额，取款时需要输入PIN码进行验证withdraw(amount, pin)
# 余额充足，则可以取款
# 余额不足，则提示余额不足
# 密码错误，则提示Pin错误
# 在主程序中，创建一个银行账户对象，并调用公有方法进行存款和取款操作。

# 要求：

# 存款操作：直接将指定金额加到账户余额中
# 取款操作：先调用方法验证PIN码，若验证通过则将指定金额从账户余额中减去；若验证不通过则输出错误提示信息
# 参考如下方式创建账户对象
# account = BankAccount("123456789", 1000)

class BankAccount:
    def __init__(self, account_number, balance, pin):
        """
        初始化银行账户
        :param account_number: 账号号码
        :param balance: 初始账户余额
        :param pin: 账户PIN码
        """
        self.__account_number = account_number  # 私有属性：账号号码
        self.__balance = balance  # 私有属性：账户余额
        self.__pin = pin  # 私有属性：PIN码

    def get_balance(self):
        """
        获取账户余额
        :return: 当前账户余额
        """
        return self.__balance

    def validate_pin(self, pin):
        """
        验证输入的PIN码是否正确
        :param pin: 用户输入的PIN码
        :return: True（正确）或 False（错误）
        """
        return self.__pin == pin

    def deposit(self, amount):
        """
        存款操作
        :param amount: 要存入的金额
        :return: 无
        """
        if amount > 0:
            self.__balance += amount
            print(f"存款成功！当前余额为：{self.__balance}")
        else:
            print("存款金额无效！")

    def withdraw(self, amount, pin):
        """
        取款操作
        :param amount: 要取出的金额
        :param pin: 用户输入的PIN码
        :return: 无
        """
        if not self.validate_pin(pin):
            print("PIN码错误！")
            return

        if amount <= 0:
            print("取款金额无效！")
        elif amount > self.__balance:
            print("余额不足！")
        else:
            self.__balance -= amount
            print(f"取款成功！当前余额为：{self.__balance}")

# 主程序
if __name__ == "__main__":
    # 创建一个银行账户对象，初始余额为1000，PIN码为"1234"
    account = BankAccount("123456789", 1000, "1234")

    # 存款操作
    account.deposit(500)  # 存入500

    # 尝试取款操作
    account.withdraw(200, "1234")  # 输入正确PIN码取款200
    account.withdraw(2000, "1234")  # 输入正确PIN码尝试超额取款
    account.withdraw(100, "0000")  # 输入错误PIN码尝试取款
