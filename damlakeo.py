import random
def suluachon(luachon):
    if luachon == "D":
        return "da"
    elif luachon == "K":
        return  "keo"
    elif luachon == "G":
        return  "giay"
    else:
        return "Ban da nhap sai, vui long nhap lai  "
def main():
    print("chao mung den voi game dam la keo...!")
    print("[D]= da, [K] = keo,[G] = giay and [Q] = thoat game")
    luachon = ["D","K","G"]
    counter = 1
    game_on = True
    while game_on:
        nguoi_choi = input(f"game #{counter}.Hay nhap lua chon cua ban:  ")
        nguoi_choi = nguoi_choi.upper()
        if nguoi_choi == "Q":
            print("cam on cac ban da choi game. chuc ban ngay moi vui ve !")
            game_on = False
        else:
            random_index = random.randint(0,2)
            may_choi = luachon[random_index]
            print(f"Ban da chon {suluachon(nguoi_choi)} vs may chon {suluachon(may_choi)}")
            if nguoi_choi == "D" and may_choi == "K":
                print("Chuc mung ban da thang,'Da thang keo'")
            elif nguoi_choi == "G" and may_choi == "D":
                print("Chuc mung ban da thang'giay thang da'")
            elif nguoi_choi == "K" and may_choi == "G":
                print("Chuc mung ban da thang'Keo thang giay'")
            elif nguoi_choi == "G" and may_choi == "D":
                print("rat tiec. may da win'giay thang da'")
            elif nguoi_choi == "G" and may_choi == "K":
                print("rat tiec. may da win'Keo thang giay'")
            elif nguoi_choi == "D" and may_choi == "G":
                print("rat tiec. may da win'giay thang da'")
            elif nguoi_choi == "K" and may_choi == "D":
                print("rat tiec. may da win'da thang keo'")
            elif nguoi_choi == may_choi:
                print(f"oi roi oi hoa roi ban va may deu chon {suluachon(nguoi_choi)}")
            else:
                print("Chi duoc nhap [B,K,G]: ")
            counter +=1
            print("___"*10)
if __name__ == "__main__":
    main()