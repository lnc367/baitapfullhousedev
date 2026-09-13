#nhập dữ liệu
ten = input("Nhập tên khách hàng: ")
quang_duong=float(input("Nhập quãng đường (km): "))
xuat_phat=int(input("Nhập giờ xuất phát (0-23): "))
loai_xe=input("Nhập loại xe (4 cho/7 cho): ")
mua_hay_ko=input("Trời có mưa không? (co/khong): ")

#kiểm tra lỗi
if ten == "":
    print("Lỗi: Bạn chưa nhập tên khách hàng.")
elif quang_duong <= 0:
    print("Lỗi: Quãng đường đi phải lớn hơn 0.")
elif xuat_phat < 0 or xuat_phat > 23:
    print("Lỗi: Giờ xuất phát phải nằm trong khoảng 0-23.")
elif loai_xe != "4 cho" and loai_xe != "7 cho":
    print("Lỗi: Loại xe chỉ có thể là '4 cho' hoặc '7 cho'.")

else:
    # tính cước cơ bản
    if loai_xe == "4 cho":
        don_gia = 12000
    else: don_gia = 15000
    cuoc_co_ban = quang_duong * don_gia
    
    #phụ thu giờ cao điểm
    if (6 <=xuat_phat <= 8) or (17 <= xuat_phat <= 19):
        phu_thu_cuoc = cuoc_co_ban * 0.1
    else: phu_thu_cuoc = 0
    
    #phụ thu trời mưa
    if mua_hay_ko == "co":
        phu_thu_mua = quang_duong * 5000
    else: phu_thu_mua = 0
    
    Tong_cuoc = cuoc_co_ban + phu_thu_cuoc + phu_thu_mua
    
    #phân loại chuyến đi
    if quang_duong < 5:
        loai_chuyen_di = "Chuyến ngắn"
    elif quang_duong <= 15:
        loai_chuyen_di = "Chuyến trung bình"
    else: loai_chuyen_di = "Chuyến dài"
    
    #Đánh giá mức độ ưu tiên điều xe (Nested If)
    if (6 <=xuat_phat <= 8) or (17 <= xuat_phat <= 19):
        if loai_chuyen_di == "Chuyến dài":
            uu_tien = "Ưu tiên tài xế nhiều kinh nghiệm"
        else: uu_tien = "Ưu tiên tài xế gần nhất"
    else:
        uu_tien = "Bình thường"
    
    #Đánh giá mức cước (Toán tử ba ngôi)
    muc_cuoc = "Cao" if Tong_cuoc > 150000 else "Thấp"
    if loai_xe == "4 cho":
        loai_xe = "4 chỗ"
    elif loai_xe == "7 cho":
        loai_xe = "7 chỗ"
print("\n--- KẾT QUẢ ---")
print("Khách hàng:", ten)
print("Quãng đường:", quang_duong)
print("Loại xe:", loai_xe)
print("                ")
print("Cước cơ bản:", cuoc_co_ban, "VND")
print("Phụ thu giờ cao điểm:", phu_thu_cuoc, "VND")
print("Phụ thu trời mưa:", phu_thu_mua, "VND")
print("Tổng cước:", Tong_cuoc, "VND")
print("                ")
print("Loại chuyến đi:", loai_chuyen_di)
print("Ưu tien điều xe:", uu_tien)
print("Mức cước:", muc_cuoc)





    
    
