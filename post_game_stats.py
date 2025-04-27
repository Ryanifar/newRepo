# Post Game Stats
# COdedex

# Task 1: Create Player Data
player_data = [
    {"name": "Patrick Mahomes", "position": "Quaterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
    {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 1},
]
names = [player["name"] for player in player_data]
print("Player Names:", names)

# Task 2: Analye Player Positions
positions = [player["position"] for player in player_data]
print("Player Positions:", positions)

# Task 3: Update Player Statistics
player_data[0]["yards_gained"] += 50
player_data[0]["touchdowns"] += 1

# Task 4: Calculate Avarage Stats
average_yards = sum(player["yards_gainded"] for player in player_data) / len(player_data)
average_touchdowns = sum(player["touchdowns"] for player in player_data) / len(player_data)
print("Average Yards Gained:", average_yards)
print("Average Touchdowns:", average_touchdowns)