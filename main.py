import data
import utils
import os

count = 0
os.system(f"title {data.title}")

while True:
    try:
        text = input(data.prompt)

        if not text.strip():
            continue
        if text in ["quit", "exit", "q", "end"]:
            break
        if text in ["cls", "clear"]:
            utils.flush()
            continue
        if text == "log":
            utils.log("log.txt", count, "base_log.txt", count)

        os.system(text)

    except Exception as err:
        with open("log.txt", "a") as file:
            count += 1
            file.write(f"{count}. {err}\n")
    except KeyboardInterrupt:
        print("\nExiting...")        
        break
