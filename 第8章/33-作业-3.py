# 编写一个银行账户管理系统的类BankAccount，具有以下功能：

# 账户属性包括：账号(account_number)，账户类型(account_type)，余额(balance)和交易历史记录(transactions)，账户类型可以有多种
# 初始化方法__init__()用于设置账户属性。
# 存款方法deposit(amount)：接收存款金额(amount)，如果金额大于0，则将金额加入余额(balance)，并将存款信息添加到交易历史记录(transactions)中，并打印存款成功信息。
# 取款方法withdraw(amount)：接收取款金额(amount)，如果金额大于0且小于等于余额(balance)，则从余额中扣除金额，并将取款信息添加到交易历史记录(transactions)中，并打印取款成功信息。否则，打印余额不足或者取款金额无效的信息。
# 转账方法transfer(recipient_account, amount)：接收收款账户(recipient_account)和转账金额(amount)。如果金额大于0且小于等于余额(balance)，则从当前账户余额中扣除相应金额，将金额存入收款账户，并在两个账户的交易历史记录(transactions)中添加相应信息，并打印转账成功信息。否则，打印余额不足或者转账金额无效的信息。
# 查看交易历史记录方法get_transaction_history()：打印当前账户的交易历史记录。
# str()方法用于返回账户的信息字符串表示。
# 请根据以上要求完成BankAccount类的编写，完成如下需求。

# 1，打印账户余额：

# 打印123456789账户的账户号码，类型，余额
# 打印987654321账户的账户号码，类型，余额
# 2，针对123456789账户进行500元的存入，和2000元的取出

# 3，账户987654321给123456789转账共3000 元。

# 4，打印123456789 的交易历史记录。

# 并最终输出结果如下：

# 账号：123456789  类型：储蓄账户  余额：10000
# 账号：987654321  类型：支票账户  余额：5000

# 成功存入 500 元。当前余额为：10500 元。
# 成功取出 2000 元。当前余额为：8500 元。

# 开始转账
# 成功存入 3000 元。当前余额为：11500 元。
# 本次转账，账户987654321 成功转账给账户123456789共3000 元。

# 账户 123456789 的交易历史记录：
# 存入 500 元。
# 取出 2000 元。
# 存入 3000 元。

# 遵循如下代码开始编写：

# # 创建账户对象
# account1 = BankAccount("123456789", "储蓄账户", 10000)
# account2 = BankAccount("987654321", "支票账户", 5000)


class BankAccount:
    def __init__(self, account_number, account_type, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"存入 {amount} 元。")
            print(f"成功存入 {amount} 元。当前余额为：{self.balance} 元。")
        else:
            print("存款金额无效。")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"取出 {amount} 元。")
            print(f"成功取出 {amount} 元。当前余额为：{self.balance} 元。")
        elif amount > self.balance:
            print("余额不足。")
        else:
            print("取款金额无效。")

    def transfer(self, recipient_account, amount):
        print("开始转账")
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.transactions.append(f"转出 {amount} 元到账户 {recipient_account.account_number}。")
            recipient_account.transactions.append(f"从账户 {self.account_number} 转入 {amount} 元。")
            print(f"本次转账，账户{self.account_number} 成功转账给账户{recipient_account.account_number}共{amount} 元。")
        elif amount > self.balance:
            print("余额不足，转账失败。")
        else:
            print("转账金额无效。")

    def get_transaction_history(self):
        print(f"账户 {self.account_number} 的交易历史记录：")
        for transaction in self.transactions:
            print(transaction)

    def __str__(self):
        return f"账号：{self.account_number}  类型：{self.account_type}  余额：{self.balance}"

# 创建账户对象
account1 = BankAccount("123456789", "储蓄账户", 10000)
account2 = BankAccount("987654321", "支票账户", 5000)

# 打印账户余额
print(account1)
print(account2)

# 存款和取款操作
account1.deposit(500)
account1.withdraw(2000)

# 转账操作
account2.transfer(account1, 3000)

# 打印交易历史记录
account1.get_transaction_history()
