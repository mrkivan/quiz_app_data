import json
import os

def validate_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        print(f"Error in {os.path.basename(file_path)}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error with {os.path.basename(file_path)}: {e}")
        return False

def check_quiz_directory(directory):
    print(f"\nChecking directory: {directory}")
    valid_count = 0
    invalid_files = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(f"\nValidating {filename}...")
            if validate_json_file(file_path):
                print(f"✅ {filename} is valid JSON")
                valid_count += 1
            else:
                print(f"❌ {filename} has JSON syntax errors")
                invalid_files.append(filename)
    
    total_files = len([f for f in os.listdir(directory) if f.endswith('.json')])
    print(f"\nValidation complete for {directory}:")
    print(f"Total files: {total_files}")
    print(f"Valid files: {valid_count}")
    print(f"Invalid files: {len(invalid_files)}")
    if invalid_files:
        print("\nList of invalid files:")
        for file in invalid_files:
            print(f"- {file}")
    return invalid_files

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    quiz_dirs = ['android_quiz', 'java_quiz', 'kotlin_quiz']
    all_invalid = []
    
    for quiz_dir in quiz_dirs:
        dir_path = os.path.join(base_dir, quiz_dir)
        if os.path.exists(dir_path):
            invalid = check_quiz_directory(dir_path)
            all_invalid.extend([(quiz_dir, f) for f in invalid])
    
    if all_invalid:
        print("\n\nSummary of all invalid JSON files:")
        for quiz_dir, filename in all_invalid:
            print(f"- {quiz_dir}/{filename}")
    else:
        print("\n\nAll JSON files across all directories are valid!")
