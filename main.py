# main.py

from config import TICKER, BOX_SIZE, REVERSAL_AMOUNT
from data_fetcher import get_stock_data
from pnf_calculator import calculate_pnf_data
from charter import create_pnf_chart

def main():
    """Main function to run the PNF charting application."""
    print(f"Fetching data for {TICKER}...")
    stock_data = get_stock_data(TICKER)

    if stock_data is not None:
        print("Calculating PNF data...")
        pnf_data = calculate_pnf_data(stock_data, BOX_SIZE, REVERSAL_AMOUNT)

        if pnf_data:
            print("Creating PNF chart...")
            create_pnf_chart(pnf_data, TICKER, BOX_SIZE)
        else:
            print("Could not generate PNF data.")

if __name__ == "__main__":
    main()
