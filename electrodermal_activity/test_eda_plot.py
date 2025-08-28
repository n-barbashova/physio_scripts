import pandas as pd
import matplotlib.pyplot as plt

# Load your Ledalab input .txt file
file_path = "/Users/nadezhdabarbashova/Documents/fmcc_EDA/timing_files_whole_60_seconds/49_run1_countdown_endonly.txt"
df = pd.read_csv(file_path, sep='\t', header=None, names=["timepoint", "EDA", "EVENT"])

# Plot EDA over time
plt.figure(figsize=(10, 4))
plt.plot(df["timepoint"], df["EDA"], label="EDA (µS)")
plt.xlabel("Time (s)")
plt.ylabel("EDA (µS)")
plt.title("Raw EDA signal over 60 seconds")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
