

from app.models import User, Wallet

def test_add_expense_success(db_session, client):
    user = User(login="test1")
    db_session.add(user)
    db_session.flush()

    wallet = Wallet(name = "card", balance = 200, user_id = user.id)
    db_session.add(wallet)
    db_session.commit()
    db_session.refresh(wallet)

    responce = client.post("/api/v1/operation/expense",
                            json={
                                "wallet" : "card",
                                "amount" : 50,
                                "description" : "food"
                                },
                                headers = {"Authorization" : f"Bearer {user.login}"})
    print(responce.json())
    assert responce.status_code == 200
    assert responce.json()["wallet_name"] == wallet.name
    assert responce.json()["amount"] == 50
    assert responce.json()["new_balance"] == 150
    assert responce.json()["message"] == "Amount is deducted to balance"

    