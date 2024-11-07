print("Nguyen Dinh Hai")
print("MSSV: 235752021610028")
print("############################")
class HinhChunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        # Tính diện tích hình chữ nhật
        return self.chieu_dai * self.chieu_rong
hcn= HinhChunhat(2, 3)
dien_tich= hcn.tinh_dien_tich()
print("Diện tich hình chữ nhật là:", dien_tich)
