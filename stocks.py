def stock_func():
    import yfinance as yf
    method_choice = input("Enter your choice (e.g., info, actions): ").strip().lower()
    if method_choice == "if":
        index_funds()
    stock_input = input("Enter the ticker symbol for the stock or stocks you want (e.g., NVDA): ").strip()
    ticker_list = stock_input.split()

    ticker_symbols = ",".join(ticker_list)
    tickers = yf.Tickers(ticker_symbols)

    def actions():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].actions
                print(f"{ticker} actions: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def analyst_price_targets():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].analyst_price_targets
                print(f"{ticker} analyst_price_targets: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def balance_sheet():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].balance_sheet
                print(f"{ticker} balance_sheet: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def balancesheet():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].balancesheet
                print(f"{ticker} balancesheet: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def basic_info():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].info
                print(f"{ticker} basic_info: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def calendar():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].calendar
                print(f"{ticker} calendar: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def capital_gains():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].capital_gains
                print(f"{ticker} capital_gains: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def cash_flow():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].cash_flow
                print(f"{ticker} cash_flow: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def cashflow():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].cashflow
                print(f"{ticker} cashflow: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def dividends():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].dividends
                print(f"{ticker} dividends: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def earnings():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].earnings
                print(f"{ticker} earnings: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def earnings_dates():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].earnings_dates
                print(f"{ticker} earnings_dates: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def earnings_estimate():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].earnings_estimate
                print(f"{ticker} earnings_estimate: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def earnings_history():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].earnings_history
                print(f"{ticker} earnings_history: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def eps_revisions():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].eps_revisions
                print(f"{ticker} eps_revisions: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def eps_trend():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].eps_trend
                print(f"{ticker} eps_trend: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def fast_info():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].fast_info
                print(f"{ticker} fast_info: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def financials():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].financials
                print(f"{ticker} financials: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def funds_data():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].funds_data
                print(f"{ticker} funds_data: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def growth_estimates():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].growth_estimates
                print(f"{ticker} growth_estimates: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def history_metadata():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].history_metadata
                print(f"{ticker} history_metadata: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def income_stmt():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].income_stmt
                print(f"{ticker} income_stmt: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def incomestmt():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].incomestmt
                print(f"{ticker} incomestmt: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def info():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].info
                print(f"{ticker} info: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def insider_purchases():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].insider_purchases
                print(f"{ticker} insider_purchases: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def insider_roster_holders():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].insider_roster_holders
                print(f"{ticker} insider_roster_holders: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def insider_transactions():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].insider_transactions
                print(f"{ticker} insider_transactions: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def institutional_holders():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].institutional_holders
                print(f"{ticker} institutional_holders: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def isin():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].isin
                print(f"{ticker} isin: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def major_holders():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].major_holders
                print(f"{ticker} major_holders: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def mutualfund_holders():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].mutualfund_holders
                print(f"{ticker} mutualfund_holders: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def news():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].news
                print(f"{ticker} news: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def options():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].options
                print(f"{ticker} options: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def quarterly_balance_sheet():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].quarterly_balance_sheet
                print(f"{ticker} quarterly_balance_sheet: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def quarterly_balancesheet():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].quarterly_balancesheet
                print(f"{ticker} quarterly_balancesheet: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def quarterly_cash_flow():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].quarterly_cash_flow
                print(f"{ticker} quarterly_cash_flow: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def quarterly_cashflow():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].quarterly_cashflow
                print(f"{ticker} quarterly_cashflow: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def quarterly_earnings():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].quarterly_earnings
                print(f"{ticker} quarterly_earnings: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def quarterly_financials():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].quarterly_financials
                print(f"{ticker} quarterly_financials: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def quarterly_income_stmt():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].quarterly_income_stmt
                print(f"{ticker} quarterly_income_stmt: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def quarterly_incomestmt():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].quarterly_incomestmt
                print(f"{ticker} quarterly_incomestmt: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def recommendations():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].recommendations
                print(f"{ticker} recommendations: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def recommendations_summary():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].recommendations_summary
                print(f"{ticker} recommendations_summary: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def revenue_estimate():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].revenue_estimate
                print(f"{ticker} revenue_estimate: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def sec_filings():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].sec_filings
                print(f"{ticker} sec_filings: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def shares():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].shares
                print(f"{ticker} shares: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def splits():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].splits
                print(f"{ticker} splits: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def sustainability():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].sustainability
                print(f"{ticker} sustainability: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")

    def upgrades_downgrades():
        for ticker in ticker_list:
            try:
                info1 = tickers.tickers[ticker].upgrades_downgrades
                print(f"{ticker} upgrades_downgrades: {info1}")
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            except KeyError:
                print(f"Stock symbol {ticker} not found.")



    if method_choice == "actions":
        actions()
    elif method_choice == "analyst_price_targets":
        analyst_price_targets()
    elif method_choice == "balance_sheet":
        balance_sheet()
    elif method_choice == "balancesheet":
        balancesheet()
    elif method_choice == "basic_info":
        basic_info()
    elif method_choice == "calendar":
        calendar()
    elif method_choice == "capital_gains":
        capital_gains()
    elif method_choice == "cash_flow":
        cash_flow()
    elif method_choice == "cashflow":
        cashflow()
    elif method_choice == "dividends":
        dividends()
    elif method_choice == "earnings":
        earnings()
    elif method_choice == "earnings_dates":
        earnings_dates()
    elif method_choice == "earnings_estimate":
        earnings_estimate()
    elif method_choice == "earnings_history":
        earnings_history()
    elif method_choice == "eps_revisions":
        eps_revisions()
    elif method_choice == "eps_trend":
        eps_trend()
    elif method_choice == "fast_info":
        fast_info()
    elif method_choice == "financials":
        financials()
    elif method_choice == "funds_data":
        funds_data()
    elif method_choice == "growth_estimates":
        growth_estimates()
    elif method_choice == "history_metadata":
        history_metadata()
    elif method_choice == "income_stmt":
        income_stmt()
    elif method_choice == "incomestmt":
        incomestmt()
    elif method_choice == "info":
        info()
    elif method_choice == "insider_purchases":
        insider_purchases()
    elif method_choice == "insider_roster_holders":
        insider_roster_holders()
    elif method_choice == "insider_transactions":
        insider_transactions()
    elif method_choice == "institutional_holders":
        institutional_holders()
    elif method_choice == "isin":
        isin()
    elif method_choice == "major_holders":
        major_holders()
    elif method_choice == "mutualfund_holders":
        mutualfund_holders()
    elif method_choice == "news":
        news()
    elif method_choice == "options":
        options()
    elif method_choice == "quarterly_balance_sheet":
        quarterly_balance_sheet()
    elif method_choice == "quarterly_balancesheet":
        quarterly_balancesheet()
    elif method_choice == "quarterly_cash_flow":
        quarterly_cash_flow()
    elif method_choice == "quarterly_cashflow":
        quarterly_cashflow()
    elif method_choice == "quarterly_earnings":
        quarterly_earnings()
    elif method_choice == "quarterly_financials":
        quarterly_financials()
    elif method_choice == "quarterly_income_stmt":
        quarterly_income_stmt()
    elif method_choice == "quarterly_incomestmt":
        quarterly_incomestmt()
    elif method_choice == "recommendations":
        recommendations()
    elif method_choice == "recommendations_summary":
        recommendations_summary()
    elif method_choice == "revenue_estimate":
        revenue_estimate()
    elif method_choice == "sec_filings":
        sec_filings()
    elif method_choice == "shares":
        shares()
    elif method_choice == "splits":
        splits()
    elif method_choice == "sustainability":
        sustainability()
    elif method_choice == "upgrades_downgrades":
        upgrades_downgrades()
    else:
        print("Invalid input, please try again.")

def index_funds():
    import yfinance as yf
    method_choice = input("Enter your Index Fund ticker symbol here: ").strip()
    if_input = input("What data would you like to retrieve: ")

    ticker = yf.Ticker(method_choice)

    def long_business_summary():
        try:
            info1 = ticker.info.get('longBusinessSummary', None)
            if info1:
                print(f"{method_choice} fund description:")
                print(info1)
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            else:
                print(f"No description available for {method_choice}")
        except KeyError:
            print(f"Stock symbol {method_choice} not found")

    def history():
        try:
            info1 = ticker.info.get('history', None)
            if info1:
                print(f"{method_choice} history: ")
                print(info1)
                with open("stocks.txt", "w") as file:
                    file.write(str(info1))
            else:
                print(f"No description available for {method_choice}")
        except KeyError:
            print(f"Stock symbol {method_choice} not found")

    if if_input.lower() == "long business summary":
        long_business_summary()
    elif if_input.lower() == "history":
        history()

stock_func()
