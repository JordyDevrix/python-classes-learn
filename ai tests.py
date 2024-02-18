import subprocess

p_message = input()

prx = ','


def vaw():
    if p_message[0:4] == f"{prx}cs:":
        my_message = p_message.split(':')[1].strip()
        message = f"tgpt '{my_message}'"
        print(message)
        # subprocess.call(f"tgpt 'hi'", shell=True)

        process = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass",
                                  r"tgpt 'hello'"],
                                 stdout=subprocess.PIPE)
        print(process.stdout)


vaw()
