from server import Server

Myserver = Server("10.22.0.41",15555)
while 1:
    Myserver.GererSession()
    
    
# User1 = info(info.get_user_id(), info.get_user_sociopro(), info.get_user_location())
# User1.show_fiche()