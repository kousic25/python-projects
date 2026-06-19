batterylevel = 100
screenbrightnesshigh = True
print("Device un-plugged. Monitoring battery health...")
while batterylevel > 0:
    print(f"🔋 Battery status: {batterylevel}%")
    if screenbrightnesshigh:
        batterylevel -= 25
    else:
        batterylevel -= 10
print(" 0% - Battery completely depleted. Shutting down system.")