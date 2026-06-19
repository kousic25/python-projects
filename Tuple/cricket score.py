#SPORTS TOURNAMENT
teams = (
    ("Chennai Super Kings", "CSK", 10, 5, 3, 0),
    ("Mumbai Indians",      "MI",  10, 6, 4, 0),
    ("Royal Challengers",   "RCB", 10, 5, 5, 0),
    ("Kolkata Knight Riders","KKR",10, 4, 6, 0),
    ("Delhi Capitals",      "DC",  10, 3, 7, 0),
)
print(f"{'Team':<25} {'Code':<5} {'P':>3} {'W':>3} {'L':>3} {'NR':>4} {'Pts':>5} {'WR%':>7}")
print("-" * 58)
for team, code, played, won, lost, nr in teams:
    points  = won * 2 + nr
    win_rate = (won / played) * 100
    print(f"{team:<25} {code:<5} {played:>3} {won:>3} {lost:>3} {nr:>4} {points:>5} {win_rate:>6.1f}%")
winner = max(teams, key=lambda x: x[3])
print(f"\nLeader: {winner[0]} ({winner[3]} wins)")