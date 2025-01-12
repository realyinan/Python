class Home(object):
    def __init__(self, area, addr):
        self.area = area
        self.addr = addr
        self.containerItem = []

    def __str__(self):
        msg = "房子的面积为" + str(self.area) + "平," + "房子的地址为" + self.addr + ", " "房子内拥有的家具: "
        if len(self.containerItem) > 0:
            for i in self.containerItem:
                msg += i + ','
            msg = msg.strip(',')
        else:
            msg += "暂无任何家具"
        return msg


class Bed(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def getName(self):
        return self.name

newHouse = Home(180, "北京")
print(newHouse)