function aboutNav() {
    document.getElementById("settings_button").style.backgroundColor = "#333"
    document.getElementById("settings_button").style.borderColor = "#333"
    document.getElementById("about_button").style.backgroundColor = "slateblue"
    document.getElementById("about_button").style.borderColor = "slateblue" 
    document.getElementById("menu_button").style.backgroundColor = "#333"
    document.getElementById("menu_button").style.borderColor = "#333"
    if (document.getElementById('cashier_button')) {
        document.getElementById("cashier_button").style.backgroundColor = "#333"
        document.getElementById("cashier_button").style.borderColor = "#333"
    }
    if (document.getElementById("stock_button")) {
        document.getElementById("stock_button").style.backgroundColor = "#333"
        document.getElementById("stock_button").style.borderColor = "#333"
        document.getElementById("pay_nav_button").style.backgroundColor = "#333"
        document.getElementById("pay_nav_button").style.borderColor = "#333"
    }
    
    document.getElementById('home_div').style.display = 'block'
    document.getElementById('account_div').style.display = 'none'
    document.getElementById('menu_div').style.display = 'none'
    document.getElementById('drink_div').style.display = 'none'
    if(document.getElementById('cashier_div')) {
        document.getElementById('cashier_div').style.display = 'none'
    }
    if(document.getElementById('stock_div')) {
        document.getElementById('stock_div').style.display = 'none'
        document.getElementById('pay_div').style.display = 'none'
    }
}

function settingsNav() {
    document.getElementById("about_button").style.backgroundColor = "#333"
    document.getElementById("about_button").style.borderColor = "#333"
    document.getElementById("settings_button").style.backgroundColor = "slateblue"
    document.getElementById("settings_button").style.borderColor = "slateblue"
    document.getElementById("menu_button").style.backgroundColor = "#333"
    document.getElementById("menu_button").style.borderColor = "#333"
    if (document.getElementById('cashier_button')) {
        document.getElementById("cashier_button").style.backgroundColor = "#333"
        document.getElementById("cashier_button").style.borderColor = "#333"
    }
    if (document.getElementById("stock_button")) {
        document.getElementById("stock_button").style.backgroundColor = "#333"
        document.getElementById("stock_button").style.borderColor = "#333"
        document.getElementById("pay_nav_button").style.backgroundColor = "#333"
        document.getElementById("pay_nav_button").style.borderColor = "#333"
    }

    document.getElementById('account_div').style.display = 'block'
    document.getElementById('home_div').style.display = 'none'
    document.getElementById('menu_div').style.display = 'none'
    document.getElementById('drink_div').style.display = 'none'
    if(document.getElementById('cashier_div')) {
        document.getElementById('cashier_div').style.display = 'none'
    }
    if(document.getElementById('stock_div')) {
        document.getElementById('stock_div').style.display = 'none'
        document.getElementById('pay_div').style.display = 'none'
    }
}

function menuNav() {
    document.getElementById("about_button").style.backgroundColor = "#333"
    document.getElementById("about_button").style.borderColor = "#333"
    document.getElementById("settings_button").style.backgroundColor = "#333"
    document.getElementById("settings_button").style.borderColor = "#333"
    document.getElementById("menu_button").style.backgroundColor = "slateblue"
    document.getElementById("menu_button").style.borderColor = "slateblue"
    if (document.getElementById('cashier_button')) {
        document.getElementById("cashier_button").style.backgroundColor = "#333"
        document.getElementById("cashier_button").style.borderColor = "#333"
    }
    if (document.getElementById("stock_button")) {
        document.getElementById("stock_button").style.backgroundColor = "#333"
        document.getElementById("stock_button").style.borderColor = "#333"
        document.getElementById("pay_nav_button").style.backgroundColor = "#333"
        document.getElementById("pay_nav_button").style.borderColor = "#333"
    }

    document.getElementById('account_div').style.display = 'none'
    document.getElementById('home_div').style.display = 'none'
    document.getElementById('menu_div').style.display = 'block'
    document.getElementById('drink_div').style.display = 'none'
    if(document.getElementById('cashier_div')) {
        document.getElementById('cashier_div').style.display = 'none'
    }
    if(document.getElementById('stock_div')) {
        document.getElementById('stock_div').style.display = 'none'
        document.getElementById('pay_div').style.display = 'none'
    }
}

