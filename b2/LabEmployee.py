import matplotlib.pyplot as plt
import Employee as emp

menu = {
    1: 'Tải danh sách từ file',
    2: 'Thêm nhân viên',
    3: 'Hiển thị danh sách nhân viên',
    4: 'Tìm theo mã',
    5: 'Sửa thông tin',
    6: 'Xóa nhân viên',
    7: 'Tăng lương 1 nhân viên',
    8: 'Giảm lương 1 nhân viên',
    9: 'Đếm số nhân viên',
    10: 'Tổng lương hàng tháng',
    11: 'Trung bình lương nhân viên',
    12: 'Trung bình tuổi nhân viên',
    13: 'Danh sách nhân viên có tuổi lớn nhất',
    14: 'Sắp xếp danh sách nhân viên tăng theo lương',
    15: 'Vẽ biểu đồ tương quan lương theo tuổi',
    16: 'Vẽ biểu đồ so sánh lương trung bình các nhóm tuổi 35,50',
    17: 'Vẽ biểu đồ thể hiện phần trăm tổng lương các nhóm tuổi 35,50',
    18: 'Vẽ biểu đồ thể hiện phần trăm số nhân viên các nhóm tuổi 35,50',
    19: 'Lưu file',
    'Others': 'Thoát'
}

def print_menu():
    for key in menu.keys():
        print(key,'--',menu[key])

dsNV=[]

