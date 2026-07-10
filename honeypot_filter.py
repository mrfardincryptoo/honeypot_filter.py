# Simulate honeypot checks by verifying sell taxes and transfer parameters
def check_token_safety(buy_tax, sell_tax, is_mintable):
    if sell_tax > 10.0 or buy_tax > 10.0:
        return "High Risk: Dynamic Tax Flagged"
    if is_mintable:
        return "Medium Risk: Mint function enabled"
    return "Safe: Standard deployment metrics met"

token_status = check_token_safety(buy_tax=2.5, sell_tax=15.0, is_mintable=False)
print(f"Automated Scan Result: {token_status}")
