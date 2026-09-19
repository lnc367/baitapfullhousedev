danh_sach = [[136, 152], ["Lê Nguyên Chương", "Lê Nguyên Minh"], [17,13], [10,9], [10,8], [10,7], ["Giỏi","Giỏi"]]

while True:   
    print("  Chào mừng bạn đến với app quản lý sinh viên!")
    print("-------------------------------------------------")
    choice = input("Vui lòng chọn chức năng mà bạn mong muốn:\n1.Thêm sinh viên\n2.Xem thông tin sinh viên\n3.Xóa sinh viên\n4.Tạo bảng xếp hạng sinh viên\n0.Thoát chương trình\n")

    if choice == "1":
        mssv = int(input("Nhập mã số sinh viên: "))
        if not mssv:
            print("MSSV không được bỏ trống!")
            continue
        
        hvt = input("Nhập họ và tên sinh viên: ")
        if not hvt:
            print("Họ và tên không được bỏ trống!")
            continue
        
        try:
            age = int(input("Nhập tuổi sinh viên: "))
            if not mssv:
                print("Tuổi không được bỏ trống!")
                continue
        except:
            print("Tuổi không hợp lệ")
        try:        
            m = float(input("Nhập điểm môn toán: "))
        except:
            print("Điểm toán không hợp lệ!")
        try:        
            p = float(input("Nhập điểm môn lý: "))
        except:
            print("Điểm lý không hợp lệ!")
        try:        
            c = float(input("Nhập điểm môn hóa: "))
        except:
            print("Điểm hóa không hợp lệ!")
        tong_diem = m + p + c
        loai = "Giỏi" if (tong_diem / 3) >= 8 else ("Khá" if (tong_diem / 3) >= 6.5 else "Trung bình")
        danh_sach.append([mssv, hvt, age, m, p, c, loai])
    elif choice == "2":
        print("--------------------")
        print("Danh sách sinh viên:")
        for ds in danh_sach:
            print(f"{'MSSV':<12} | {'Họ và tên':<20} | {'Tuổi':<12} | {'Điểm Toán':<12} | {'Điểm Lý':<12} | {'Điểm Hóa':<12} | {'Loại':<12}")
            print(f"{ds[0]:<12} | {ds[1]:<20} | {ds[2]:<12} | {ds[3]:<12} | {ds[4]:<12} | {ds[5]:<12} | {ds[6]:<12}")
    elif choice == "3":
        mssv = input("Nhập vào MSSV cần xóa: ")
        check = False
        for student in danh_sach:
            if student[0] == mssv:
                danh_sach.remove(student)
                print("Đã xóa thành công!")
                check = True
                break
        if not check:
            print("Không tìm thấy sinh viên.")
    elif choice == "4":
        diem = []
        for ds in danh_sach:
            tong = ds[3] + ds[4] + ds[5]
            diem.append([ds[0], ds[1], tong])
        diem.reverse(tong)
        for d in diem:
            print(f"{'MSSV':<12} | {'Họ và tên':<20} | {'Tổng điểm':<12} |")       
            print(f"{d[0]:<12} | {d[1]:<12} | {d[2]:<12}")
    elif choice == "0":
        break
    else:
        print("Lựa chọn không hợp lệ!")
                
        