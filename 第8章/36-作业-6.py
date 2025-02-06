# 假设我们正在开发一个银行账户管理系统，其中有一个账户类 Account，每个账户具有以下属性和功能：

# 属性：

# 账号（account_number）
# 持有人姓名（owner）
# 余额（balance）
# 功能：

# 存款（deposit）
# 取款（withdraw）
# 查询余额（get_balance）
# 现在，我们希望实现一个从外部数据源加载账户信息并创建账户对象的类方法。这样，我们可以通过类方法来统一处理账户对象的创建过程，并确保创建的账户对象已初始化。


class Account():
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('存钱失败')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print('取钱失败')

    def get_balance(self):
        return self.balance
    
    @classmethod
    def form_data_source(cls, data):
        return cls(
            account_number = data.get("account_number"),
            owner = data.get("owner"),
            balance = data.get('balance', 0.0)
        )
    

external_data = {
    "account_number": "123456",
    "owner": "张三",
    "balance": 1000.0
}

account = Account.form_data_source(external_data)
print(account.owner)
print(account.balance)
