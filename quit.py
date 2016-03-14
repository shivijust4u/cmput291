import session

def quit_callback(frame):
	session.db.close_connection()
	frame.quit()	