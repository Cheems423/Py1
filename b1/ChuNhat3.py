import Rectangle as rec

menu = {
    1: 'Thêm mới hình chữ nhật',
    2: 'In danh sách hình chữ nhật',
    3: 'Đọc danh sách từ file',
    4: 'Lưu danh sách vào file',
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
        print('Sai định dạng, hãy nhập lại')
        continue
    if choice==1:
        cr=float(input('Nhập chiều rộng: '))
        cd=float(input('Nhập chiều dài: '))
        hcn = rec.Rectangle(cr,cd)
        dsHCN.append(hcn)
    elif choice==2:
        if not dsHCN:
            print('Danh sách rỗng')
        else:
            for hcn in dsHCN:
                hcn.display()
    elif choice==3:
        fr=open('input.db',mode='r',encoding='utf-8')
        dsHCN=[]
        for line in fr:
            splitLine=line.strip('\n')
            ds=splitLine.split('-')
            cr=float(ds[0])
            cd=float(ds[1])
            hcn=rec.Rectangle(cr,cd)
            dsHCN.append(hcn)
        fr.close()
    elif choice==4:
        fw=open('input.db',mode='w',encoding='utf-8')
        for hcn in dsHCN:
            fw.write(f'{hcn.width}-{hcn.length}-{hcn.perimeter()}-{hcn.area()}\n')
        fw.close()
    else:
        print('Thoát chương trình BYE BYE')
        break