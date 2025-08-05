import json

# def load_data():
#     try:
#         with open('youtube.txt', 'r') as file:
#             test = json.load(file)
#           #   print(test)
#           #   print(type(test))
#             return test

#     except FileNotFoundError:
#         return []
#     #    return ["No file found!"]

#     # finally:


# def save_data_helper(videos):
#     with open('youtube.txt', 'w') as file:
#         json.dump(videos, file)


# def list_all_videos(videos):
#     #     for index, video in enumerate(videos, start=1):
#     #         print(f"{index}. {video}")
#     print('\n')
#     print('<=>'*30)
#     for index, video in enumerate(videos, start=1):
#         print(f"{index}. {video['name']}, Duration: {video['time']}")
#     print('\n')
#     print('<=>'*30)
# # def list_all_videos(videos):
# #     print('\n')
# #     print('<=>'*100)
# #     for index, video in enumerate(videos, start=1):

# #         print(f"{index}. {video}")  # Just print the string directly
# #     print('\n')
# #     print('<=>'*100)


# def add_video(videos):
#     name = input("Enter Video Name: ")
#     time = input("Enter Video Length: ")
#     videos.append({'name': name, 'time': time})
#     save_data_helper(videos)


# def update_video(videos):
#     list_all_videos(videos)
#     index = int(input("Which video number do you want to update ?"))
#     if 1 <= index <= len(videos):
#         name = input("Enter the new Video Name: ")
#         time = input("Enter the new Video Time: ")
#         videos[index-1] = {'name': name, 'time': time}
#         save_data_helper(videos)
#     else:
#         print("Invalid index selected!")


# def delete_video(videos):
#     list_all_videos(videos)
#     index = int(input("Which video number do you want to delete ?"))

#     if 1 <= index <= len(videos):
#         del videos[index-1]
#         save_data_helper(videos)
#     else:
#         print("Invalid index selected!")


# def main():
#     videos = load_data()
#     while True:
#         print("YouTube Manager || Choose an Option")
#         print("1. List All Favourite Videos")
#         print("2. Add a YouTube Videos")
#         print("3. Update the YouTube Videos")
#         print("4. Delete a YouTube Videos")
#         print("5. Exit the Application")
#         choice = input("Enter your choice: ")
#     #    print(videos)

#         match choice:
#             case '1':
#                 list_all_videos(videos)
#             case '2':
#                 add_video(videos)
#             case '3':
#                 update_video(videos)
#             case '4':
#                 delete_video(videos)
#             case '5':
#                 break
#             case _:
#                 print("Invalid Choice!")


# if __name__ == "__main__":
#     main()


# ------------------------- File Operations ------------------------- #


def load_data():
    """Loads video data from the JSON file."""
    try:
        with open('youtube.txt', 'r') as file:
            data = json.load(file)
            print("📂 Loaded data:", data)
            print("📄 Data type:", type(data))
            return data
    except FileNotFoundError:
        return []  # Return an empty list if file is not found


def save_data_helper(videos):
    """Saves video data to the JSON file."""
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

# ------------------------- Core Functions ------------------------- #


def list_all_videos(videos):
    """Displays all saved videos in a formatted list."""
    print('\n' + '<=> ' * 30)
    print("🎬 Your Favorite YouTube Videos:\n")

    if not videos:
        print("⚠️  No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            if isinstance(video, dict):
                print(f"{index}. {video['name']} — Duration: {video['time']}")
            else:
                # fallback if data isn't formatted correctly
                print(f"{index}. {video}")

    print('\n' + '<=> ' * 30)


def add_videos(videos):
    """Adds a new video to the list."""
    print("\n➕ Add New Video")
    name = input("📺 Enter Video Name: ")
    time = input("⏱️  Enter Video Duration: ")

    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("✅ Video added successfully!")


def update_videos(videos):
    """Updates an existing video entry."""
    list_all_videos(videos)

    try:
        index = int(input("✏️  Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("📺 Enter new Video Name: ")
            time = input("⏱️  Enter new Duration: ")
            videos[index - 1] = {'name': name, 'time': time}
            save_data_helper(videos)
            print("✅ Video updated successfully!")
        else:
            print("⚠️  Invalid index!")
    except ValueError:
        print("❌ Please enter a valid number!")


def delete_videos(videos):
    """Deletes a video from the list."""
    list_all_videos(videos)

    try:
        index = int(input("🗑️  Enter the video number to delete: "))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_data_helper(videos)
            print("✅ Video deleted successfully!")
        else:
            print("⚠️  Invalid index!")
    except ValueError:
        print("❌ Please enter a valid number!")

# ------------------------- Main Menu ------------------------- #


def main():
    """Main loop that runs the YouTube Manager application."""
    videos = load_data()

    while True:
        print("\n" + "=" * 50)
        print("🎥 YouTube Manager — Choose an Option")
        print("=" * 50)
        print("1️⃣  List All Favourite Videos")
        print("2️⃣  Add a YouTube Video")
        print("3️⃣  Update a YouTube Video")
        print("4️⃣  Delete a YouTube Video")
        print("5️⃣  Exit the Application")
        print("=" * 50)

        choice = input("👉 Enter your choice (1-5): ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                print("\n👋 Exiting YouTube Manager. Goodbye!\n")
                break
            case _:
                print("⚠️  Invalid choice! Please select a valid option.")

# ------------------------- Run the App ------------------------- #

if __name__ == "__main__":
    main()