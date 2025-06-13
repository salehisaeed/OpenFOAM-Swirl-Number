import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

base_directory = Path(__file__).parent
postproc_dir = base_directory / "postProcessing"

radii = 0.1

regions = sorted(set(
    name.replace("swirl_", "").replace("numerator_", "").replace("denominator_", "")
    for name in os.listdir(postproc_dir)
    if name.startswith("swirl_")
))

    
print(f"🔎 Found regions: {regions}")

# --- Process Each Region ---
swirl_data = {}

fig = plt.figure(figsize=(8, 5))

for region in regions:
    print(f"\nProcessing region: '{region}'")
    
    num_path = postproc_dir / f"swirl_numerator_{region}/0/surfaceFieldValue.dat"
    denom_path = postproc_dir / f"swirl_denominator_{region}/0/surfaceFieldValue.dat"

    # --- Read Data and Calculate Swirl Number ---
    num_df = pd.read_csv(num_path, sep='\s+', comment="#", names=["time", "num"])
    denom_df = pd.read_csv(denom_path, sep='\s+', comment="#", names=["time", "denom"])
    merged_df = pd.merge(num_df, denom_df, on="time", how="inner")

    merged_df["swirl"] = merged_df["num"] / (merged_df["denom"] * radii)
    swirl_data[region] = merged_df

    # --- Plotting ---
    plt.plot(merged_df["time"], merged_df["swirl"], label=f"{region}")

# --- Publication-quality Figure Settings ---
# plt.style.use("seaborn-v0_8-whitegrid")
# plt.axi
plt.xlabel("Time (s)", fontsize=15)
plt.ylabel("Swirl Number (S)", fontsize=15)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.tight_layout()
plt.legend(loc="best", fancybox=True, framealpha=0.95, fontsize=13)
plt.show()

fig.savefig(base_directory / "docs/figures/swirl_number_plot.png", dpi=300, bbox_inches='tight')