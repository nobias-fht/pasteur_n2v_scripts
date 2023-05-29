from pathlib import Path
from microscopy_portfolio import Portfolio

# data path
data_path = Path("data")

# download data
portfolio = Portfolio()
portfolio.denoising.N2V_SEM.download(data_path)

print("Done!")
