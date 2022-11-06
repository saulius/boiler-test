import sys

def main():
    if len(sys.argv) < 2:
        print('Run with update_inventory.py <host_name>')
        sys.exit(1)

    host_name = sys.argv[1]

    with open("inventory.txt", "a") as f:
        f.write(host_name)

if __name__ == "__main__":
    main()
