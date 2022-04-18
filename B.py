def arrsize(arr):
    return len(arr)

def euler(sizearr):
    e = 2.718
    pi = 3.14
    j = -1**0.5
    return e**((-2*pi*j)/sizearr)

def matriks(isiarray):
    return [[isiarray**0*0,isiarray**1*0,isiarray**2*0,isiarray**3*0,isiarray**4*0,isiarray**5*0],
        [isiarray**0*1,isiarray**1*1,isiarray**2*1,isiarray**3*1,isiarray**4*1,isiarray**5*1],
        [isiarray**0*2,isiarray**1*2,isiarray**2*2,isiarray**3*2,isiarray**4*2,isiarray**5*2],
        [isiarray**0*3,isiarray**1*3,isiarray**2*3,isiarray**3*3,isiarray**4*3,isiarray**5*3],
        [isiarray**0*4,isiarray**1*4,isiarray**2*4,isiarray**3*4,isiarray**4*4,isiarray**5*4],
        [isiarray**0*5,isiarray**1*5,isiarray**2*5,isiarray**3*5,isiarray**4*5,isiarray**5*5]]

def MatriksFourier(Matriks,Pengali):
    return[
        Matriks[0][0]*Pengali[0]+Matriks[0][1]*Pengali[1]+Matriks[0][2]*Pengali[2]+Matriks[0][3]*Pengali[3]+Matriks[0][4]*Pengali[4]+Matriks[0][5]*Pengali[5],
        Matriks[1][0]*Pengali[0]+Matriks[1][1]*Pengali[1]+Matriks[1][2]*Pengali[2]+Matriks[1][3]*Pengali[3]+Matriks[1][4]*Pengali[4]+Matriks[1][5]*Pengali[5],
        Matriks[2][0]*Pengali[0]+Matriks[2][1]*Pengali[1]+Matriks[2][2]*Pengali[2]+Matriks[2][3]*Pengali[3]+Matriks[2][4]*Pengali[4]+Matriks[2][5]*Pengali[5],
        Matriks[3][0]*Pengali[0]+Matriks[3][1]*Pengali[1]+Matriks[3][2]*Pengali[2]+Matriks[3][3]*Pengali[3]+Matriks[3][4]*Pengali[4]+Matriks[3][5]*Pengali[5],
        Matriks[4][0]*Pengali[0]+Matriks[4][1]*Pengali[1]+Matriks[4][2]*Pengali[2]+Matriks[4][3]*Pengali[3]+Matriks[4][4]*Pengali[4]+Matriks[4][5]*Pengali[5],
        Matriks[5][0]*Pengali[0]+Matriks[5][1]*Pengali[1]+Matriks[5][2]*Pengali[2]+Matriks[5][3]*Pengali[3]+Matriks[5][4]*Pengali[4]+Matriks[5][5]*Pengali[5]
    ] 
def main():
    Soal = [1,1,1,1,1,1]
    N = len(Soal)
    W = euler(N)
    M = matriks(W)
    H = MatriksFourier(M,Soal)
    print("Hasil DFT: ",H)
main()