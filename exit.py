def logout_user(user_manager):
    if user_manager.current_user:
        print(f"User {user_manager.current_user} has logged out.")
        user_manager.current_user = None

    return "Logged out successfully."
