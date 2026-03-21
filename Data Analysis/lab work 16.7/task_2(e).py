# 2. Re-Indexing & Altering Labels
import pandas as pd

league = pd.DataFrame({
    "Team": ["A", "B", "C"],
    "Wins": [10, 8, 6],
    "Losses": [2, 4, 6],
    "Points": [30, 24, 18]
})

print("Original Order:")
print(league)

print("----------------------------------------------")

# Reorder columns
league_reordered = league.reindex(columns=["Team", "Points", "Wins", "Losses"])

print("\nReordered Columns:")
print(league_reordered)

