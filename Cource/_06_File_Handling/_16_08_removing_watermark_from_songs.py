import os


def rename_mp3_files(directory):
    try:
        i = 0;
        for filename in os.listdir(directory):
            i += 1
            # if filename.__contains__("Jeremy"):
            #     continue
            if filename.endswith("jpg"):
                old_file_path = os.path.join(directory, filename)
                new_filename = filename.replace(filename, f"Jeremy Zucker {i}.jpg").strip()
                new_file_path = os.path.join(directory, new_filename)

                if old_file_path != new_file_path:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")

        print("Renaming completed.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    directory_path = input("Enter the directory path containing image files: ")

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        rename_mp3_files(directory_path)
    else:
        print("Invalid directory path.")