function cashierNav() {
    document.getElementById("about_button").style.backgroundColor = "#333"
    document.getElementById("about_button").style.borderColor = "#333"
    document.getElementById("settings_button").style.backgroundColor = "#333"
    document.getElementById("settings_button").style.borderColor = "#333"
    document.getElementById("menu_button").style.backgroundColor = "#333"
    document.getElementById("menu_button").style.borderColor = "#333"
    if (document.getElementById("stock_button")) {
        document.getElementById("stock_button").style.backgroundColor = "#333"
        document.getElementById("stock_button").style.borderColor = "#333"
        document.getElementById("pay_nav_button").style.backgroundColor = "#333"
        document.getElementById("pay_nav_button").style.borderColor = "#333"
    }

    document.getElementById("cashier_button").style.backgroundColor = "slateblue"
    document.getElementById("cashier_button").style.borderColor = "slateblue"


    document.getElementById('account_div').style.display = 'none'
    document.getElementById('home_div').style.display = 'none'
    document.getElementById('menu_div').style.display = 'none'
    document.getElementById('drink_div').style.display = 'none'
    document.getElementById('cashier_div').style.display = 'block'
    if(document.getElementById('stock_div')) {
        document.getElementById('stock_div').style.display = 'none'
        document.getElementById('pay_div').style.display = 'none'
    }
}

function payNav() {
    document.getElementById("about_button").style.backgroundColor = "#333"
    document.getElementById("about_button").style.borderColor = "#333"
    document.getElementById("settings_button").style.backgroundColor = "#333"
    document.getElementById("settings_button").style.borderColor = "#333"
    document.getElementById("menu_button").style.backgroundColor = "#333"
    document.getElementById("menu_button").style.borderColor = "#333"
    document.getElementById("cashier_button").style.backgroundColor = "#333"
    document.getElementById("cashier_button").style.borderColor = "#333"
    document.getElementById("stock_button").style.backgroundColor = "#333"
    document.getElementById("stock_button").style.borderColor = "#333"

    document.getElementById("pay_nav_button").style.backgroundColor = "slateblue"
    document.getElementById("pay_nav_button").style.borderColor = "slateblue"

    document.getElementById('account_div').style.display = 'none'
    document.getElementById('home_div').style.display = 'none'
    document.getElementById('menu_div').style.display = 'none'
    document.getElementById('drink_div').style.display = 'none'
    document.getElementById('cashier_div').style.display = 'none'
    document.getElementById('stock_div').style.display = 'none'
    document.getElementById('pay_div').style.display = 'block'
}

function stockNav() {
    document.getElementById("about_button").style.backgroundColor = "#333"
    document.getElementById("about_button").style.borderColor = "#333"
    document.getElementById("settings_button").style.backgroundColor = "#333"
    document.getElementById("settings_button").style.borderColor = "#333"
    document.getElementById("menu_button").style.backgroundColor = "#333"
    document.getElementById("menu_button").style.borderColor = "#333"
    document.getElementById("cashier_button").style.backgroundColor = "#333"
    document.getElementById("cashier_button").style.borderColor = "#333"
    document.getElementById("pay_nav_button").style.backgroundColor = "#333"
    document.getElementById("pay_nav_button").style.borderColor = "#333"

    document.getElementById("stock_button").style.backgroundColor = "slateblue"
    document.getElementById("stock_button").style.borderColor = "slateblue"

    document.getElementById('account_div').style.display = 'none'
    document.getElementById('home_div').style.display = 'none'
    document.getElementById('menu_div').style.display = 'none'
    document.getElementById('drink_div').style.display = 'none'
    document.getElementById('cashier_div').style.display = 'none'
    document.getElementById('stock_div').style.display = 'block'
    document.getElementById('pay_div').style.display = 'none'
}

function drinkPageNav() {
    document.getElementById("about_button").style.backgroundColor = "#333"
    document.getElementById("about_button").style.borderColor = "#333"
    document.getElementById("settings_button").style.backgroundColor = "#333"
    document.getElementById("settings_button").style.borderColor = "#333"
    document.getElementById("menu_button").style.backgroundColor = "#333"
    document.getElementById("menu_button").style.borderColor = "#333"
    if (document.getElementById('cashier_button')) {
        document.getElementById("cashier_button").style.backgroundColor = "#333"
        document.getElementById("cashier_button").style.borderColor = "#333"
    }
    if (document.getElementById("stock_button")) {
        document.getElementById("stock_button").style.backgroundColor = "#333"
        document.getElementById("stock_button").style.borderColor = "#333"
        document.getElementById("pay_nav_button").style.backgroundColor = "#333"
        document.getElementById("pay_nav_button").style.borderColor = "#333"
    }

    document.getElementById('account_div').style.display = 'none'
    document.getElementById('home_div').style.display = 'none'
    document.getElementById('menu_div').style.display = 'none'
    document.getElementById('drink_div').style.display = 'block'
    if(document.getElementById('cashier_div')) {
        document.getElementById('cashier_div').style.display = 'none'
    }
    if(document.getElementById('stock_div')) {
        document.getElementById('stock_div').style.display = 'none'
        document.getElementById('pay_div').style.display = 'none'
    }
}