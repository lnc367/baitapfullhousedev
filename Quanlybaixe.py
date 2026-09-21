def print_menu():
    print("="*40)
    print("    QUẢN LÝ BÃI XE - SMART PARKING")
    print("="*40)
    print(" 1. Check-in (Đăng ký xe vào)")
    print(" 2. Báo cáo tồn kho (Hiển thị danh sách)")
    print(" 3. Tìm kiếm xe (Theo biển số)")
    print(" 4. Check-out (Xử lý xe ra & Tính phí)")
    print(" 5. Thoát chương trình")
    print("="*40)
    
def get_stt_id(list_xe):
    if not list_xe:
        return 0
    return list_xe[-1]["ID"]

def nhap_int_type(message):
    while True:
        try:
            entry_time = int(input(f"Nhập vào {message}: "))
            return entry_time
        except:
            print(f"{message} phải là 1 số")

def check_exist_xe(list_xe,plate):
    if not list_xe:
        return False
    for xe in list_xe:
        if xe['plate'] == plate:
            return xe
    return False

def nhap_data_xe():
    while True:
        plate = input("Nhập biển số xe: ")
        if check_exist_xe(list_xe,plate):
            print("Biển số xe đã tồn tại!")
        else:
            break
    while True:
        type = input("Nhập loại xe: ")
        if type == "Ô tô" or type == "Xe máy":
            break  
    #TODO: giờ vào từ 0-23
    while True:
        entry_time = nhap_int_type("Giờ vào")
        if not (int(entry_time)>=0 or int(entry_time)<=23):
            print("Giờ vào không hợp lệ!")
        else:
            break
    return plate, type, entry_time

def check_in(list_xe):
    
    plate, type, entry_time = nhap_data_xe()

    list_xe.append({
        "ID": get_stt_id(list_xe)+1,
        "plate": plate,
        "type": type,
        "entry_time": entry_time    
    })
    print("Nhập vào thành công!")

def check_list_xe(list_xe):
    if not list_xe:
        print("Bãi xe hiện đang trống!")
        return True

def display_list_xe(list_xe):
    if check_exist_xe(list_xe):
        return
    print(f"{'ID':<4} | {'Biển số xe':<20} | {'Loại xe':<14} | {'Giờ vào':<10}")
    for xe in list_xe:
        print(f"{xe['ID']:<4} | {xe['plate']:<20} | {xe['type']:<14} | {xe['entry_time']:<10}")

def search_xe(list_xe):
    if check_list_xe(list_xe):
        return
    bien_so = input("Nhập vào biển số xe: ")
    xe_finded = check_exist_xe(list_xe, bien_so)
    if not xe_finded:
        print(f"[Lỗi]: Không tìm thấy biển số {bien_so} trong hệ thống")
    print(f"Thông tin chi tiết: {xe_finded}")

def check_out(list_xe):
    bien_so = input("Nhập vào biển số xe: ")
    gio_ra = nhap_int_type("Giờ ra")
    xe = check_exist_xe(list_xe, bien_so)
    
    if not xe:
        print(f"[Lỗi]: Không tìm thấy biển số {bien_so} trong hệ thống")
        return
    if (gio_ra<xe['entry_time'] or gio_ra>23):
        print("[Lỗi: Giờ ra phải sau giờ vào]")
        return
    
    phi_giu_xe = 5000
    tong_phi = phi_giu_xe*(gio_ra - xe['entry_time'])
    print(f"Tổng phí phải trả: {tong_phi}")
    
    #Xóa xe sau thanh toán
    list_xe.remove(xe)
    print(f"[Thành công]: Đã xóa xe ID {xe['ID']} thành công!")
list_xe = [{
    "ID":1,
    "plate": "AB-88844",
    "type": "Xe máy",
    "entry_time": 3
}]
def main():    
    print_menu()
    while True:
        try:
            choice = int(input("Nhập vào lựa chọn của bạn (1-5): "))
        except ValueError:
            print("Phải nhập vào là một số!")
            continue
        if (choice==1):
            check_in(list_xe)            
        elif (choice== 2):
            display_list_xe(list_xe)
        elif choice == 3:
            search_xe(list_xe)
        elif choice == 4:
            check_out(list_xe)
        elif (choice == 5):
            print("Cảm ơn bạn đã sử dụng chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ")
                
            
if __name__ == "__main__":
    main()
        