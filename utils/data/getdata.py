def info(use_json: bool = False):
    if use_json:
        import json, os, sys
        if os.path.exists("config.json"):
            with open("config.json", "r", encoding="UTF-8") as f:
                return json.load(f)
        else:
            print ("config.json not found! Please create it.")
            sys.exit()
    if not use_json:
        from dotenv import load_dotenv
        import os, sys
        load_dotenv()
        if os.getenv("TOKEN") is None:
            print("TOKEN not found! Please create it.")
            sys.exit()
        return {
            "Token": os.getenv("TOKEN"),
        }
