# 设计一个Game类

# 属性：

# 定义一个类属性top_score记录游戏的历史最高分

# 定义一个实例属性player_name记录当前游戏的玩家姓名

# 方法：

# 静态方法show_help显示游戏帮助信息

# 类方法show_top_score显示历史最高分

# 实例方法start_game开始当前玩家的游戏

class Game():
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @classmethod
    def show_top_score(cls):
        return cls.top_score
    
    @staticmethod
    def show_help():
        print("帮助信息")

    def start_game(self):
        print("开始游戏")