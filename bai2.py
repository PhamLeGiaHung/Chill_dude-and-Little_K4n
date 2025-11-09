from guizero import App, Box, Text

# Tạo ứng dụng
app = App(title="Bảng điểm học sinh", width=300, height=250)

# Box chính dùng layout grid
main_box = Box(app, layout="grid")

# --- Tiêu đề ---
title = Text(main_box, text="🎓 Điểm môn học", size=16, grid=[0,0,2,1])
title.bg = "#d9ead3"
title.text_color = "black"

# --- Cột tiêu đề ---
mon_title = Text(main_box, text="Môn", size=12, grid=[0,1])
diem_title = Text(main_box, text="Điểm", size=12, grid=[1,1])

# --- Các môn học và điểm ---
mon1 = Text(main_box, text="Toán", grid=[0,2])
diem1 = Text(main_box, text="8", grid=[1,2])

mon2 = Text(main_box, text="Văn", grid=[0,3])
diem2 = Text(main_box, text="9", grid=[1,3])

mon3 = Text(main_box, text="Anh", grid=[0,4])
diem3 = Text(main_box, text="10", grid=[1,4])

# --- Tính điểm trung bình ---
avg = (8 + 9 + 10) / 3
avg_text = Text(main_box, text=f"Điểm trung bình: {avg:.2f}", size=12, grid=[0,5,2,1])
avg_text.bg = "#cfe2f3"

# --- Thêm viền và căn giữa từng ô ---
for widget in main_box.children:
    widget.width = 15
    widget.height = 2
    widget.text_color = "black"
    widget.master.border = True  # tạo viền cho từng ô

# Hiển thị ứng dụng
app.display()
