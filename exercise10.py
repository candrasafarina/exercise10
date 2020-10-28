#bangun class segitiga

class segitiga:
    def __init__(self, a=20, b=15, c=10, d=20, t=20):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.t = t

    def luasSegitiga(self):
        print("luas Segitiga :", 0.5 * self.a * self.t)

    def kelilingSegitiga(self):
        print("Keliling Segitiga :", self.a + self.b + self.c)

    def luasPersegiPanjang(self):
        print("Luas Persegi panjang :", self.a * self.b)

    def kelilingPersegiPanjang(self):
        print("Keliling Persegi panjang :", self.a + self.b + self.c + self.d) 

luas1 = segitiga()
luas1.luasSegitiga()

keliling1 = segitiga(a=10, b=10, c=12)
keliling1.kelilingSegitiga()

luaspersegi = segitiga()
luaspersegi.luasPersegiPanjang()

kelilingpersegi = segitiga()
kelilingpersegi.kelilingPersegiPanjang()


print("\n")


data = [{"name" : "luke skywalker", "jabatan" : "Jedi master"},
        {"name" : "mandra", "jabatan" : "supir"}
    ]
"""
data.append({"name" : "udin", "jabatan" : "pengusaha"})
print(data)
"""

class recordata:
    def __init__(self):
        self.record = data

    def save(self, nama, jabatan):
        self.record.append({"nama " : nama, 
                            "jabatan ": jabatan})

    def getData(self):
        return self.record

list = recordata()
list.save('luke', 'master')
list.save('udin', 'supir')

print(list.getData())
    
