'''Command-Line Tool
 Covers: Command-line argument parsing and list comprehensions
 Description: Create a script that accepts file names and search terms from the command line, 
processes logs, and outputs filtered results.'''
import argparse
import re

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("search")
    return parser.parse_args()

def filter_logs(filename, keyword):
    try:
        with open(filename, "r") as file:
            matches = [line.strip() for line in file if re.search(keyword, line, re.IGNORECASE)]
            return matches
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


args = parse_arguments()
results = filter_logs(args.filename, args.search)
    
if results:
    print(f"\nFiltered Results ({len(results)} matches):")
    for line in results:
        print(line)
else:
    print("\nNo matching entries found.")

