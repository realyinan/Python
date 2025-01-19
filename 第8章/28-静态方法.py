# 在开发时，如果需要在类中封装一个方法，这个方法：​    
# ① 既 不需要访问实例属性或者调用实例方法  
# ② 也 不需要访问类属性或者调用类方法
# 这个时候，可以把这个方法封装成一个静态方法

class Game():
    @staticmethod
    def menu():
        print("1. 开始游戏")
        print("2. 暂停游戏")
        print("3. 退出游戏")


Game.menu()

g1 = Game()
g1.menu()