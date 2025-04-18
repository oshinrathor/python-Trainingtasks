from datetime import datetime

log_file = 'chapter1.txt'

print("Chat logger started. Type your messages below. Type 'exit' to stop.\n")

while True:
    user_input = input("> ")
    if user_input.strip().lower() == "exit":
        print("Chat session ended.")
        break

    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare log entry
    log_entry = f"[{timestamp}] {user_input}\n"

    # Write to log file
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)
