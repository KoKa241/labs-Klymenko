
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0) -> None:
        try:
            self._hours = int(hours)
            self._minutes = int(minutes)
            self._seconds = int(seconds)
        except ValueError:
            print("Невірний тип даних")
            exit()

    def __str__(self) -> str:
        return f"{self._hours}:{self._minutes}:{self._seconds}"

    def next_second(self) -> None:
        self._seconds += 1

        if self._seconds == 60:
            self._seconds = 0
            self._minutes += 1

        if self._minutes == 60:
            self._minutes = 0
            self._hours += 1

    def prev_second(self) -> None:

        self._seconds -= 1

        if self._seconds < 0:
            self._seconds = 59
            self._minutes -= 1

        if self._minutes < 0:
            self._minutes = 59
            self._hours -= 1


if __name__ == "__main__":

  timer = Timer(10, 10, 59)
  timer.next_second()
  print(timer)
