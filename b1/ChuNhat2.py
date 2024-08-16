import Rectangle as rec

menu = {
    1: 'Thêm mới hình chữ nhật',
    2: 'In danh sách hình chữ nhật',
    3: 'Tổng diện tích các hình chữ nhật',
    4: 'Danh sách các hình chữ nhật có chu vi nhỏ nhất',
    'Others': 'Thoát'
}

def print_menu():
    for key in menu.keys():
        print(key,'--',menu[key])

dsHCN=[]

while(True):
    print_menu()
    choice=''
    try:
        choice=int(input('Nhập lựa chọn: '))
    except:
        print('Sai định dạng, hãy chọn lại')
        continue
    if choice==1:
        cr = float(input('Nhập chiều rộng: '))
        cd = float(input('Nhập chiều dài: '))
        hcn = rec.Rectangle(cr, cd)
        dsHCN.append(hcn)
    elif choice==2:
        if not dsHCN:
            print('Danh sách rỗng')
        else:
            for hcn in dsHCN:
                hcn.display()
    elif choice==3:
        dt=0.0
        for hcn in dsHCN:
            dt+=hcn.area()
        print(f'Tổng diện tích các hình chữ nhật: {dt}')
    elif choice==4:
        if not dsHCN:
            print('Danh sách rỗng')
        else:
            min=dsHCN[0].perimeter()
            for hcn in dsHCN:
                if min>hcn.perimeter():
                    min=hcn.perimeter()
            for hcn in dsHCN:
                if hcn.perimeter()==min:
                    hcn.display()
    else:
        print('Thoát chương trình BYE BYE')
        break               