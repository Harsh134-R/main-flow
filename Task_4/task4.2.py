import os
from collections import defaultdict, Counter

# Constants
MAX_FILE_SIZE_MB = 100
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


def parse_log_file(file_path):
    """
    Parses the log file and extracts insights: most frequent IPs, response codes, and URLs.

    Args:
        file_path (str): Path to the log file.

    Returns:
        dict: Aggregated data including frequent IPs, response codes, and URLs.
    """
    # Check file size
    if os.path.getsize(file_path) > MAX_FILE_SIZE_BYTES:
        raise ValueError(f"File size exceeds the allowed limit of {MAX_FILE_SIZE_MB} MB.")

    # for storing aggregated data
    ip_counter = Counter()
    response_code_counter = Counter()
    url_counter = Counter()

    # Read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Example log format: "127.0.0.1 - - [12/Jan/2025:12:34:56 +0000] \"GET /index.html HTTP/1.1\" 200 1024"
                parts = line.strip().split()
                ip = parts[0]  # Extract IP address
                url = parts[6]  # Extract URL (typically the 7th part)
                response_code = parts[8]  # Extract response code (typically the 9th part)

                # Aggregate data
                ip_counter[ip] += 1
                url_counter[url] += 1
                response_code_counter[response_code] += 1

            except IndexError:
                # Handle malformed log lines
                print(f"Warning: Malformed log line skipped - {line.strip()}")
                continue

    # Return the aggregated data
    return {
        "most_frequent_ips": ip_counter.most_common(5),
        "response_codes": response_code_counter.most_common(),
        "most_accessed_urls": url_counter.most_common(5),
    }


def display_results(results):
    """
    Displays the results of the log analysis in a readable format.

    Args:
        results (dict): The aggregated results from the log analysis.
    """
    print("\n=== Log Analysis Results ===\n")

    print("Top 5 Most Frequent IP Addresses:")
    for ip, count in results["most_frequent_ips"]:
        print(f"{ip}: {count} times")

    print("\nHTTP Response Codes Count:")
    for code, count in results["response_codes"]:
        print(f"{code}: {count} times")

    print("\nTop 5 Most Accessed URLs:")
    for url, count in results["most_accessed_urls"]:
        print(f"{url}: {count} times")


if __name__ == "__main__":
    # Example usage
    log_file_path = "access.log"  # Replace with the path to your log file

    try:
        results = parse_log_file(log_file_path)
        display_results(results)
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
