# 假设我们正在开发一个日期处理工具类 DateUtils，其中包含一些用于处理日期的功能。我们希望在这个工具类中定义一个静态方法，用于判断给定的年份是否为闰年。请实现名为 is_leap_year 的方法，该方法接收一个整数参数 year，表示要判断的年份，返回一个布尔值，表示该年份是否为闰年。

class DateUtils():
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    

if __name__ == "__main__":
    test_years = [1900, 2000, 2024, 2023]
    for year in test_years:
        print(f"{year} 是闰年: {DateUtils.is_leap_year(year)}")