while(True):
    print_menu()
    choice=''
    try:
        choice=int(input('Nhập lựa chọn: '))
    except:
        print('Sai định dạng, hãy nhập lại')
        continue

    #1. Lưu thông tin
    if choice==1:
        fr=open('nv.db',mode='r',encoding='utf-8')
        dsNV=[]
        for line in fr:
            strLine=line.strip('\n')
            ds=strLine.split('-')
            maso=ds[0]
            ten=ds[1]
            tuoi=int(ds[2])
            luong=float(ds[3])
            nv=emp.Emplooyee(maso,ten,tuoi,luong)
            dsNV.append(nv)
        fr.close()
    
    #2. Thêm nhân viên
    elif choice==2:
        maso=input('Nhập mã số: ')
        ten=input('Nhập tên: ')
        tuoi=int(input('Nhập tuổi: '))
        luong=float(input('Nhập lương: '))
        try:
            nv=emp.Emplooyee(maso,ten,tuoi,luong)
        except ValueError as e:
            print(f'Không thêm được nhân viên: {e}')
        dsNV.append(nv)

    #3. In danh sách nhân viên
    elif choice==3:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            for nv in dsNV:
                nv.display()

    #4. Tìm theo mã
    elif choice==4:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            listId={nv.code:nv for nv in dsNV}
            ma=input('Nhập mã cần tìm: ')
            nv=listId.get(ma)
            if nv:
                nv.display()
            else:
                print('Không tìm thấy nhân viên')

    #5. Sửa thông tin
    elif choice==5:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            listId={nv.code:nv for nv in dsNV}
            ma=input('Nhập mã cần cập nhật: ')
            nv=listId.get(ma)
            if nv:
                nv.display()
                menu1 = {
                    1: 'Cập nhật tên: ',
                    2: 'Cập nhật tuổi: ',
                    3: 'Cập nhật lương',
                    'Others': 'Thoát'
                }
                def in_menu():
                    for key in menu1.keys():
                        print(key,'--',menu1[key])
                while(True):
                    in_menu()
                    chon=''
                    try:
                        chon=int(input('Nhập lựa chọn sửa: '))
                    except:
                        print('Sai định dạng, hãy chọn lại')
                        continue
                    if chon==1:
                        ten=input('Nhập tên mới: ')
                        nv.name=ten
                        nv.display()
                    elif chon==2:
                        tuoi=int(input('Nhập tuổi mới: '))
                        nv.age=tuoi
                        nv.display()
                    elif chon==3:
                        luong=float(input('Nhập lương mới: '))
                        nv.salary=luong
                        nv.display()
                    else:
                        print('Dừng cập nhật\n')
                        break
            else:
                print('Không tìm thấy nhân viên')

    #6. Xóa nhân viên
    elif choice==6:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            listId={nv.code: nv for nv in dsNV}
            ma=input('Nhập mã cần xóa: ')
            nv=listId.get(ma)
            if nv:
                nv.display()
                tl=input('Chắc chắn xóa(Y/N): ')
                if tl=='Y':
                    dsNV.remove(nv)        
                    for nv in dsNV:
                        nv.display()
            else:
                print('Không tìm thấy nhân viên')  

    #7. Tăng lương 1 nhân viên
    elif choice==7:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            listId={nv.code: nv for nv in dsNV}
            ma=input('Nhập mã cần tăng lương: ')
            nv=listId.get(ma)
            if nv:
                luong=float(input('Nhập lương cần tăng: '))
                nv.increaseSalary(luong)
                nv.display() 
            else:
                print('Không tìm thấy nhân viên')

    #8.Giảm lương 1 nhân viên
    elif choice==8:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            listId={nv.code: nv for nv in dsNV}
            ma=input('Nhập mã cần giảm lương: ')
            nv=listId.get(ma)
            if nv:
                luong=float(input('Nhập lương cần giảm: '))
                nv.decreaseSalary(luong)
                nv.display() 
            else:
                print('Không tìm thấy nhân viên')

    #9. Đếm số nhân viên
    elif choice==9:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            sl=len(dsNV)
            print(f'Tổng nhân viên: {sl}')

    #10. Tổng lương hàng tháng
    elif choice==10:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            total=sum(nv.salary for nv in dsNV)
            print(f'Tổng nhân viên tháng: {total:.2f}')
    
    #11. Trung bình lương nhân viên
    elif choice==11:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            total=sum(nv.salary for nv in dsNV)
            sl=len(dsNV)
            print(f'Trung bình lương nhân viên tháng: {(total/sl):.2f}')
    
    #12. Trung bình tuổi nhân viên
    elif choice==12:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            total=sum(nv.age for nv in dsNV)
            sl=len(dsNV)
            print(f'Trung bình tuổi: {(total/sl):.2f}')

    #13. Danh sách nhân viên có tuổi lớn nhất
    elif choice==13:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            max_age=max(nv.age for nv in dsNV)
            for nv in dsNV:
                if nv.age==max_age:
                    nv.display()

    #14. Sắp xếp danh sách nhân viên tăng theo lương
    elif choice==14:
        if not dsNV:
            print('Danh sách rỗng')
        else:
            dsNV.sort(key=lambda nv:nv.salary)
            for nv in dsNV:
                nv.display()
    
    #15. Vẽ biểu đồ tương quan lương theo tuổi
    elif choice==15:
        arrTuoi=[nv.age for nv in dsNV]
        arrLuong=[nv.salary for nv in dsNV]
         #vẽ đồ thị
        plt.figure(figsize=(10,5))
        plt.title('Tương quan lương theo tuổi')
        plt.xlabel('Tuổi')
        plt.ylabel('Lương')
        plt.plot(arrTuoi,arrLuong,'go')
        plt.grid(True)
        plt.show()
    
    #16. Vẽ biểu đồ so sánh lương trung bình các nhóm tuổi
    elif choice==16:
        under_35=[nv.salary for nv in dsNV if nv.age<35]
        between_35_and_50=[nv.salary for nv in dsNV if 35<=nv.age<=50]
        over_50=[nv.salary for nv in dsNV if nv.age>50]
        avg_under_35=sum(under_35)/len(under_35) if under_35 else 0
        avg_35_50=sum(between_35_and_50)/len(between_35_and_50) if between_35_and_50 else 0
        avg_over_50=sum(over_50)/len(over_50) if over_50 else 0
        age_groups=['Under 35', '35-50', 'Over 50']
        avg_salaries=[avg_under_35,avg_35_50,avg_over_50]
        plt.bar(age_groups,avg_salaries,color=['blue','red','green'])
        plt.xlabel('Nhóm tuổi')
        plt.ylabel('Trung bình lương')
        plt.title('Trung bình lương các nhóm tuổi')
        plt.show()

    #17. Vẽ biểu đồ thể hiện phần trăm tổng lương các nhóm tuổi
    elif choice==17:
        under_35=sum(nv.salary for nv in dsNV if nv.age<35)
        between_35_and_50=sum(nv.salary for nv in dsNV if 35<=nv.age<=50)
        over_50=sum(nv.salary for nv in dsNV if nv.age>50)
        salaries=[under_35,between_35_and_50,over_50]
        labels=['Dưới 35','Từ 35 đến 50','Trên 50']
        plt.figure(figsize=(8,8))
        plt.pie(salaries,labels=labels,autopct='%1.1f%%',startangle=140,colors=['blue','red','green'])
        plt.title('Phần trăm tổng lương theo nhóm tuổi')
        plt.show()
    
    #18. Vẽ biểu đồ thể hiện phần trăm số nhân viên theo nhóm tuổi
    elif choice==18:
        under_35=sum(1 for nv in dsNV if nv.age<35)
        between_35_and_50=sum(1 for nv in dsNV if 35<=nv.age<=50)
        over_50=sum(1 for nv in dsNV if nv.age>50)
        sl=[under_35,between_35_and_50,over_50]
        labels=['Dưới 35','Từ 35 đến 50','Trên 50']
        plt.figure(figsize=(8,8))
        plt.pie(sl,labels=labels,autopct='%1.1f%%',startangle=140,colors=['blue','red','green'])
        plt.title('Phần trăm số nhân viên theo nhóm tuổi')
        plt.show()

    #19.Lưu thông tin
    elif choice==19:
        fw=open('nv.db',mode='w',encoding='utf-8')
        for nv in dsNV:
            fw.write(f'{nv.code}-{nv.name}-{nv.age}-{nv.salary}\n')
        fw.close()

    #Thoát
    else:
        print('Thoát chương trình BYE BYE')
        break