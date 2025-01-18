from yahoo_fin import stock_info as si

# from yahoo finance

exchange_rate = si.get_live_price("EURBGN=X")

amount_in_eur = int(input("Enter amount EUR:"))
covert_amount = amount_in_eur * exchange_rate

print(f"{amount_in_eur:.2f} equals {covert_amount:.2f} lv")