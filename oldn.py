def logo():
	os.system('clear');
print(f"""

\033[1;97m  .M" "bgd  .M" "bgd `7MM" "Yp, 
  ,MI    "Y ,MI    "Y   MM    Yb 
  `MMb.     `MMb.       MM    dP 
    `YMMNq.   `YMMNq.   MM" "bg. 
  .     `MM .     `MM   MM    `Y 
  Mb     dM Mb     dM   MM    ,9 
  P"Ybmmd"  P"Ybmmd"  .JMMmmmd9
-----------------------------------------
 FACEBOOK  :     \033[1;97mShXXX
 WHATAPP   :     \033[1;97m+918000XXXXXX
 
-----------------------------------------
""")
def main():
    input_file = input("Input file path: ").strip()

    start_615 = []
    start_100 = []
    others = []

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line.strip():
                    continue

                uid = line.split("|", 1)[0]

                if uid.startswith("615"):
                    start_615.append(line)
                elif uid.startswith("100"):
                    start_100.append(line)
                else:
                    others.append(line)
        with open("GS.txt", "w", encoding="utf-8") as out:
            for line in start_615 + others + start_100:
                out.write(line + "\n")

        print("✅ Done!\nAccounts saved to output.txt")

    except FileNotFoundError:
        print("❌ File not found. Please check the path and try again.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()