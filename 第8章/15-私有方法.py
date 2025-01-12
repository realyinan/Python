class ATM(object):
    def  __card(self):
         print('插卡')

    def  __auth(self):
         print('用户认证')

    def __input(self):
          print('输入取款金额')

    def __print_bill(self):
          print('打印账单')

    def __take_money(self):
          print('取款')

    # 定义一个对外提供服务的公共方法
    def withdraw(self):
          self.__card()
          self.__auth()
          self.__input()
          self.__print_bill()
          self.__take_money()


atm = ATM()
atm.withdraw()