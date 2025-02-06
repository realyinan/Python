# 假设有一个电商平台，需要设计一个商品类（Product）用于表示网站上的商品信息，同时还需要设计一个会员类（Member）用于表示平台上的会员信息。要求使用面向对象的思想和多继承的方式，设计并实现这两个类。
# 要求：

# 商品类（Product）具有以下属性和方法：
# 属性：名称（product_name）、价格（product_price）
# 方法：获取商品名称（get_product_name()）、获取商品价格（get_product_price()）
# 会员类（Member）具有以下属性和方法：
# 属性：用户名（name）、会员等级（level）
# 方法：获取用户名（get_name()）、获取会员等级（get_level()）
# 会员商品类（MemberProduct）应该继承自商品类和会员类，并具有以下特有的属性和方法：
# 特有属性：折扣（discount）
# 特有方法：获取折扣价格（get_discount_price()），根据会员等级和商品价格计算商品的折扣价格。
# 假设有一个会员“张三”（username = "zhangsan"）是VIP会员（level = "VIP"），购买了一件名为“iPhone12”的商品，价格为5999元，折扣为0.8。
# 请设计并实现上述类，并编写主程序输出以下信息：

# 张三购买的商品名称、价格和折扣价格。
# 参考如下方式创建实例
# zhangsan = Member("张三", "VIP")
# iphone12 = MemberProduct("iPhone12", 5999, 0.8, zhangsan)

class Product():
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def get_product_name(self):
        return self.product_name
    
    def get_product_price(self):
        return self.product_price
    

class Member():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    

class MemberProduct(Product, Member):
    def __init__(self, product_name, product_price, discount, member):
        Product.__init__(self, product_name, product_price)
        Member.__init__(self, member.get_name(), member.get_level())
        self.discount = discount

    def get_discount_price(self):
        return self.discount * self.product_price
    


zhangsan = Member('张三', 'VIP')
iphone12 = MemberProduct('iPhone12', 5999, 0.8, zhangsan)