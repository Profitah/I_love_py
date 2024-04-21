from datetime import datetime as dt

def correct(HH, MM):
    return abs((dt.strptime(f'2022-01-01 {HH}:{MM}', '%Y-%m-%d %H:%M') - dt(2022, 1, 1, 9)).seconds // 60)

if __name__ == "__main__":
    HH, MM = map(int, input().split())
    print(correct(HH, MM))
