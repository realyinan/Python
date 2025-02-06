# 假设你正在设计一个电商平台的订单支付系统和库存管理系统。用户在下单时，需要选择支付方式，并且对应的商品库存数量会相应减少。
# 请设计并实现这些系统的类和相关操作，补齐函数实现（写有 # TODO 处），以及缺失的参数即可。

# 要求：

# 支付类（Payment）具有以下属性和方法：
# 方法：支付（pay(amount)）
# 方法：退款（refund(order_id)）

# 库存管理类（Inventory）具有以下属性和方法：
# 属性：库存数量（quantity）
# 方法：更新库存（update_inventory(quantity_change)）

# 订单类（Order）具有以下属性和方法：
# 属性：订单号（order_id）和商品数量（quantity）
# 方法：下单（place_order(payment, inventory)）,假设每件商品的单价都是100元

# 创建支付对象、库存管理对象和订单对象，并编写主程序模拟以下场景：
# 用户使用支付宝支付了200元
# 用户使用微信支付了100元
# 分别输出支付结果和库存管理对象的最新库存数量。
# 用户使用支付宝支付 200 元，购买了2件商品
# 支付结果： 支付宝支付 200 元成功！
# 当前库存数量： 8

# 用户使用微信支付 100 元，购买了1件商品
# 支付结果： 微信支付 100 元成功！
# 当前库存数量：7

class Payment:
    def pay(self, amount):
        raise NotImplementedError
    
    def refund(self, order_id):
        raise NotImplementedError

class Alipay(Payment):
    def pay(self, amount):
        return f"支付宝支付 {amount} 元成功！"
    
    def refund(self, order_id):
        return f"支付宝退款成功，订单号：{order_id}"

class WeChatPay(Payment):
    def pay(self, amount):
        return f"微信支付 {amount} 元成功！"
    
    def refund(self, order_id):
        return f"微信退款成功，订单号：{order_id}"

class Inventory:
    def __init__(self, quantity):
        self.quantity = quantity
    
    def update_inventory(self, quantity_change):
        if self.quantity + quantity_change < 0:
            return False  # 库存不足
        self.quantity += quantity_change
        return True

class Order:
    UNIT_PRICE = 100  # 每件商品的单价 100 元
    
    def __init__(self, order_id, quantity):
        self.order_id = order_id
        self.quantity = quantity
    
    def place_order(self, payment, inventory):
        total_amount = self.quantity * self.UNIT_PRICE
        
        if inventory.update_inventory(-self.quantity):  # 先检查库存是否足够
            payment_result = payment.pay(total_amount)
            return payment_result
        else:
            return "下单失败，库存不足！"

# 创建支付对象、库存对象和订单对象
alipay = Alipay()
wechat_pay = WeChatPay()
inventory = Inventory(10)

order1 = Order("12345", 2)
order2 = Order("67890", 1)

# 模拟用户下单并输出结果
print("用户使用支付宝支付 200 元，购买了2件商品")
print("支付结果：", order1.place_order(alipay, inventory))
print("当前库存数量：", inventory.quantity)

print("用户使用微信支付 100 元，购买了1件商品")
print("支付结果：", order2.place_order(wechat_pay, inventory))
print("当前库存数量：", inventory.quantity)
