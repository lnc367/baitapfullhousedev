while True:
    ten = input("Nhập tên khách hàng: ")
    so_luong = int(input("Số lượng sản phẩm: "))
    list_san_pham = ""
    for i in range(so_luong):
        print("\n--- Sản phẩm thứ", i+1, "---")
        ten_san_pham = input("Tên sản phẩm: ")
        don_gia = int(input("Đơn giá: "))
        so_luong= int(input("Số lượng mua: "))
    
    thanh_tien = don_gia * so_luong
    if thanh_tien > 1000000:
        gia_tri= "Sản phẩm có giá trị cao"
    elif thanh_tien > 500000:
        gia_tri= "Sản phẩm có giá trị trung bình"
    else:
        gia_tri= "Sản phẩm có giá trị thấp"
    tong_tien = 0
    
    for i in range(so_luong):
        tong_tien += thanh_tien
        list_san_pham += f"{ten_san_pham} - {so_luong} : {thanh_tien}\n{gia_tri}\n"
    if tong_tien > 500_000:
        giam_gia= tong_tien * 0.1
    elif tong_tien > 300_000:
        giam_gia= tong_tien * 0.05
    else:
        giam_gia=0
    
    thanh_toan = tong_tien - giam_gia
    
    if (tong_tien >= 300_000) and (so_luong >= 3):
        qua= "Được tặng quà"
    else:
        qua= "Không được tặng quà"
    while True:
        check = input("Bạn có muốn tiếp tục đơn hàng không?(Y/N)")
        if check == "N":
            break
        elif check == "Y":
            continue
        else: print("Lựa chọn này không hợp lệ, mời bạn chọn lại")
    
    # TODO: print hóa đơn
    print(f"Tên khách hàng {ten}")
    print("*"*15)
    print("Thông tin sản phẩm bạn đã chọn là:")
    print("*"*15)
    print(list_san_pham)
    print("*"*15)
    print(f"Tổng tiền trước giảm giá: {tong_tien}")
    print(f"Số tiền được giảm: {giam_gia}")
    print('*'*15)
    print(f"Số tiền cần thành toán: {thanh_toan}")
    print(qua)
    break
    
    
    
