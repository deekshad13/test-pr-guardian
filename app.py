def get_user(id):
    query = "SELECT * FROM users WHERE id = " + id
    return db.execute(query)

def process_payment(amount, card_number):
    # TODO: add validation later
    print(f"Processing payment of {amount} for card {card_number}")
    return True

def delete_user(id):
    query = "DELETE FROM users WHERE id = " + id
    db.execute(query)
