def huruf_besar(teks):
    jumlah_huruf_besar = 0
    for huruf in teks:
        if huruf.isupper():
            jumlah_huruf_besar += 1
    return jumlah_huruf_besar