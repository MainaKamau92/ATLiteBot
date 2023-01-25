XPATH_MAP = {
    "auth_service": {
        'username': '//*[@id="txtLogin"]',
        'password': '//*[@id="txtPassword"]',
        'submit': '//*[@id="btnLogin"]'
    },
    "finance_service": {
        'available_funds_btn': '//*[@id="btnLinkAvailableFund"]',
        'finance_data_table': '//*[@id="tbl_ATLiteAvailableFundsForNormal"]/tbody',
        'available_transfer_btn': '//*[@id="btnLinkFundTransfer"]',
        'transfer_amount_input': '//*[@id="txtPayReqAmount"]',
        'pay_mode_select': '//*[@id="lstPayType"]',
        'transfer_remarks_input': '//*[@id="txtPayReqRemarks"]',
        'transfer_submit_btn': '//*[@id="btnSubmit"]',
        'transfer_confirm_btn': '//*[@id="btn_WithdrawSubmit"]',
    },
    "market_service": {
        'market_data_body': '/html/body/form/div[3]/div/div[65]/div[3]/div[2]/table/tbody',
        'table_header': '/html/body/form/div[3]/div/div[65]/div[3]/div[1]/div/table/thead',
    },
    "order_service": {
        'market_data_body': '/html/body/form/div[3]/div/div[65]/div[3]/div[2]/table/tbody',
        'order_sell_btn': '//*[@id="rdoOrderTypeSell"]',
        'order_buy_btn': '//*[@id="rdoOrderTypeBuy"]',
        'trade_type_select': '//*[@id="lstBorder"]',
        'trade_order_quantity': '//*[@id="txtOrderQty"]',
        'trade_order_price': '//*[@id="txtOrderPrice"]',
        'trade_order_date': '//*[@id="txtOrderValidUpto"]',
        'trading_mode_select': '//*[@id="lstTradingMode"]',
        'order_validate_transaction': '//*[@id="btnOrderSubmit"]',
        'order_confirm_transaction': '//*[@id="btnOSubmit"]',
    },
    "portfolio_service": {
        'portfolio_valuation_btn': '//*[@id="btnLinkPortfolioValuation"]',
        'portfolio_details_btn': '//*[@id="immpvssd"]',
        'portfolio_value_free_btn': '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/div[2]/table/tbody/tr[3]/td[2]',
        'unsettled_purchase_value_btn': '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/div[2]/table/tbody/tr[4]/td[2]',
        'portfolio_value_frozen_btn': '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/div[2]/table/tbody/tr[5]/td[2]/i',
        'market_data_body': '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/center/div/table/tbody',
        'table_header': '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/center/center/div/table/thead',
    },
}