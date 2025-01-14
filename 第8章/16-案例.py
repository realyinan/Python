class Home(object):
    def __init__(self, area, addr):
        self.area = area
        self.addr = addr
        self.containerItem = []

    def addItem(self, item):
        needArea = item.getArea()
        if self.area >= needArea:
            self.containerItem.append(item)
            self.area -= needArea
        else:
            print("无法摆放")
        

    def __str__(self):
        msg = "房子的面积为" + str(self.area) + "平," + "房子的地址为" + self.addr + ", " "房子内拥有的家具: "
        if len(self.containerItem) > 0:
            for i in self.containerItem:
                msg += i.getName() + ','
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
    
    def getArea(self):
        return self.area

newHouse = Home(180, "北京")
bed1 = Bed("席梦思1", 30)
bed2 = Bed("席梦思2", 30)
bed3 = Bed("席梦思3", 30)
bed4 = Bed("席梦思4", 30)
bed5 = Bed("席梦思5", 30)
bed6 = Bed("席梦思6", 30)
bed7 = Bed("席梦思7", 30)
newHouse.addItem(bed1)
newHouse.addItem(bed2)
newHouse.addItem(bed3)
newHouse.addItem(bed4)
newHouse.addItem(bed5)
newHouse.addItem(bed6)
newHouse.addItem(bed7)
print(newHouse)