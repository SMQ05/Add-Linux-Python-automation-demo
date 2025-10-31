# log_parser.py — Find errors in log file (like grep)

log_file = "/var/log/nginx/access.log"  # Change if needed
output_file = "errors.txt"

try:
    with open(log_file) as f:
        errors = [line for line in f if "error" in line.lower()]

    with open(output_file, "w") as f:
        f.writelines(errors)

    print(f"Found {len(errors)} errors → saved to {output_file}")
except FileNotFoundError:
    print(f"Error: {log_file} not found. Run on a server with nginx logs.")
