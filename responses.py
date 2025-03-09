user_progress = 1  # Numero corrente globale
last_user = None  # Ultimo utente che ha scritto

def isCountingCorrect(user_input: int, username: str) -> bool:
    global user_progress, last_user

    # Se si prova a scrivere 1, va sempre bene
    if user_input == 1:
        user_progress = 2
        last_user = username
        return True  # ✅

    # Se lo stesso utente prova a scrivere due volte di fila -> ERRORE
    if username == last_user:
        user_progress = 1  # Reset conteggio
        last_user = None
        return False  # ❌

    # Se il numero è corretto -> OK
    if user_input == user_progress:
        user_progress += 1
        last_user = username
        return True  # ✅
    
    # Se il numero è sbagliato -> RESET
    user_progress = 1
    last_user = None
    return False  # ❌