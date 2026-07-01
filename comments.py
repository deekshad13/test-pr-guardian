import pickle

def render_comment(comment):
    return f"<div>{comment}</div>"  # no escaping, XSS risk

def load_user_session(session_path):
    return pickle.load(open(session_path, 'rb'))  # insecure deserialization

def parse_user_input(raw_data):
    return eval(raw_data)  # arbitrary code execution
