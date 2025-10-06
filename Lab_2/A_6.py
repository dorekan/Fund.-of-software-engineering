x = int(input())

hours = (x // 3600) % 24
minutes = (x % 3600) // 60
seconds = x % 60

print(f"{hours}:{minutes:02}:{seconds:02}")