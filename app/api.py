from flask import Flask, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
from src.mongo_accounts_repository import MongoAccountsRepository

app = Flask(__name__)
registry = AccountRegistry()
repo = MongoAccountsRepository()

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")

    for acc in registry.get_all_accounts():
        if acc.pesel == data["pesel"]:
            return jsonify("Account with this pesel already exists."), 409

    account = PersonalAccount(data["first_name"], data["last_name"], data["pesel"])
    if "balance" in data:
        account.balance = data["balance"]
    registry.add_account(account)
    return jsonify({"message": "Account created"}), 201

@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.get_all_accounts()
    accounts_data = [{"first_name": acc.first_name,
                      "last_name": acc.last_name,
                      "pesel": acc.pesel,
                      "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200
#
@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = registry.get_account_count()
    return jsonify({"count": count}), 200
#
@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    acc = registry.get_account_by_pesel(pesel)
    if acc is None:
        return jsonify("No account found."), 404

    return jsonify({"first_name": acc.first_name, "last_name": acc.last_name, "pesel": acc.pesel, "balance": acc.balance}), 200
#
@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    acc = registry.get_account_by_pesel(pesel)

    if acc is None:
        return jsonify("No account found."), 404

    data = request.get_json()

    for el in data.keys():
        if el == "pesel":
            return jsonify("Update error. Can't update pesel"), 405

    for el, val in data.items():
        setattr(acc, el, val)

    return jsonify("Account updated"), 200
#
@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    for el in registry.get_all_accounts():
        if el.pesel == pesel:
            registry.get_all_accounts().remove(el)
            return jsonify("Account deleted"), 200

    return jsonify("No account found."), 404

@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def account_transfer(pesel):
    acc = registry.get_account_by_pesel(pesel)
    if acc is None:
        return jsonify("Account not found."), 404

    data = request.get_json()

    if data["type"] == "incoming":
        acc.incoming_transfer(data["amount"])
        return jsonify("Zlecenie przyjęto do realizacji."), 200
    elif data["type"] == "outgoing":
        tempbalance = acc.balance
        acc.outgoing_transfer(data["amount"])
        if acc.balance == tempbalance:
            return jsonify("Insufficient funds."), 422
        return jsonify("Zlecenie przyjęto do realizacji."), 200
    elif data["type"] == "express":
        tempbalance = acc.balance
        acc.express_transfer(data["amount"])
        if acc.balance == tempbalance:
            return jsonify("Insufficient funds."), 422
        return jsonify("Zlecenie przyjęto do realizacji."), 200
    else:
        return jsonify("Zły typ przelewu."), 406

@app.route("/api/accounts/save", methods=['POST'])
def save_accounts():
    repo.save_all(registry.get_all_accounts())
    return jsonify("DB Saved"), 200

@app.route("/api/accounts/load", methods=['POST'])
def load_accounts():
    repo.load_all(registry)

    return jsonify("DB Loaded"), 200