from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk, ImageDraw, ImageFont

FONT_NAME = "Arial"
PINK = "#F19ED2"
LIGHT_PINK = "#E8C5E5"
MINT = "#91DDCF"
WHITE = "#F7F9F2"

org_img = None
tk_img = None
watermarked_img = None

def upload_img():
    """
    Function for uploading an image
    """
    global tk_img, org_img 
    file_path = askopenfilename(title="Select an Image", 
                                filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        org_img = Image.open(file_path)
        show_img(org_img)

def show_img(image):
    """
    Function for displaying an image
    """
    global tk_img        
    img_width, img_height = image.size
    canvas_width, canvas_height = 500, 500
    scale=min(canvas_width/img_width, canvas_height/img_height)
    new_img_width= int(img_width*scale)
    new_img_height=int(img_height*scale)
    resized_img=image.resize((new_img_width, new_img_height), 
                             Image.Resampling.LANCZOS)
    tk_img = ImageTk.PhotoImage(resized_img)
    canvas.delete("all")
    canvas.create_image(253, 253, image=tk_img)

def add_txt():
    """
    Function to add watermark on an image
    """
    global org_img, watermarked_img
    if org_img:
        watermark_txt = askstring(title="Add text", 
                                  prompt="Insert your watermark:")
        watermarked_img=org_img.copy()
        draw=ImageDraw.Draw(watermarked_img)
        img_width, img_height =watermarked_img.size
        font=ImageFont.load_default(15)
        font_bbox=font.getbbox(watermark_txt)
        font_width, font_height = font_bbox[2],font_bbox[3]
        x,y=img_width-font_width-15, img_height-font_height-15
        if x<0: x=10
        if y<0: y=10
        draw.text((x,y), watermark_txt, font=font, fill=(255, 255, 255))
        show_img(watermarked_img)

def save_img():
    """
    Function to save the final watermarked image
    """
    global watermarked_img
    if watermarked_img:
        file_path = asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), 
                       ("JPEG files", "*.jpg"), 
                       ("All Files", "*.*")]
        )
        if file_path:
            watermarked_img.save(file_path)

window = Tk()
window.title("Image Watermarking App")
window.minsize(width=750, height=500)
window.config(padx=10, pady=10, bg=WHITE)
window.resizable(True, True) 

top_canvas = Canvas(window, 
                    bg=MINT, 
                    height=50)
top_lbl= top_canvas.create_text(200,30,
                                text ="Upload an image to watermark", 
                                fill="white", 
                                font=(FONT_NAME, 25, "bold"))
top_canvas.pack(fill=X)

canvas = Canvas(window, 
                bg='white', 
                width=500, 
                height=500, 
                highlightbackground=PINK)
canvas.pack(pady=15)

btn_frame=Frame(window)
btn_frame.pack()

upload_img_button = Button(master=window, 
                           text="Upload", 
                           highlightthickness=0,
                           font=(FONT_NAME,15,'bold'), 
                           bg=PINK,
                           fg=WHITE,
                           highlightbackground=MINT, 
                           highlightcolor=WHITE,
                           width=5, height=2, 
                           command = upload_img)
upload_img_button.pack(in_=btn_frame, side=LEFT,padx=5)

watermark_button = Button(master=window, 
                          text="Add text", 
                          font=(FONT_NAME,15,'bold'), 
                          highlightthickness=0,
                          highlightbackground=MINT,
                          highlightcolor=WHITE,
                          fg=WHITE,
                          bg=PINK,  
                          width=5, height=2, 
                          command = add_txt)
watermark_button.pack(in_=btn_frame, side=LEFT, padx=5)

save_button = Button(master=window, 
                          text="Save", 
                          font=(FONT_NAME,15,'bold'), 
                          highlightthickness=0,
                          highlightbackground=MINT,
                          highlightcolor=WHITE,
                          fg=WHITE,
                          bg=PINK,  
                          width=5, height=2, 
                          command = save_img)
save_button.pack(in_=btn_frame, side=LEFT, padx=5)

window.mainloop()