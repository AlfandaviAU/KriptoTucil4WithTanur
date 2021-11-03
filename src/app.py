from flask import Flask, render_template, request, redirect, url_for
from forms import Todo
from rsa import *
from elGamal import *
from paillier import *
from ecc import *
import sys, os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

# Output steganography
try:
    os.mkdir("output")
except:
    pass

@app.route('/', methods=['GET', 'POST'])
def main():
    request_method = request.method
    return render_template('index.html',request_method=request_method)


@app.route('/rsa', methods=['GET', 'POST'])
def page_rsa():
    request_method = request.method
    # if len(request.form) == 0:
    #     result = ""
    # else:
    #     if len(request.files.get("srcfile").filename) != 0:
    #         srctext = request.files.get("srcfile").read()
    #         outputfile = "output/rc4-" + request.files.get("srcfile").filename
    #     else:
    #         srctext = request.form.get("message")
    #         outputfile = "output/rc4-manual"


    #     if len(rckey) > 0:
    #         result  = mod_rc4(srctext, rckey)

    #     with open(outputfile, "w") as file:
    #         file.write(str(result.encode('utf-8')))

    # return render_template('rc4.html',request_method=request_method, result=result)\
    return render_template('rsa.html',request_method=request_method)

@app.route('/enc_rsa', methods=['GET', 'POST'])
def enc_rsa():
    request_method = request.method
    p   = int(request.form.get("p"))
    q   = int(request.form.get("q"))
    e   = int(request.form.get("e"))
    plainteks   = request.form.get("plainteks")
    res2 = encryptRSA(olahPesanFromKalimat(plainteks),p,q,e)
    print(res2)
    res = ' '.join([str(elem) for elem in res2])
    return render_template('rsa.html',request_method=request_method, res = res)

@app.route('/dec_rsa', methods=['GET', 'POST'])
def dec_rsa():
    request_method = request.method
    p   = int(request.form.get("p"))
    q   = int(request.form.get("q"))
    e   = int(request.form.get("e"))
    cipherteks2   = request.form.get("cipherteks")
    cipherteks = cipherteks2.split(" ")
    res2 = decryptRSA(cipherteks,p,q,generateKunciDekripsi(47,71,79))
    res3 = (olahPesanToKalimat(res2))
    res = ''.join([str(elem) for elem in res3])
    return render_template('rsa.html',request_method=request_method, res = res.upper())

@app.route('/elgamal', methods=['GET', 'POST'])
def page_elgamal():
    request_method = request.method
    return render_template('elGamal.html',request_method=request_method)

@app.route('/enc_elGamal', methods=['GET', 'POST'])
def enc_elGamal():
    request_method = request.method
    p   = int(request.form.get("p"))
    g   = int(request.form.get("g"))
    x   = int(request.form.get("x"))
    k   = int(request.form.get("k"))
    plainteks   = int(request.form.get("plainteks"))
    publicKey = bangkitKunciElGamal(p,g,x)["public"]
    res = enkripsiElGamal(p,g,x,publicKey,plainteks,k)
    return render_template('elGamal.html',request_method=request_method, res = res)

@app.route('/dec_elGamal', methods=['GET', 'POST'])
def dec_elGamal():
    request_method = request.method
    p   = int(request.form.get("p"))
    g   = int(request.form.get("g"))
    x   = int(request.form.get("x"))
    cipherteks   = (request.form.get("ciphertext"))
    cipherteks = cipherteks.replace("(","")
    cipherteks = cipherteks.replace(")","")
    cipherteks = cipherteks.split(",")
    privateKey = bangkitKunciElGamal(p,g,x)["private"]
    # print(cipherteks)
    res = dekripsiElGamal(p,g,x,cipherteks,privateKey)
    # print(res)
    return render_template('elGamal.html',request_method=request_method, res = res)


@app.route('/paillier', methods=['GET', 'POST'])
def page_paillier():
    request_method = request.method
    return render_template('pailier.html',request_method=request_method)

# @app.route('/enc_paillier', methods=['GET', 'POST'])
# def enc_paillier():
#     request_method = request.method
#     pt   = int(request.form.get("plainteks"))
#     key = paillier_keygen()
#     res = paillier_enc(pt,key["public"])
#     return render_template('pailier.html',request_method=request_method, res = res)



@app.route('/ecc', methods=['GET', 'POST'])
def page_ecc():
    request_method = request.method
    return render_template('ecc.html',request_method=request_method)

# @app.route('/enc_stegano', methods=['GET', 'POST'])
# def encode_stegano():
#     srcfilename = request.files.get("cover-file").filename

#     filestream  = request.files.get("cover-file")
#     outputfile  = "output/steg-" + srcfilename
#     if request.form.get("key") == "":
#         stegoKey = None
#     else:
#         stegoKey = request.form.get("key")

#     embedfilestream = request.files.get("embed-file")
#     embeddedmsg     = embedfilestream.read()

#     stegoEnc = request.form.get("metode-steg")
#     if stegoEnc == "with-enc" and len(stegoKey) > 0:
#         embeddedmsg = mod_rc4(embeddedmsg, stegoKey)
#     stegEncoder = None
#     if srcfilename.split(".")[1].lower() == "png":
#         stegEncoder = StegPNG(filestream, outputfile)
#     elif srcfilename.split(".")[1].lower() == "wav":
#         stegEncoder = StegWAV(filestream, outputfile)

#     stegEncoder.encode(embeddedmsg, stegoKey)

#     return redirect('/stegano')

# @app.route('/dec_stegano', methods=['GET', 'POST'])
# def decode_stegano():
#     srcfilename = request.files.get("file").filename.split(".")

#     filestream  = request.files.get("file")
#     outputfile  = "output/dec-" + srcfilename[0] + ".txt"
#     if request.form.get("key") == "":
#         stegoKey = None
#     else:
#         stegoKey = request.form.get("key")

#     if srcfilename[1].lower() == "png":
#         stegDecoder = StegPNG(filestream, outputfile)
#     elif srcfilename[1].lower() == "wav":
#         stegDecoder = StegWAV(filestream, outputfile)

#     try:
#         stegDecoder.decode()
#     except:
#         # Objek bukan stego object yang valid / lcg header salah
#         # TODO : Handler ?
#         pass

#     return redirect('/stegano')


if __name__ == '__main__':
    app.run(debug=True)
