

try:
    with open('input.txt', 'r') as infile:
        lines = infile.readlines()

    # Modify: Add line numbers and uppercase the content
    modified_lines = [f"{idx + 1}: {line.strip().upper()}\n" for idx, line in enumerate(lines)]

    with open('output.txt', 'w') as outfile:
        outfile.writelines(modified_lines)

    print("✅ File read and modified content written to 'output.txt' successfully.")

except FileNotFoundError:
    print("❌ The file 'input.txt' was not found.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
