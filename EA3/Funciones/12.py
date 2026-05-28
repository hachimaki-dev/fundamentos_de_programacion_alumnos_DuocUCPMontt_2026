def es_email_valido(email: str) -> bool:
    if email.count("@") == 1 and email.count(".") >= 1:
        return True
    else:
        return False
    
print(es_email_valido("martin"))
print(es_email_valido("anakin.darthvader@imperiogalactico.gx"))