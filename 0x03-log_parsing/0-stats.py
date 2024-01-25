#!/usr/bin/python3
import sys

def process_line(line, metrics):
    try:
        parts = line.split()
        ip_address = parts[0]
        http_status = int(parts[-2])
        file_size = int(parts[-1])

        metrics['total_size'] += file_size
        metrics['line_count'] += 1

        if http_status in [200, 301, 400, 401, 403, 404, 405, 500]:
            metrics['status_counts'][http_status] += 1

    except (ValueError, IndexError):
        pass  # Skip lines with invalid format

def print_statistics(metrics):
    print(f"Total file size: {metrics['total_size']}")

    for status_code in sorted(metrics['status_counts']):
        count = metrics['status_counts'][status_code]
        print(f"{status_code}: {count}")

def main():
    metrics = {'total_size': 0, 'line_count': 0, 'status_counts': {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}}

    try:
        for line in sys.stdin:
            process_line(line.strip(), metrics)

            if metrics['line_count'] % 10 == 0:
                print_statistics(metrics)

    except KeyboardInterrupt:
        print_statistics(metrics)

if __name__ == "__main__":
    main()

