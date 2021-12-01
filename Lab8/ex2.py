class Player:
    def __init__(self,number, shot_accuracy):
        self.number = number
        self.shot_accuracy=shot_accuracy
    def speed_ratio(self,bench_mark_accuracy):
        return self.shot_accuracy/bench_mark_accuracy
def main():
    bench_mark_accuracy=85.0
    p1 = Player(5,65.6)
    ratio=p1.speed_ratio(bench_mark_accuracy)
    print (ratio)

if __name__ == "__main__":
    main()