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
}