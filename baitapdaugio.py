def print_menu():
    print("="*40)
    print("   QUẢN LÝ KHO HÀNG - GROCERY STORE")
    print("="*40)
    print("""
1. Xem danh sách tồn kho
2. Nhập thêm hàng hóa mới
3. Cập nhật số lượng tồn kho theo ID
4. Thoát chương trình
    """)
    print("="*40)
    
def check_list_hang(list_hang):
    if not list_hang:
        print("Kho hàng hiện đang trống!")
        return True
    
def display_kho(list_hang):
    if not list_hang:
        print("Kho hàng hiện đang trống!")
        return
    print("    ----- DANH SÁCH TỒN KHO -----")
    print(f"{'ID':<6} | {'Tên hàng hóa':<15} | {'Số lượng tồn'}")
    print("-"*40)
    for sp in list_hang:
        print(f"{sp['id']:<6} | {sp['name']:<15} | {sp['quantity']}")
    print("-"*40)

def check_bo_trong(message):
    while True:
        check = input(f"Nhập {message.lower()}: ")
        if not check:
            check = input(f"{message} không được để trống! Nhập lại: ")
        return check
    
def add_item(list_hang):
    print("--- NHẬP HÀNG HÓA MỚI ---")
    id = check_bo_trong("Mã hàng hóa(ID)")
    name = check_bo_trong("Tên hàng hóa")
    while True:
        quantity = int(input("Nhập số lượng tồn kho: "))
        if quantity <=0:
            print("Số lượng phải lớn hơn 0!")
        else:
            break
    list_hang.append({
        "ID": id,
        "name": name,
        "quantity": quantity
    })
    print("Thêm hàng hóa vào kho thành công!")

def check_exist_hang(list_hang,id):
    for hang in list_hang:
        if hang['id'] == id:
            return hang
    return False
    
def update_quantity(list_hang):
    if check_list_hang(list_hang):
        return
    print("--- CẬP NHẬT SỐ LƯỢNG HÀNG TỒN KHO ---")    
    code = input("Nhập mã hàng hóa cần sửa: ")
    tim_hang = check_exist_hang(list_hang, code)
    if not tim_hang:
        print(f"Không tìm thấy hàng hóa có mã [{code}]")
    print(f"Tìm thấy hàng hóa: {tim_hang['name']} (Số lượng hiện tại: {tim_hang['quantity']})")
    while True:
        new_quan = int(input('Nhập số lượng mới: '))
        if new_quan <=0:
            print("Số lượng không được nhỏ hơn 0!")
        else:
            break
    tim_hang['quantity'] = new_quan
    print("Cập nhật số lượng thành công!")
    
list_hang = [{
    "id": "G9", "name": "gạo", "quantity": 30 
}]

def main():
    print_menu()
    while True:
        choice = input("Nhập vào lựa chọn của bạn: ")
        if choice == "1":
            display_kho(list_hang)
        elif choice == "2":
            add_item(list_hang)
        elif choice == "3":
            update_quantity(list_hang)
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng phần mềm!")
            print("[Chương trình kết thúc]")
            break
        else:
            print("Lựa chọn không hợp lệ!")
            
if __name__ == "__main__":
    main()
