def info(use_json: bool = True):
    import os
    if not os.path.exists("config.json"):
        print ("No config file found! Please create one. Trying .env")
        use_json = False
    if use_json:
        import json
        with open("config.json", "r", encoding="UTF-8") as f:
            return json.load(f)
    if not use_json:
        import sys
        from dotenv import load_dotenv
        load_dotenv()
        if os.getenv("TOKEN") is None:
            print("TOKEN not found in .env! Please create it.")
            sys.exit()
        if os.getenv("OWNERID") is None:
            print("OWNERID not found in .env! Please create it.")
            sys.exit()
        if os.getenv("BRANCH") is None:
            print("BRANCH not found in .env! Please create it.")
            sys.exit()
        return {
            "Token": os.getenv("TOKEN"),
            "OwnerID": os.getenv("OWNERID"),
            "Branch": os.getenv("BRANCH"),
        }
