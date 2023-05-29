from pathlib import Path
from microscopy_portfolio import Portfolio

# data path
root = Path(__file__).parent
data_path = root / "data"

# download data
portfolio = Portfolio()
portfolio.denoising.N2V_SEM.download(data_path)

print("Done!")
