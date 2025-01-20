# 4. 题干
# 这是一个电商网站的库存管理问题，我们需要管理商品的库存信息。每个商品都有商品编号、名称和库存数量。

# 商品编号   商品名称   数量
#   1	   手机      10
#   2        电视      5
#   3        耳机      20
# 现在有一个用户购买了商品编号为1的商品5件，需要对库存中的商品数量进行调整，如果库存充足，对外售出，我们会输出减少库存的商品信息，否则，我们会输出库存不足的商品信息。
# 提示：通过面向对象处理这个问题

# 属性
# product_id（商品编号）：一个整数，用于唯一标识每个商品。
# name（商品名称）：一个字符串，表示商品的名称。
# stock（库存数量）：一个整数，表示商品的库存数量。
# 方法：
# init(self, product_id, name, stock)：初始化方法，用于创建商品对象。需要传入商品的编号、名称和库存数量。
# reduce_stock(self, quantity)：减少库存的方法。需要传入一个整数quantity表示要减少的库存数量。如果库存充足，并成功减少库存，返回True；否则返回False。
# 数据存储
# products = [
#           Product(1, "手机", 10),
#           Product(2, "电视", 5),
#           Product(3, "耳机", 20)
#       ]


class Product():
    def __init__(self, product_id, name, stock):
        self.product_id = product_id
        self.name = name
        self.stock = stock

    def reduce_stock(self, quantity):
       if self.stock >= quantity:
          self.stock -= quantity
          return True
       return False


products = [
          Product(1, "手机", 10),
          Product(2, "电视", 5),
          Product(3, "耳机", 20)
      ]


def purchase(product_id, quantity):
    for product in products:
        if product.product_id == product_id:
            if product.reduce_stock(quantity):
                print(f"商品编号: {product.product_id}, 商品名称: {product.name}, 剩余库存: {product.stock}")
            else:
                print(f"库存不足: 商品编号: {product.product_id}, 商品名称: {product.name}, 当前库存: {product.stock}")
    print("商品不存在")


purchase(1, 5)