import time
lights = ["🔴 RED - Stop", "🟡 YELLOW - Slow", "🟢 GREEN - Go"]
durations = [3, 1, 3]
cycles = 2
cycle = 0
while cycle < cycles:
    i = 0
    while i < len(lights):
        print(f"{lights[i]} ({durations[i]}s)")
        time.sleep(durations[i])
        i += 1
    cycle += 1
