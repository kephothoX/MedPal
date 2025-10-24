import json
import csv


def json_to_csv(json_file_path, csv_file_path):
    """
    Convert a JSON file to CSV format.

    Args:
        json_file_path (str): Path to the input JSON file
        csv_file_path (str): Path to the output CSV file
    """
    try:
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        if not isinstance(data, list):
            print("Error: JSON data must be a list of objects")
            return

        if not data:
            print("Warning: JSON file is empty")
            return

        headers = list(data[0].keys())

        with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(f"Successfully converted {json_file_path} to {csv_file_path}")

    except FileNotFoundError:
        print(f"Error: File {json_file_path} not found")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    json_to_csv("medical_health_facilities.json", "medical_health_facilities.csv")
