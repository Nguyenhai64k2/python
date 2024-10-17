print ("Sinh vien : Nguyen Dinh Hai ")
print ("MSSV 23575202161028")
print ("####################")
def benefit(t, n, k):
    return n * (1 + t / 100) **k
# Nhap tu ban phim
t=float(input("Nhap lai suat (%/ thang):"))
n=float(input("Nhap so von ban dau:"))
k=int(input("nhap so thang gui:"))

# Tinh so tien nhan duoc sau k thang gui
so_tien = benefit(t, n, k)
print(f"so tien nha duoc sau {k} thang gui la: {so_tien:.2f}")
