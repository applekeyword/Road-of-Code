import os

from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["cash"]

    stocks = db.execute(
        "SELECT name, symbol, SUM(shares * status) AS shares FROM transactions GROUP BY name HAVING user_id = ?", session["user_id"])

    asset = cash
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["total"] = stock["shares"] * stock["price"]
        asset += stock["total"]

    return render_template("index.html", stocks=stocks, cash=cash, asset=asset)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("missing symbol")

        # make sure the symbol exist
        stock = lookup(symbol)
        if not stock:
            return apology("stock doesn't exist")

        shares = request.form.get("shares")
        if not shares:
            return apology("missing shares")

        if not shares.isdigit():
            return apology("invalid shares")

        shares = int(shares)
        # make sure share must be positive
        if shares <= 0:
            return apology("shares must be greater than 0")

        # check if money is enough
        money = shares * stock["price"]
        cash = db.execute("SELECT cash FROM users where id = ?", session["user_id"])[0]["cash"]
        if money > cash:
            return apology("can't afford")

        # change the user's balance
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - money, session["user_id"])

        db.execute("INSERT INTO transactions (user_id, name, symbol, shares, price, status, time) VALUES (?, ?, ?, ?, ?, 1, ?)",
                   session["user_id"], stock["name"], stock["symbol"], shares, stock["price"], datetime.now())
        flash("Bought!")

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def changepassword():
    """Change the password"""

    if request.method == "POST":
        old_password = request.form.get("password")
        if not old_password:
            return apology("missing password")

        new_password = request.form.get("new-password")
        if not new_password:
            return apology("missing new password")

        # check whether the password is right
        hash_old_password = generate_password_hash(old_password)
        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        print(generate_password_hash("123456"))
        print(hash_old_password)
        print(user[0]["hash"])
        if not check_password_hash(user[0]["hash"], old_password):
            return apology("wrong password")

        # check whether the new password is same as the former
        hash_new_password = generate_password_hash(new_password)
        if check_password_hash(user[0]["hash"], new_password):
            return apology("same as present password")

        # change the password
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash_new_password, session["user_id"])

        return redirect("/login")

    else:
        return render_template("change-password.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    txs = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])
    return render_template("history.html", txs=txs)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "GET":
        return render_template("quote.html")

    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("missing symbol")

        quote = lookup(symbol)
        if not quote:
            return apology("invalid symbol")

        return render_template("quoted.html", quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # ensure username was submitted
        if not username:
            return apology("missing username")

        # ensure password and confirmation was submitted
        if (not password) or (not confirmation):
            return apology("missing password or confirmation")

        # ensure password and confirmation was consistent
        if password != confirmation:
            return apology("the passwords don't match")

        # ensure the username hasn't been registered
        rows = db.execute("SELECT * FROM users where username = ?", username)
        if len(rows) != 0:
            return apology("username has been registered")

        # add new user to the table
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("missing symbol")

        shares = request.form.get("shares")
        if not shares:
            return apology("missing shares")

        if not shares.isdigit():
            return apology("invalid shares")

        shares = int(shares)
        if shares <= 0:
            return apology("invalid shares")

        # get the shares of the stock
        row = db.execute("SELECT SUM(shares * status) AS shares FROM transactions GROUP BY name HAVING user_id = ? AND symbol = ?", session["user_id"], symbol)
        if shares > row[0]["shares"]:
            return apology("too many shares")

        stock = lookup(symbol)
        money = shares * stock["price"]
        cash = db.execute("SELECT cash FROM users where id = ?", session["user_id"])[0]["cash"]
        # update the user's balance
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + money, session["user_id"])

        # write record
        db.execute("INSERT INTO transactions (user_id, name, symbol, shares, price, status, time) VALUES (?, ?, ?, ?, ?, -1, ?)",
                   session["user_id"], stock["name"], stock["symbol"], shares, stock["price"], datetime.now())
        flash("Sold!")

        return redirect("/")

    else:
        symbols = db.execute("SELECT DISTINCT(symbol) AS symbol FROM transactions WHERE user_id = ?", session["user_id"])
        return render_template("sell.html", symbols = symbols)
