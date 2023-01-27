import customtkinter as cutk

cutk.set_appearance_mode("dark")
cutk.set_default_color_theme("dark-blue")

root = cutk.CTk()
root.geometry("400x500")

def scrap():
    print("Test")

frame = cutk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = cutk.CTkLabel(master=frame, text="YT Scraper")
label.pack(pady=12, padx=10)

entry = cutk.CTkEntry(master=frame, placeholder_text="Youtube URL")
entry.pack(pady=12, padx=10)

checkbox=cutk.CTkCheckBox(master=frame, text="Title")
checkbox.pack(pady=12, padx=10)
checkbox=cutk.CTkCheckBox(master=frame, text="Embed Link")
checkbox.pack(pady=12, padx=10)
checkbox=cutk.CTkCheckBox(master=frame, text="Keywords")
checkbox.pack(pady=12, padx=10)
checkbox=cutk.CTkCheckBox(master=frame, text="Description")
checkbox.pack(pady=12, padx=10)
checkbox=cutk.CTkCheckBox(master=frame, text="thumbnail")
checkbox.pack(pady=12, padx=10)

button = cutk.CTkButton(master=frame, text="scrap", command=scrap)
button.pack(pady=12, padx=10)

root.mainloop()





# from pytube import YouTube
# import re
# url_list=["https://www.youtube.com/shorts/e4yB9nmc2Iw",
#           "https://www.youtube.com/watch?v=fW_OS3LGB9Q",
#           "https://www.youtube.com/watch?v=EygCjCrqtyA",
#           "https://www.youtube.com/watch?v=dfyZBYL7D4U",
#           "https://youtube.com/shorts/JtrxEtawLqs?feature=share"]
# urls = list(map(lambda x:YouTube(x),url_list))
# Titles = list(map(lambda x:re.sub(r'\s+', ' ', re.sub(r'#\w+', '', x.title)),urls))
# booleans = list(map(lambda x:("no", "yes") [x.length < 60],urls))
# Keywords = list(map(lambda x:', '.join(x.keywords+re.findall(r'#(\w+)', x.title)),urls))
# Embed_Links = list(map(lambda x:"https://www.youtube.com/embed/"+x.video_id,urls))
# Descriptions = list(map(lambda x:x.description,urls))
# thumbnail_url = list(map(lambda x:x.thumbnail_url,urls))

# import csv

# # Open a .csv file for writing
# with open('last.csv', 'w') as f:
#     # Create a CSV writer
#     writer = csv.writer(f)
#     # Write the dates and times to the .csv file
#     writer.writerow(['Titles', 'Embed Links', 'Shorts', 'Keywords'])
#     writer.writerows(zip(Titles, Embed_Links, booleans, Keywords))
#     #writer.writerows([[time] for time in times])