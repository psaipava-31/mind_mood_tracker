from tracker_agent import analyse_entry
from mood_db import log_entry

def main():
    print("Mind and mood tracker")
    user_input = input("How are you feeling today?\n>")

    result = analyse_entry(user_input)
    print("\nAI Insight:\n", result)

    log_entry(user_input,result)
    print("Entry Logged")

if __name__ == "__main__":
    main()
