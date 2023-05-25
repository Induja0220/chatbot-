import webbrowser
import random
from tkinter import*
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import simpledialog

chat_color = 'violet'
text_color = 'pink'
button_color = 'purple'

def change_button_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[1]:
        button.config(bg=color[1])

#open new tab
def open_new_tab():
    # Clear the chat window
    chatwin.config(state=NORMAL)
    chatwin.delete("1.0", END)
    chatwin.config(state=DISABLED)

    messagebox.showinfo("New Tab", "Opening a new tab")


#save the chat
def save_chat():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        try:
            with open(file_path, 'w') as file:
                chat_content = chatwin.get("1.0", END)
                file.write(chat_content)
            messagebox.showinfo("Save", "Chat saved successfully!")
        except IOError:
            messagebox.showerror("Error", "Failed to save the chat.")


#change color of chat window
def change_chat_color():
    global chat_color
    new_color = colorchooser.askcolor(color=chat_color)[1]
    if new_color:
        chat_color = new_color
        chatwin.config(bg=chat_color)

def change_text_color():
    global text_color
    new_color = colorchooser.askcolor(color=text_color)[1]
    if new_color:
        text_color = new_color
        msgwin.config(bg=text_color)

def change_button_color():
    global button_color
    new_color = colorchooser.askcolor(color=button_color)[1]
    if new_color:
        button_color = new_color
        button.config(bg=button_color)

def update_widget_colors():
    chatwin.config(bg=chat_color)
    msgwin.config(bg=text_color)
    button.config(bg=button_color)
        
#quit from chat
def quit_chat():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()

#display the message
def send_message():
    message = msgwin.get("1.0", END).strip()
    if message:
        chatwin.config(state=NORMAL)
        chatwin.insert(END, "User: " + message + "\n")
        chatwin.config(state=DISABLED)
        msgwin.delete("1.0", END)

        # Chatbot's response logic
        response = generate_response(message)
        
        if response:
            chatwin.config(state=NORMAL)
            chatwin.insert(END, "Hubba: " + response + "\n")
            chatwin.config(state=DISABLED)
        else:
            web_search_url = "https://www.google.com/search?q=" + message.replace(" ", "+")
            webbrowser.open(web_search_url)
        
        chatwin.see(END)



#tell me a joke
def get_random_joke():
    jokes = ["Why don't scientists trust atoms?\n Because they make up everything!",
        "I wouldn't buy anything with velcro.\n It's a total rip-off.",
        "Why did the scarecrow win an award?\n Because he was outstanding in his field!",
        "I used to play piano by ear.\n But now I use my hands.",
        "What do you call a fish wearing a crown?\n King of the sea!"
    ]
    random_joke = random.choice(jokes)
    return random_joke


#sing a song
def sing_song(song_name):
    if song_name.lower() == "happy birthday":
        lyrics = "Happy birthday to you\nHappy birthday to you\nHappy birthday dear friend\nHappy birthday to you!"
    elif song_name.lower() == "twinkle twinkle little star":
        lyrics = "Twinkle, twinkle, little star\nHow I wonder what you are\nUp above the world so high\nLike a diamond in the sky"
    elif song_name.lower() == "jingle bells":
        lyrics = "Jingle bells, jingle bells\nJingle all the way\nOh, what fun it is to ride\nIn a one horse open sleigh"
    else:
        lyrics = "Sorry, I don't know the lyrics for that song."

    return lyrics

def generate_response(message):
    # Add your response generation logic here
    if message.lower() == "hello" or message.lower() == "hai":
        return "Hello! How can I assist you?"
    elif message.lower() == "how are you?":
        return "I'm an AI chatbot. I don't have feelings, but thanks for asking!"
    elif message.lower() == "bye" or  message.lower() == "goodbye":
        return "Goodbye! Have a nice day."
    elif message.lower() == "tell me a joke" or  message.lower() == "joke":
        return get_random_joke()
    elif message.lower().startswith("sing"):
        song_name = message[5:].strip()
        return sing_song(song_name)
    else:
        return None

root=Tk()
root.title('CHATBOT')
root.geometry('400x500')


#menu
main_menu=Menu(root)

#file_menu
file_menu=Menu(root)
file_menu.add_command(label='New', command=open_new_tab)
file_menu.add_command(label='Save As',command=save_chat)
file_menu.add_command(label='Exit',command=quit_chat)

#edit_menu
edit_menu=Menu(root)
edit_menu.add_command(label='Chatwindow color',command=change_chat_color)
edit_menu.add_command(label='Textwindow color',command=change_text_color)
edit_menu.add_command(label='Button Color', command=change_button_color)

#main_menu
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_command(label='Quit',command=quit_chat)
root.config(menu=main_menu)


# Chat window
chatwin = Text(root, bd=1, bg=chat_color, width=50, height=8)
chatwin.place(x=6, y=6, height=385, width=370)
chatwin.config(state=DISABLED)
chatwin.configure(font=('Comic', 12))

# Text window
msgwin = Text(root, bg=text_color, width=30, height=3)
msgwin.place(x=128, y=400, height=88, width=260)
msgwin.configure(font=('Arial', 12))

# Send button
button = Button(root, text='send', bg=button_color, activebackground='LightBlue', width=12, height=5, font=('comic', 12), command=send_message)
button.place(x=6, y=400, height=88, width=120)

#scroll bar
scbar=Scrollbar(root,command=chatwin.yview())
scbar.place(x=375,y=5,height=385)

# Call the function to update widget colors initially
update_widget_colors()

root.mainloop()
